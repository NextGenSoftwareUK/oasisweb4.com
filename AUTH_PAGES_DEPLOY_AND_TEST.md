# Auth Pages: Fix 404 and How to Test

## Why "Forgot password?" in the email gives 404

The **"Email already registered"** and **"Reset your password"** emails contain links like:

- `https://oasisweb4.com/avatar/forgot-password`
- `https://oasisweb4.com/avatar/reset-password?token=...`
- `https://oasisweb4.com/avatar/verify-email?token=...`

Those URLs point at your **live site** (oasisweb4.com). If you see **404 NOT_FOUND** (e.g. from Vercel), it means the **deployed** site does not yet have the auth pages or the rewrites that serve them.

## Fix: Deploy the auth pages

1. **Deploy this repo** (with the latest `avatar/*.html` and `vercel.json` rewrites) to the same Vercel (or host) project that serves **https://www.oasisweb4.com** (or **https://oasisweb4.com**).

2. **Ensure `vercel.json` is in the deploy**  
   It should include rewrites like:
   - `/avatar/forgot-password` → `/avatar/forgot-password.html`
   - `/avatar/register` → `/avatar/register.html`
   - etc.

3. **Match the API base URL to your live site**  
   The API builds email links using **OASISWebSiteURL** (from OASIS DNA / env). That value must match the **canonical** URL of the site you deploy:
   - If the site is **https://www.oasisweb4.com**, set `OASISWebSiteURL = "https://www.oasisweb4.com"`.
   - If the site is **https://oasisweb4.com** (no www), set `OASISWebSiteURL = "https://oasisweb4.com"`.  
   Default in code is `https://oasisweb4.com` (no www). Change it in your API config (e.g. `OASIS_DNA.json` or environment) to match where the front end actually lives.

## How to test that it’s fixed

1. **Deploy** the latest `oasisweb4.com-repo` (with auth pages and `vercel.json`).

2. **Open the forgot-password page in a browser**  
   Use the same base URL as in the emails (with or without www, to match your config):
   - https://www.oasisweb4.com/avatar/forgot-password  
   - or https://oasisweb4.com/avatar/forgot-password  
   You should see the “Reset your password” form, not 404.

3. **Test the “Email already registered” flow**
   - Register (or try to register) with **max@quantumstreet.io** (or any email already in the system).
   - You should get the “Email already registered” email.
   - Click **“Forgot password?”** in that email.
   - The link should open the forgot-password page (no 404). Submit your email and check you get the “Reset your password” email.

4. **Test the reset-password link**
   - In the “Reset your password” email, click the link.
   - It should open the “Set new password” page with the token in the URL. Set a new password and confirm it works.

5. **Optional: test verify-email**
   - Register with a **new** email, then click the verification link in the email. It should open the verify-email page and show success.

## Quick local check (no deploy)

To confirm the **pages and rewrites** are correct before deploying:

- Run the local server: `python3 server.py` (serves on port 8081 by default).
- Open: http://localhost:8081/avatar/forgot-password  
- You should see the forgot-password form. The same URLs work for `/avatar/register`, `/avatar/sign-in`, `/avatar/reset-password`, `/avatar/verify-email`.

Email links will still 404 until the **production** site is deployed with these files and rewrites and **OASISWebSiteURL** points at that production URL.
