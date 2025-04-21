import os
import time

import openai
import pandas as pd
from dotenv import load_dotenv
from yelpapi import YelpAPI

# Load environment variables from the .env file
load_dotenv()

# Retrieve the Yelp API credentials from the environment
CLIENT_ID = os.getenv('YELP_CLIENT_ID')
API_KEY = os.getenv('YELP_API_KEY')
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

if not CLIENT_ID or not API_KEY:
    print("Error: Yelp API credentials are not set in the .env file.")
    exit(1)

# Initialize YelpAPI with the API key
yelp_api = YelpAPI(API_KEY)

def analyze_online_presence(name, city):
    prompt = (
        f"Research the business '{name}' in '{city}'. "
        "Does it have a Google Business Profile? "
        "Summarize its online presence in 1-2 sentences. "
        "Return a short, structured answer."
    )
    try:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.2,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"LLM error: {e}"

def get_yelp_results(city, category, pages=1):
    all_leads = []
    for page in range(pages):
        offset = page * 50  # Yelp API returns 50 results per page, so we calculate offset

        # Make the API call
        response = yelp_api.search_query(term=category, location=city, offset=offset, sort_by='rating')

        businesses = response.get('businesses', [])
        if not businesses:
            print(f"No results found on page {page + 1}.")
            continue

        # Extract relevant business details
        for biz in businesses:
            name = biz.get('name')
            yelp_url = biz.get('url')
            website = biz.get('url', None)  # Some businesses may have a website, others may not
            phone = biz.get('phone')

            # Some businesses may not have phone or website info
            if not website:
                website = None
            if not phone:
                phone = None

            # Scoring logic based on availability of website and phone number
            score = 1
            if not website:
                score += 3
            if not phone:
                score += 2

            online_presence = analyze_online_presence(name, city)

            all_leads.append({
                "Name": name,
                "Phone": phone,
                "Website": website,
                "Yelp URL": yelp_url,
                "Score": score,
                "Online Presence": online_presence
            })

        time.sleep(2)  # Be polite to Yelp API

    return all_leads

def save_to_csv(leads, filename="yelp_leads.csv"):
    if not leads:
        print("\nNo leads found. CSV not saved.")
        return

    df = pd.DataFrame(leads)

    if "Score" in df.columns:
        df.sort_values("Score", ascending=False, inplace=True)

    df.to_csv(filename, index=False)
    print(f"\n✅ Saved {len(df)} leads to {filename}")

if __name__ == "__main__":
    city = input("Enter city (e.g., Toronto): ").strip()
    category = input("Enter business category (e.g., painters): ").strip()
    pages_input = input("How many pages to scrape (1 page = ~50 results)? ").strip()

    try:
        pages = max(1, int(pages_input))
    except ValueError:
        print("Invalid input for number of pages. Defaulting to 1.")
        pages = 1

    leads = get_yelp_results(city, category, pages)
    save_to_csv(leads)
