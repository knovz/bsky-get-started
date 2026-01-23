# Not so simple post

from dotenv import load_dotenv
import os
from atproto import Client, client_utils


load_dotenv()

# bsky cred
bsky_app_pass = os.getenv("BSKY_APP_PASS")
bsky_handle = os.getenv("BSKY_HANDLE")

client = Client()
client.login(bsky_handle, bsky_app_pass)

tb = client_utils.TextBuilder()

tb.text("Hello ")
tb.mention("atproto.com", "did:plc:ewvi7nxzyoun6zhxrhs64oiz")
tb.text(" this is an example of URL sharing ")
tb.link("CBOR", "https://en.wikipedia.org/wiki/CBOR")
tb.text(". You got me to read the article!")

post = client.send_post(tb, langs=["en-US"])

print(post.uri)
print(post.cid)
