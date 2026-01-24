"""Entry point for testing the different blsky api options."""

import os
from dotenv import load_dotenv
from atproto import Client

load_dotenv()

def login() -> Client:
    """Return a blsky logged in client."""
    bsky_app_pass = os.getenv("BSKY_APP_PASS")
    bsky_handle = os.getenv("BSKY_HANDLE")

    client = Client()
    profile_view = client.login(bsky_handle, bsky_app_pass)
    print(f"Logged as \"{profile_view.display_name} \"(@{profile_view.handle})")
    return client


def main() -> None:
    """Main code, returns nothing."""
    print("Running")
    client = login()


if __name__ == "__main__":
    main()
