# Post with embeded image, post with embeded website card

from dotenv import load_dotenv
import os, time
from atproto import Client, models


load_dotenv()

# bsky cred
bsky_app_pass = os.getenv("BSKY_APP_PASS")
bsky_handle = os.getenv("BSKY_HANDLE")

client = Client()
client.login(bsky_handle, bsky_app_pass)

# post with image
with open("img/dk.jpg", "rb") as f:
    img_data = f.read()

client.send_image(
    text="Peace of mind.",
    image=img_data,
    image_alt="Mirror like lake surface with trees in the background.",
)

time.sleep(3)

# post with web card
with open("img/xkcd.png", "rb") as f:
    img_data = f.read()

thumb = client.upload_blob(img_data)

embed = models.AppBskyEmbedExternal.Main(
    external=models.AppBskyEmbedExternal.External(
        title="xkcd",
        description="A webcomic of romance, sarcasm, math, and language.",
        uri="https://xkcd.com/",
        thumb=thumb.blob,
    )
)

client.send_post(
    "If you don't know it, I highly recommend giving it a chance.", embed=embed
)
