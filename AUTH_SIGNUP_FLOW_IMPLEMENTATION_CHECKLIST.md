# OASIS Auth Signup Flow – Implementation Checklist

Based on research from Clerk, SuperTokens, Authgear, Supabase, and UX best practices. Use this checklist to improve the OASIS email signup flow.

---

## Next steps (in order)

### Step 1: Deploy what’s ready
- [ ] **Commit and push** `AvatarManager-Private.cs` (branded templates, token encoding, base URL)
- [ ] **Deploy ONODE API** to api.oasisweb4.com so verification, reset, and “already registered” emails use the new design
- [ ] **Deploy oasisweb4.com** so the “Log in” button and “email already exists” error handling go live

### Step 2: Wire up “Start building”
- [ ] Add `href` or `onclick` to all “Start building” nav buttons: when logged out → `/avatar/register`; when logged in → `portal/portal.html`
- [ ] Ensure hero “Start building” (links to docs) stays as-is or is updated per product decision

### Step 3: Improve “email already exists” UX
- [ ] On register page: when API returns “email already exists”, show error + “Sign in” and “Forgot password?” links (email prefilled)
- [x] In login modal: same treatment when registration fails for existing email ✅

### Step 4: Post-signup “check your inbox”
- [ ] After successful registration, show a clear “Check your inbox” state (or redirect to a dedicated page)
- [ ] Add “Check your spam folder” hint
- [ ] Add “Resend verification email” button (requires API endpoint if missing)

### Step 5: Resend verification
- [ ] Add API endpoint: `POST /api/avatar/resend-verification` (email in body) – resends if user exists and not verified
- [ ] Add “Resend” button on verify-email page (for expired/missing emails) with 60s cooldown

### Step 6: Auto-login after verify
- [ ] On verify-email page: when verification succeeds, call authenticate API, store token, redirect to portal

### Step 7: Polish error states
- [ ] Expired verification link: friendly message + “Request new verification email” CTA
- [ ] Expired reset link: friendly message + “Request new reset link” → forgot-password
- [ ] Network error: “We’re having trouble connecting” + Retry, preserve form data

### Step 8: Form UX improvements
- [ ] Add “Show password” toggle (eye icon) to password fields
- [x] Add inline password validation on register (6+ chars with ✓ when met) ✅
- [x] Autocomplete attributes on auth inputs ✅

---

## 1. Error handling & messaging

- [ ] **Email already exists** – Show on-page message immediately (API returns 200 + `isError`). ✅ *Partially done – verify modal + register page both display it.*
- [ ] **Email already exists – UX upgrade** – When detected, prefill email, show "Sign in" and "Forgot password?" links (don’t just show error text).
- [ ] **Expired verification link** – Show friendly message: "This link has expired. Request a new verification email." with a single CTA.
- [ ] **Expired reset link** – Same pattern on reset-password page; "Request a new link" → forgot-password.
- [ ] **Network/server error** – Show "We're having trouble connecting. Please try again." with Retry; never clear user input.
- [ ] **Wrong password** – Keep email/username prefilled; show error near password field; after 2–3 failures, surface "Forgot password?" more prominently.

---

## 2. Post-signup & verification flow

- [ ] **"Check your inbox" page** – After successful registration, show a dedicated page (or clear state) with:
  - "We've sent a verification link to [email]"
  - "Check your spam folder if you don't see it"
  - **Resend email** button (with cooldown, e.g. 60 seconds)
- [ ] **Resend verification** – Add API support (if not exists) and "Resend" on verify-email page for expired/missing emails.
- [ ] **Auto-login after verify** – After successful email verification, sign the user in and redirect to portal (don’t show "Now sign in").
- [ ] **Welcome state** – After first login post-verify, show a brief welcome message or onboarding hint.

---

## 3. Signup form UX

- [ ] **Inline password validation** – Show requirements (length, complexity) as user types; green checkmarks when met.
- [ ] **"Show password" toggle** – Add eye icon to password fields; consider removing "Confirm password" in favor of show + careful entry.
- [ ] **Minimal fields** – Evaluate if username is required; consider email-only signup with optional display name later.
- [ ] **Social login** – Add "Sign in with Google" (or similar) to reduce friction and auto-verify email.
- [ ] **Clear CTAs** – Use "Create account" or "Sign up" (not vague "Continue"); keep primary button prominent.

---

## 4. Email templates & delivery

- [ ] **Branded templates live** – Deploy API with `EmailTemplates.cs` and `AvatarManager-Private.cs` changes so verification, reset, and "already registered" emails use the new design.
- [ ] **Email deliverability** – Configure SPF, DKIM, DMARC for sending domain; consider separate subdomain for transactional email.
- [ ] **Link prefetch protection** – Optional: verify-email page shows "Verify" button; token consumed only on button click (avoids email client prefetch consuming token).

---

## 5. Forgot password & reset flow

- [ ] **Streamlined reset** – Single screen: enter email → "Check your inbox" → reset-password page. No extra steps.
- [ ] **Resend reset email** – "Didn't get it? Resend" on a waiting/error state.
- [ ] **Success feedback** – After password reset, show "Password updated. Sign in with your new password." and auto-redirect to sign-in.

---

## 6. Navigation & entry points

- [ ] **"Log in" always visible** – Button label stays "Log in" (not "Account"); click → portal if logged in, modal if not. ✅ *Done.*
- [ ] **"Start building" works** – When logged out → `/avatar/register`; when logged in → portal. ✅ *To be implemented.*
- [ ] **Consistent auth links** – Sign in, Create account, Forgot password visible where relevant across all auth pages.

---

## 7. Security & tokens

- [ ] **Token length** – Verification and reset tokens are 64–128 chars (current hex tokens are fine).
- [ ] **Token expiry** – Verification: 24h typical; reset: 24h. Document and enforce.
- [ ] **Token reuse on resend** – When user requests "Resend verification", reuse existing token if not expired (simpler UX than invalidating).

---

## 8. Accessibility & mobile

- [ ] **Autocomplete attributes** – `autocomplete="email"`, `autocomplete="username"`, `autocomplete="new-password"` on inputs.
- [ ] **ARIA labels** – Error messages and form fields have appropriate `aria-describedby` / `aria-invalid`.
- [ ] **Mobile tap targets** – Buttons and links at least 44×44px; responsive layout.
- [ ] **Password paste allowed** – Do not disable paste on password fields (WCAG 2.2, password managers).

---

## Priority order (suggested)

| Priority | Item | Effort |
|----------|------|--------|
| P0 | Deploy branded email templates (API) | Deploy |
| P0 | "Email already exists" on-page + prefill/sign-in links | Small |
| P1 | Resend verification email | Medium |
| P1 | Auto-login after verify | Small |
| P1 | "Check your inbox" page with resend | Small |
| P2 | "Start building" → register/portal | Small |
| P2 | Inline password validation | Medium |
| P2 | Show password toggle | Small |
| P3 | Social login (Google) | Large |
| P3 | Optional username / email-only signup | Medium |

---

## References

- [Clerk: How We Roll – Email Verification](https://clerk.com/blog/how-we-roll-email-verification)
- [SuperTokens: Implementing the right email verification flow](https://supertokens.com/blog/implementing-the-right-email-verification-flow)
- [Authgear: Login & Signup UX Guide 2025](https://www.authgear.com/post/login-signup-ux-guide)
- [Supabase Auth](https://supabase.com/docs/guides/auth/passwords)
- [NN/g: Error Message Guidelines](https://www.nngroup.com/articles/errors-forms-design-guidelines/)
