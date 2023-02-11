import requests
import os

def print_header():
    print("Mastodon")
    print("--------")

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
        send_text +=  i + ' '
    return send_text[:-1]

def post_status(text):
    url = f"https://{os.environ['m_site']}/api/v1/statuses"
    headers = {"Authorization": f"Bearer {os.environ['m_token']}"}
    data = {"status": text}
    r = requests.post(url, data, headers=headers)
    return r.status_code
