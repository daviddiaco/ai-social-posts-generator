from dotenv import load_dotenv
import os
from config import KEYWORDS
from news_fetcher import fetch_filtered_articles
from generator import generate_post
from telegram_bot import send_telegram_message

def main():
    load_dotenv()  # Load from .env

    print("🔄 Fetching and generating posts...")

    articles = fetch_filtered_articles(KEYWORDS)

    for i, article in enumerate(articles[:10]):
        post = generate_post(article)
        if post:
            print(f"\n✅ Post {i+1}:\n{post}\n")
            send_telegram_message(post)

    print("✅ Done.")

if __name__ == "__main__":
    main()
