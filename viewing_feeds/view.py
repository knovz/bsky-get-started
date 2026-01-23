# View feed

from dotenv import load_dotenv
import os
from atproto import Client

load_dotenv()

bsky_app_pass = os.getenv("BSKY_APP_PASS")
bsky_handle = os.getenv("BSKY_HANDLE")

client = Client()
client.login(bsky_handle, bsky_app_pass)

timeline = client.get_timeline(limit=5)

feed = timeline.feed
next_page = timeline.cursor

print(next_page)

print("=========")

for feed_view in feed:
    post = feed_view.post.record
    author = feed_view.post.author

    print(f"{author.display_name}: {post.text}")
