# Post with replies

from dotenv import load_dotenv
import os, time
from atproto import Client, models


load_dotenv()

# bsky cred
bsky_app_pass = os.getenv("BSKY_APP_PASS")
bsky_handle = os.getenv("BSKY_HANDLE")

client = Client()
client.login(bsky_handle, bsky_app_pass)


post = client.send_post(
    "This will be the first post of a thread, if all goes as expected.", langs=["en-US"]
)

print(post.uri)
print(post.cid)

root = models.create_strong_ref(post)

# give it a bit of time
time.sleep(5)

post2 = client.send_post(
    text="This one replies to the op.",
    langs=["en-US"],
    reply_to=models.AppBskyFeedPost.ReplyRef(parent=root, root=root),
)


parent = models.create_strong_ref(post2)

time.sleep(5)

post3 = client.send_post(
    text="This one replies to the first reply.",
    langs=["en-US"],
    reply_to=models.AppBskyFeedPost.ReplyRef(parent=parent, root=root),
)

parent = models.create_strong_ref(post3)

time.sleep(5)

post4 = client.send_post(
    text="This one replies to the reply's reply.",
    langs=["en-US"],
    reply_to=models.AppBskyFeedPost.ReplyRef(parent=parent, root=root),
)

print("done")
