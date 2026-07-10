# Telegram Reminder

This repository sends a Telegram reminder message from GitHub Actions.

## Files

- `.github/workflows/reminder.yml` runs the workflow and sends the message.
- `list.txt` contains one reminder item per line.

## Setup

1. Create a Telegram bot with `@BotFather`.
2. Send `/start` to your bot.
3. Get the chat id from `https://api.telegram.org/bot<TOKEN>/getUpdates`.
4. Create a GitHub repository and push these files.
5. Add these Secrets in GitHub:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`
6. Open the `Telegram Reminder` workflow in Actions and run it.

## Editing reminders

Add one item per line in `list.txt`. Lines starting with `#` are ignored.
