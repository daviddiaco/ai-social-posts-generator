# 📣 AI Social Posts Generator

An **automated tool for creating social media posts using real-time news updates as a source**.  
It’s designed to help social media managers or lean startup teams keep their feeds active and on-brand — with zero manual effort.

---

## 🧠 Why It Exists

Most small teams are too busy building, fundraising, or managing product to constantly create and publish high-quality social content.

This tool solves that by:
- Automating tweet/post generation using GPT-4
- Customizing tone of voice and hashtags to match your brand
- Delivering the content to Telegram — so it’s easy to review and edit before publishing

Bonus: By pushing content to Telegram instead of posting directly, you avoid:
- Mistakes going live without review
- Relying on expensive scheduling APIs

---

## ⚙️ What It Does

- Pulls the latest articles/posts via:
  - RSS feeds
  - Custom news sources
- Uses GPT-4 (via OpenAI API) to generate:
  - ✅ Short tweets
  - ✅ Long-form social posts (LinkedIn-style)
  - ✅ Optional hashtags
  - ✅ Branded tone of voice
- Sends all output to **Telegram** so the team can:
  - Review the posts in real time
  - Save or schedule for later
  - Use them as-is or make manual adjustments

---

## 🧰 Tech Stack

- Python
- OpenAI API (or any other LLM)
- AWS Lambda (fully serverless backend)
- Telegram Bot API

---

## 🚀 Who It’s For

- Crypto projects and DeFi startups  
- Lean Web3 teams with no in-house marketing  
- Social media managers who want AI support, not full automation  
- Builders who want to stay active on X/Twitter without thinking about it

🛠️ The version in this repo is configured for a **crypto startup** and includes prompt templates tailored to that industry.

---

## 🖼️ Example Output

