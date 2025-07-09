# CryptoAnswerBot — Telegram FAQ Bot

CryptoAnswerBot is a Telegram bot that automatically answers frequently asked questions (FAQ) about the Youmint platform. It supports both private chats and group chats, and responds using intelligent approximate matching.

## Features

- Responds to FAQ questions in private chats
- Works in groups and supergroups
- Supports English-language questions
- Sends personal answers to private messages if the question is personal
- Randomized answers for natural response variability
- FAQ is loaded from a structured faq.json file
- Clean code structure using Aiogram 3.3.0
- Logging for debugging and monitoring

## Example

- User: *Can I delete my account?*
- Bot: *(in DM)* *Yes, you can delete your account from the account settings page.*

## Project Structure
community_bot/
│
├── bot.py               # Main bot runner
├── config.py            # Bot token and config
├── faq.json             # All questions & answers
│
├── handlers/
│   └── main.py          # Command and question handlers
│
├── utils/
│   ├── faqloader.py     # Loads and validates the FAQ
│   ├── helpers.py       # Matching logic and random response selector
│
├── requirements.txt     # Python dependencies
└── README.md            # You’re reading it
## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
2. Set your bot token in config.py:
TOKEN = "YOUR_BOT_TOKEN"
3. Make sure you have a valid faq.json file with the following format:
[
  {
    "question": "Can I delete my account?",
    "answers": [
      "Yes, you can delete your account from the account settings page.",
      "Sure! Just go to your settings and delete your account from there."
    ]
  }
]
4. Run the bot:
python bot.py
Final Notes
  Ensure that the bot has permission to read messages in the group.
  For the bot to work properly in groups, it must be added as an admin (if message privacy is enabled).
  If the bot is mentioned in a group (@YourBotUsername), it will still detect questions.

Created with ❤️ by Danila for a Telegram-based crypto community.