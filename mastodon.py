import requests
import os

DOMAIN = os.environ["DOMAIN"]
TOKEN = os.environ["TOKEN"]
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def print_header():
    print("   MastodonCLI")
    print("-----------------")


def is_exit(text):
    return text == "!exit"


def is_status_post(text):
    text_list = text.split(" ")
    if len(text_list) <= 1 or text_list[0] != "!p":
        return False
    return True


def get_main_text(text):
    text_list = text.split(" ")
    send_text = ""
    for i in text_list[1:]:
        send_text += i + " "
    return send_text[:-1]


def post_status(text):
    url = f"https://{DOMAIN}/api/v1/statuses"
    data = {"status": text}
    r = requests.post(url, data, headers=HEADERS)
    return r.status_code
