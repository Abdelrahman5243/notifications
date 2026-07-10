import os
import sys
import time
import urllib.request
import urllib.parse

# ---- الإعدادات ----
INTERVAL_MINUTES = 15          # كل قد إيه يتبعت تذكير (لازم يتطابق مع الجدولة في workflow file)
START_EPOCH = 1750000000       # نقطة بداية ثابتة (متتغيرش) عشان الحساب يكون متسق

def load_list(path="list.txt"):
    with open(path, "r", encoding="utf-8") as f:
        items = [
            line.strip() for line in f
            if line.strip() and not line.strip().startswith("#")
        ]
    return items


def pick_current_item(items):
    if not items:
        return None
    now = int(time.time())
    interval_seconds = INTERVAL_MINUTES * 60
    slot = (now - START_EPOCH) // interval_seconds
    index = slot % len(items)
    return items[index]


def send_telegram_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": text
    }).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as resp:
        return resp.read()


def main():
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("خطأ: لازم تحط TELEGRAM_BOT_TOKEN و TELEGRAM_CHAT_ID كـ Secrets في GitHub.")
        sys.exit(1)

    items = load_list()
    item = pick_current_item(items)

    if item is None:
        print("القايمة فاضية، محدش هيتبعتله رسالة.")
        return

    message = f"🔔 تذكير:\n{item}"
    send_telegram_message(token, chat_id, message)
    print(f"اتبعتت الرسالة: {item}")


if __name__ == "__main__":
    main()
