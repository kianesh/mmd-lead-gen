# 🧲 Yelp Lead Scraper with AI-Powered Online Presence Analysis

This Python script scrapes business listings from Yelp by category and location, then analyzes each business’s online presence using OpenAI's GPT. It's perfect for web designers, marketers, or agencies looking to find and qualify high-quality leads.

---

## ⚙️ Features

- 🔎 Scrapes Yelp businesses by **city** and **category**
- 📞 Collects **name**, **phone**, **Yelp URL**, and **website**
- 🤖 Uses **GPT-3.5/4** to analyze each business's **online presence**
- 🧠 Scores leads based on their likelihood of needing digital services
- 📤 Exports results to a clean **CSV** file

---

## 📦 Requirements

Before running the script, make sure you have:

- Python 3.7+
- Yelp Fusion API Key
- OpenAI API Key
- `.env` file with credentials (see below)

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Example `requirements.txt`:
```text
python-dotenv
openai
pandas
yelpapi
```

---

## 🔐 .env Setup

Create a `.env` file in the root directory of your project with:

```
YELP_CLIENT_ID=your_yelp_client_id
YELP_API_KEY=your_yelp_api_key
OPENAI_API_KEY=your_openai_api_key
```

---

## 🚀 How to Run

In your terminal:

```bash
python yelp_scraper.py
```

You’ll be prompted to enter:

- A **city** (e.g., `Toronto`)
- A **business category** (e.g., `painters`)
- The number of **pages** to scrape (each page = ~50 leads)

---

## 📊 Output

The script will generate a `yelp_leads.csv` file that includes:

- Business Name
- Phone Number
- Website / Yelp URL
- Online Presence Summary
- Lead Score (higher = more likely to need help)

---

## 🧠 How Lead Scoring Works

- Businesses with **no website** = +3 points  
- Businesses with **no phone number** = +2 points  
- Base score = 1  

You can use this score to **prioritize outreach** for businesses most likely in need of help.

---

## 📬 Use Case Ideas

Perfect if you:
- Run a web design or digital marketing agency
- Want to offer Google Business Profile help
- Sell SEO, PPC, or website services
- Do cold outreach (email, IG, FB, etc.)

---

## ⚠️ Notes

- Be mindful of **rate limits** — this script waits between API calls
- OpenAI usage will count toward your quota
- This is for **educational and ethical lead gen only**

---

## 🧠 Want Custom Features?

DM me on Instagram or comment on my video if you want:
- Auto-email or text follow-ups
- Built-in CRM sync
- AI outreach personalization
- Live dashboard

