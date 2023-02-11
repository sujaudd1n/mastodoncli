import mastodon
import sys

def main():
    mastodon.print_header()
    while True:
        text = input("> ")
        if mastodon.is_exit(text):
            sys.exit(0)
        if mastodon.is_status_post(text):
            print("Wait...")
            status_code = mastodon.post_status(mastodon.get_main_text(text))
            if status_code == 200:
                print("Success.")
            else:
                print("Error.")



if __name__ == "__main__":
    main()
