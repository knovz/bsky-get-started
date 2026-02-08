"""Entry point for testing the different blsky api options."""

import os
from dotenv import load_dotenv
from atproto import Client
from viewing_feeds.timeline import get_timeline, print_feed

load_dotenv()


def login() -> Client:
    """Return a blsky logged in client."""
    bsky_app_pass = os.getenv("BSKY_APP_PASS")
    bsky_handle = os.getenv("BSKY_HANDLE")

    client = Client()
    profile_view = client.login(bsky_handle, bsky_app_pass)
    print(f'Logged as "{profile_view.display_name} "(@{profile_view.handle})')
    return client


def select_option() -> str:
    """
    Print option menu and return user input

    Returns:
        str -- user input. Not validated.
    """
    menu_options = {
        1: "Home",
        2: "Next",
    }

    print("")
    for key, value in menu_options.items():
        print(f"{key}. {value}")
    print("")
    print("x. Exit")
    print("")
    choice = input("Please select\n")
    print("")
    return choice


def main() -> None:
    """Main code, returns nothing."""
    print("Running")
    client = login()
    cursor = ""
    while True:
        option = select_option()
        if option == "1":
            cursor = ""
        if option == "x":
            break
        elif option == "1" or option == "2":
            if cursor is None:
                print("There are no more items in the feed")
            else:
                timeline = get_timeline(client, cursor)
                cursor = timeline.cursor
                print_feed(timeline.feed)
                if cursor is None:
                    print("\nThere are no more items in the feed")
                else:
                    print(f"\nTiemeline retrived up to {timeline.cursor}")
        else:
            print("Please select a valid option")


if __name__ == "__main__":
    main()
