#!/usr/bin/env python3
import http.server
import socketserver
import urllib.request
import json
import sys
import os

PORT = int(os.environ.get('PORT', 8081))

# Clean URL -> file path (relative to repo root)
AUTH_ROUTES = {
    '/avatar/register': 'avatar/register.html',
    '/avatar/sign-in': 'avatar/sign-in.html',
    '/avatar/forgot-password': 'avatar/forgot-password.html',
    '/avatar/reset-password': 'avatar/reset-password.html',
    '/avatar/verify-email': 'avatar/verify-email.html',
}

class ProxyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Auth clean URLs: serve the corresponding HTML file directly
        path_only = self.path.split('?')[0]
        if path_only in AUTH_ROUTES:
            file_path = AUTH_ROUTES[path_only]
            if os.path.isfile(file_path):
                try:
                    with open(file_path, 'rb') as f:
                        body = f.read()
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/html; charset=utf-8')
                    self.send_header('Content-Length', len(body))
                    self.end_headers()
                    self.wfile.write(body)
                    return
                except Exception:
                    pass
            # fall through to 404 via super()
        # Proxy API requests to avoid mixed content issues
        if self.path.startswith('/api-proxy/'):
            api_path = self.path.replace('/api-proxy', '')
            try:
                # Use HTTPS directly since we're proxying
                url = f'https://localhost:5004{api_path}'
                # Create unverified context to bypass SSL certificate check
                import ssl
                import urllib.error
                context = ssl._create_unverified_context()
                
                req = urllib.request.Request(url)
                try:
                    with urllib.request.urlopen(req, context=context) as response:
                        data = response.read()
                        self.send_response(response.getcode())
                        self.send_header('Content-Type', 'application/json')
                        self.send_header('Access-Control-Allow-Origin', '*')
                        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
                        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                        self.end_headers()
                        self.wfile.write(data)
                except urllib.error.HTTPError as e:
                    # Handle HTTP errors and pass through the error response body
                    error_body = e.read() if hasattr(e, 'read') else b'{}'
                    self.send_response(e.code)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
                    self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                    self.end_headers()
                    self.wfile.write(error_body)
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                error_msg = json.dumps({'error': str(e), 'isError': True, 'message': str(e)}).encode()
                self.wfile.write(error_msg)
        else:
            super().do_GET()
    
    def do_POST(self):
        if self.path.startswith('/api-proxy/'):
            api_path = self.path.replace('/api-proxy', '')
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length) if content_length > 0 else b''
                
                import ssl
                context = ssl._create_unverified_context()
                url = f'https://localhost:5004{api_path}'
                req = urllib.request.Request(url, data=post_data, method='POST')
                req.add_header('Content-Type', self.headers.get('Content-Type', 'application/json'))
                
                try:
                    with urllib.request.urlopen(req, context=context) as response:
                        data = response.read()
                        # Pass through the actual status code from the API
                        self.send_response(response.getcode())
                        self.send_header('Content-Type', 'application/json')
                        self.send_header('Access-Control-Allow-Origin', '*')
                        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
                        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                        self.end_headers()
                        self.wfile.write(data)
                except urllib.error.HTTPError as e:
                    # Handle HTTP errors (like 500) and pass through the error response body
                    error_body = e.read() if hasattr(e, 'read') else b'{}'
                    self.send_response(e.code)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
                    self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                    self.end_headers()
                    self.wfile.write(error_body)
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                error_msg = json.dumps({'error': str(e), 'isError': True, 'message': str(e)}).encode()
                self.wfile.write(error_msg)
        else:
            super().do_POST()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), ProxyHTTPRequestHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}/")
        print(f"API proxy available at http://localhost:{PORT}/api-proxy/")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            sys.exit(0)
