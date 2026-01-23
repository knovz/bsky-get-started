# Simplest possible post

from dotenv import load_dotenv
import os
from atproto import Client

load_dotenv()

# bsky cred
bsky_app_pass = os.getenv("BSKY_APP_PASS")
bsky_handle = os.getenv("BSKY_HANDLE")

client = Client()
client.login(bsky_handle, bsky_app_pass)

post = client.send_post("Hello world! If you read this, it means I succeeded")

print(post.uri)
print(post.cid)
