# OASIS auth pages

These pages handle the flows linked from OASIS emails and the auth UX on the site.

| Page | URL | Used by |
|------|-----|--------|
| **register** | `/avatar/register` | Create account. Submits to `POST /api/avatar/register`. |
| **sign-in** | `/avatar/sign-in` | Sign in. Submits to `POST /api/avatar/authenticate`; stores JWT and redirects to `/`. |
| **forgot-password** | `/avatar/forgot-password` | “Email already registered” email (Forgot password? button), or direct visit. Submits to `POST /api/avatar/forgot-password`. |
| **reset-password** | `/avatar/reset-password?token=...` | Link in “Reset your password” email. User sets new password; submits to `POST /api/avatar/reset-password` (token + newPassword; oldPassword sent empty for forgot-password flow). |
| **verify-email** | `/avatar/verify-email?token=...` | Link in “Verify your email” email. Calls `GET /api/avatar/verify-email?token=...` and shows result. |

API base is chosen automatically: production uses `https://api.oasisweb4.com/api`, localhost uses `http://localhost:5003/api`. Override with `window.OASIS_API_BASE` if needed.

The backend supports token-only reset (forgot-password flow): when `oldPassword` is empty and the token is valid, the API resets the password without requiring the old password.

## Edge cases covered

- **Register:** Required fields trimmed and validated; password match and length; terms checkbox; API errors (4xx/5xx) and non-JSON responses shown; double-submit prevented.
- **Sign-in:** Username trimmed and non-empty; 401/4xx body message or generic “Invalid username or password”; network/parse errors caught.
- **Forgot-password:** Email trimmed; success vs error from API by `isError` and “check your email”; non-OK and non-JSON handled.
- **Reset-password:** Missing or empty token shows message and hides form; password match and length; API error message shown (e.g. expired token); success message with link to sign-in.
- **Verify-email:** Missing or empty token shows message; API error/expired message shown; non-JSON and network errors caught.
- **All:** Links use path-only (e.g. `sign-in`, `forgot-password`) so clean URLs work on production and with `server.py`. Footer links on every page: Sign in, Create account, Forgot password (where relevant), Home.
