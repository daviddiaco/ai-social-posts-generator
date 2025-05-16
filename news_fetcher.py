import os
import re
import requests
from dotenv import load_dotenv
from config import MEME_KEYWORDS

load_dotenv()

CRYPTOCOMPARE_API_KEY = os.getenv("CRYPTOCOMPARE_API_KEY")

def fetch_filtered_articles(keywords):
    url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
    headers = {"Authorization": f"Apikey {CRYPTOCOMPARE_API_KEY}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("❌ Failed to fetch news:", response.status_code)
        return []

    news_data = response.json().get("Data", [])
    filtered_articles = []

    keyword_patterns = [re.compile(r'\b' + re.escape(k.lower()) + r'\b') for k in keywords]
    meme_terms = [m.lower() for m in MEME_KEYWORDS]

    for article in news_data:
        title = article.get("title", "").strip()
        body = article.get("body", "").strip()
        title_lower = title.lower()
        body_lower = body.lower()

        matches_keywords = any(p.search(title_lower) or p.search(body_lower) for p in keyword_patterns)
        mentions_meme = any(m in title_lower or m in body_lower for m in meme_terms)

        if matches_keywords and not mentions_meme:
            filtered_articles.append({
                "title": title,
                "body": body,
                "source": article.get("source", "")
            })

    return filtered_articles
