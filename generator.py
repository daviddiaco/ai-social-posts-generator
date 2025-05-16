import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
claude_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def truncate_text(text, max_length=700):
    return text[:max_length]

def generate_post(article):
    title = article.get("title", "")
    body = truncate_text(article.get("body", ""))

    prompt = f"""
You run the social media channel for a company startup crypto project.

Your job is to turn breaking crypto news into short, professional tweets or LinkedIn-style posts.

Here is the news article:

Title: {title}
Body: {body}

Your job is to write a short, engaging social media post about it, in a tone that matches a serious but optimistic crypto brand.

Guidelines:
- Stay under 150 characters
- Use "we" instead of "I"
- Avoid hashtags and emojis (max 1–2 if needed)
- No quotes, no hype
- Sound smart, factual, forward-looking
"""

    try:
        response = claude_client.messages.create(
            model="claude-3-7-sonnet-20250219",
            messages=[
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
            temperature=0.5,
            system="You are a crypto analyst writing social posts for an institutional audience."
        )
        return response.content[0].text.strip()

    except Exception as e:
        print(f"❌ Error generating post: {e}")
        return None
