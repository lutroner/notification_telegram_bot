import argparse
import os
from time import sleep

import requests
import telegram
from dotenv import load_dotenv

DVMN_URL = "https://dvmn.org/api/long_polling/"
TIMEOUT = 92


def get_response(url, dvmn_token, params=None):
    headers = {"Authorization": f"Token {dvmn_token}"}
    response = requests.get(url, headers=headers, timeout=TIMEOUT, params=params)
    response.raise_for_status()
    return response.json()


def send_telegram_notification(response, bot_token, chat_id):
    bot = telegram.Bot(token=bot_token)
    lesson_title = response["new_attempts"][0]["lesson_title"]
    lesson_url = response["new_attempts"][0]["lesson_url"]
    if response["new_attempts"][0]["is_negative"]:
        bot.send_message(
            chat_id=chat_id,
            text=f'У вас проверили работу "{lesson_title}" - {lesson_url} '
            "К сожалению в работе нашлись ошибки.",
        )
    else:
        bot.send_message(
            chat_id=chat_id,
            text=f'У вас проверили работу "{lesson_title}" - {lesson_url} '
            "Преподавателю все понравилось, можно приступать к следующему уроку!",
        )


def main():
    load_dotenv()
    bot_token = os.environ.get("BOT_TOKEN")
    dvmn_token = os.environ.get("DEVMAN_TOKEN")
    last_timestamp = None
    notification_bot = argparse.ArgumentParser(
        description="Бот для отправки уведомлений о проверке работ на dvmn.org"
    )
    notification_bot.add_argument("--chat_id", help="chat id Telegram бота")
    chat_id = notification_bot.parse_args().chat_id
    loop_count = 0
    while True:
        if loop_count >= 10:
            sleep(loop_count * 0.5)
        params = {"timestamp": last_timestamp}
        try:
            response = get_response(DVMN_URL, dvmn_token, params)
        except requests.exceptions.ReadTimeout:
            continue
        except requests.exceptions.ConnectionError:
            loop_count += 1
            continue
        if "timestamp_to_request" in response:
            last_timestamp = response["timestamp_to_request"]
        else:
            last_timestamp = response["last_attempt_timestamp"]
            send_telegram_notification(response, bot_token, chat_id)
        loop_count = 0


if __name__ == "__main__":
    main()
