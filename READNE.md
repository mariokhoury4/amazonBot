# 📉 Amazon Price Tracker Bot

A Python bot that automatically checks Amazon product prices and sends an email alert when the price drops below your defined target. Tracks multiple products and runs headlessly using Selenium + BeautifulSoup.

---

## 🛠 Features

- ✅ Tracks multiple Amazon products via a `products.json` file
- ✅ Sends email alerts (Outlook or Gmail) when price drops
- ✅ Headless Chrome browser for fast scraping
- ✅ Clean code structure (modular Python files)
- ✅ Debug logs and fallback HTML dump when blocked

---

## 🧪 Example Usage

```bash
python main.py
```

## 🗂 Project Structure
```
amazon-price-tracker/
├── main.py                 # Entry point
├── config.py               # Email receiver, constants
├── products.json           # List of products to track
├── browser.py              # Headless Chrome setup
├── email_utils.py          # Outlook or Gmail email sender
├── price_checker.py        # Scraper & logic
├── utils.py                # Helpers (title/price extractors)
├── requirements.txt        # Pip dependencies
├── .env                    # (Optional) Secrets (email user/pass)
└── README.md               # You're reading it!

```
## 🔧 Configuration   
products.json
```
[
  {
    "url": "https://www.amazon.com/dp/B0CL12QNNK",
    "target_price": 70.00
  },
  {
    "url": "https://www.amazon.com/dp/B08FC5L3RG",
    "target_price": 89.00
  }
]

```

## .env (Optional)
Create a .env file in the project root with:

```
EMAIL_USER=youremail@outlook.com
EMAIL_PASS=your_app_password
```
If using Gmail: generate an App Password
If using Outlook: OAuth2 setup is required (see documentation)

## 📦 Installation
```
git clone https://github.com/your-username/amazon-price-tracker.git
cd amazon-price-tracker
pip install -r requirements.txt
```

## 💌 Email Setup
Gmail (easiest)
- Enable 2FA
- Create an App Password
- Paste it into your .env

Outlook
- Outlook no longer supports basic auth
- You must register an Azure app, use OAuth2, and request an SMTP access token

## 🧱 Dependencies
```
selenium
webdriver-manager
beautifulsoup4
requests
requests-oauthlib  # Only needed for Outlook OAuth2
python-dotenv      # Optional, for reading .env
```
Install with:
```
pip install -r requirements.txt
```




