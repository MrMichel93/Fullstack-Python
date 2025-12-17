# Extension Challenges - URL Shortener

## 🌟 Beginner Challenges

### 1. Custom Short Codes
Allow users to choose their own short code instead of random generation.
- Add optional "custom_code" field to form
- Validate: alphanumeric, 3-20 characters
- Check availability before saving

### 2. QR Code Generation
Generate QR codes for shortened URLs.
- Install: `pip install qrcode[pil]`
- Create route `/qr/<short_code>`
- Return QR code image
- Add QR code display on results page

### 3. URL Preview
Show a preview page before redirecting.
- Add `/preview/<short_code>` route
- Display original URL, creation date, clicks
- Show "Continue to destination" button
- Optional: Add timer auto-redirect

## 🔥 Intermediate Challenges

### 4. Link Expiration
Add expiration dates to shortened URLs.
- Add `expires_at` column
- Optional field in creation form
- Check expiration before redirecting
- Show "Link Expired" message

### 5. Analytics Dashboard
Show detailed statistics for each link.
- Track: clicks, referrers, user agents, countries
- Create analytics table
- Display charts (using Chart.js)
- Show click timeline

### 6. Bulk URL Shortening
Allow shortening multiple URLs at once.
- Accept CSV file upload
- Process each URL
- Return CSV with short codes
- Show progress indicator

## 🚀 Advanced Challenges

### 7. REST API
Create API endpoints for programmatic access.
- `POST /api/shorten` - Create short URL
- `GET /api/stats/<code>` - Get statistics
- `DELETE /api/<code>` - Delete link
- Add API key authentication

### 8. Link Editing
Allow editing destination URLs without changing short code.
- Add edit functionality
- Preserve statistics
- Log edit history
- Require authentication

### 9. Password Protection
Add optional password to protected links.
- Add `password_hash` column
- Show password prompt before redirect
- Rate limit attempts
- Implement CAPTCHA for security

## 🏆 Expert Challenges

### 10. URL Validation & Safety
Check URLs for safety before shortening.
- Integrate Google Safe Browsing API
- Block malicious domains
- Warn users about risky links
- Maintain blocklist

### 11. A/B Testing
Support multiple destinations for one short code.
- Random or weighted distribution
- Track conversion rates
- Compare performance
- Dashboard for results

### 12. Branded Domains
Support custom domains for short links.
- Allow `yourdomain.com/abc` instead of `yourapp.com/abc`
- Domain verification
- SSL certificate management
- DNS configuration guide
