# Local Testing & How the Website Connects to the API

## How the subscription flow connects

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  BROWSER (you visit the site)                                                    │
└─────────────────────────────────────────────────────────────────────────────────┘
    │
    │  getApiBaseUrl() decides base URL:
    │  • Production (oasisweb4.com / www.oasisweb4.com) → https://api.oasisweb4.com/api
    │  • localStorage 'oasis_api_url' set → that value (e.g. http://localhost:8080/api-proxy/api)
    │  • Else (local dev) → origin + '/api-proxy/api'  (e.g. http://localhost:8080/api-proxy/api)
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│  SITE (static HTML/JS)                                                           │
│  • pricing.html, checkout-success.html, etc.                                     │
│  • Calls: GET  {API_BASE_URL}/subscription/plans                                  │
│            POST {API_BASE_URL}/subscription/checkout/session                      │
└─────────────────────────────────────────────────────────────────────────────────┘
    │
    │  Local only: requests go to same origin /api-proxy/... → handled by server.py
    │  Production: requests go directly to https://api.oasisweb4.com/api/...
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│  LOCAL: Python proxy (server.py :8080)                                            │
│  /api-proxy/*  →  forwards to  https://localhost:5004/*                            │
│  (avoids mixed content when page is http://localhost:8080)                       │
└─────────────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│  OASIS ONODE API (https://localhost:5004 or https://api.oasisweb4.com)           │
│  • GET  /api/subscription/plans           → SubscriptionController.GetPlans()    │
│  • POST /api/subscription/checkout/session → SubscriptionController (Stripe)    │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## URL resolution summary

| Where you're running the site | API base URL used |
|-------------------------------|-------------------|
| https://www.oasisweb4.com     | `https://api.oasisweb4.com/api` |
| https://oasisweb4.com         | `https://api.oasisweb4.com/api` |
| http://localhost:8080         | `http://localhost:8080/api-proxy/api` (proxied to ONODE) |
| Any other host                | `{origin}/api-proxy/api` (relies on server.py proxy) |
| Override                      | Set `localStorage.setItem('oasis_api_url', 'https://api.oasisweb4.com/api')` in console |

---

## Run the site locally

### 1. With ONODE API (full subscription + auth test)

**Terminal 1 – start the ONODE API**

```bash
cd /path/to/OASIS_CLEAN/ONODE/NextGenSoftware.OASIS.API.ONODE.WebAPI
dotnet run --urls "http://localhost:5003"
```

Leave it running. It serves at **http://localhost:5003** (first build can take 1–2 minutes).

**Auth pages (register, sign-in, forgot-password, etc.)** use **http://localhost:5003/api** when you open the site from localhost, so they talk to this local API. No proxy needed for auth.

**Terminal 2 – start the site + proxy**

```bash
cd /path/to/OASIS_CLEAN/oasisweb4.com-repo
python3 server.py
```

Site is at **http://localhost:8080**.

**Browser**

- Home: http://localhost:8080/
- Pricing (subscription): http://localhost:8080/pricing.html

The pricing page will:

1. Use `http://localhost:8080/api-proxy/api` as the API base.
2. Load plans from `GET .../subscription/plans` (proxied to ONODE).
3. “Choose plan” → `POST .../subscription/checkout/session` (proxied to ONODE).  
   Checkout only works if ONODE has Stripe keys set; otherwise you’ll get a config error.

### 2. Without ONODE (UI only)

```bash
cd /path/to/OASIS_CLEAN/oasisweb4.com-repo
python3 server.py
```

Then open http://localhost:8080/pricing.html.

- Calls to `/api-proxy/api/...` will fail (connection refused to localhost:5004).
- The page will show the **fallback plans** and the error line, so you can confirm the UI and that it tried the right URL.

### 3. Local UI against production API

To drive the live API from your local copy of the site:

1. Open http://localhost:8080/pricing.html (with `python3 server.py` running, or any simple static server).
2. Open DevTools → Console and run:

   ```js
   localStorage.setItem('oasis_api_url', 'https://api.oasisweb4.com/api');
   location.reload();
   ```

3. The pricing page will now call **https://api.oasisweb4.com/api** for plans and checkout.  
   CORS must allow your origin (e.g. `http://localhost:8080`); if it doesn’t, you’ll see CORS errors in the console.

---

## Quick checks

| What you want to verify | How |
|-------------------------|-----|
| Correct API base on production | On oasisweb4.com, open pricing and check console: `OASIS API Base URL: https://api.oasisweb4.com/api` |
| Correct API base locally | On localhost:8080, console: `OASIS API Base URL: http://localhost:8080/api-proxy/api` |
| Plans load from API | Pricing shows 4 plans (Bronze, Silver, Gold, Enterprise); no “Failed to load plans” and no fallback-only message |
| Checkout hits API | Click “Choose Silver” (or similar); if Stripe is configured you get redirected to Stripe; if not, an alert with the API error |
| Override URL | Use `localStorage.setItem('oasis_api_url', '...')` then reload; next request uses that base |

**“Stripe keys not configured” when you click Choose Silver?**  
The ONODE API needs Stripe keys. See **ONODE/NextGenSoftware.OASIS.API.ONODE.WebAPI/STRIPE_CHECKOUT_SETUP.md** for setting `STRIPE_PUBLISHABLE_KEY` and `STRIPE_SECRET_KEY` (env vars or `appsettings.Development.json`), then restart ONODE.

---

## File roles

- **pricing.html** – Reads `getApiBaseUrl()`, calls `/subscription/plans` and `/subscription/checkout/session`, shows plans and “Choose plan” buttons.
- **server.py** – Serves the static site and proxies `/api-proxy/*` to `https://localhost:5004/*` so local dev works without CORS/mixed content.
- **checkout-success.html** – Shown after Stripe success redirect (configured in the checkout request).
- **checkout-cancel.html** – Shown if user cancels in Stripe (link can be set in success page or Stripe config).
