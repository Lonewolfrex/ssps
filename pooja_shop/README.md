# Pooja Shop — Django E‑Commerce (with CAPEX/OPEX)
Features:
- Product catalog, categories, search-ready structure
- Cart (session-based), checkout form, order creation
- Inventory tracking (reduces stock on order)
- Razorpay integration placeholder (create order + webhook)
- Admin: manage products, orders, coupons
- Admin-only Expenses module (CAPEX/OPEX) with dashboard

## Quickstart
```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Seed Data (optional)
Use Django admin to add Categories & Products (image optional).

## Payments
Set environment variables (or .env file):
```
DJANGO_SECRET_KEY=change-this
RAZORPAY_KEY_ID=your_key_id
RAZORPAY_KEY_SECRET=your_key_secret
DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Expenses (Admin)
Visit `/expenses/dashboard/` (must be staff user). Add CAPEX/OPEX via the form or directly in Django Admin.

## Deploy Notes
- Use `whitenoise` for static files (already configured).
- For production: DEBUG=0, set ALLOWED_HOSTS, and configure a proper DB (PostgreSQL recommended).
- Serve with gunicorn/uvicorn behind nginx; configure media storage (S3/GCS) for product images.


## Branding
- Brand: Satvik Sparsh Pooja Store
- Theme: Light saffron `#ffc766`
- Logo: `static/img/logo.png`

## Google Pay (UPI)
A UPI intent button is shown on the order success page.
Set these in your `.env`:
```
UPI_VPA=yourname@okaxis
UPI_NAME=Satvik Sparsh Pooja Store
```
Clicking the button opens Google Pay with the amount and note.
