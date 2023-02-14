import requests
import os

DOMAIN = os.environ["m_site"]
TOKEN = os.environ["m_token"]
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


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
        send_text += i + " "
    return send_text[:-1]


def post_status(text):
    url = f"https://{DOMAIN}/api/v1/statuses"
    data = {"status": text}
    r = requests.post(url, data, headers=HEADERS)
    return r.status_code


def post_images(image_url):
    endpoint = "/api/v2/media"
    files = {
        "file": (image_url, open(image_url, "rb"), "multipart/form-type")
    }
    url = f"https://{DOMAIN}{endpoint}"
    res = requests.post(url, headers=HEADERS, files=files)
    print(res.text)
    res_json = res.json()
    image_id = res_json["id"]

    url = f"https://{DOMAIN}/api/v1/statuses"
    data = {"media_ids[]": [image_id]}
    print(url, data)
    r = requests.post(url, data, headers=HEADERS)
    print(r.status_code)

