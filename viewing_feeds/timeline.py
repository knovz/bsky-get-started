"""Retrieve user feed."""

from atproto import Client
from atproto_client import models


# TODO for this to make sense it has to handle pagination!
def get_timeline(client: Client) -> models.AppBskyFeedGetTimeline.Response:
    """Returns timeline for specified client."""
    timeline = client.get_timeline(limit=5)
    print(f"Tiemeline retrived up to {timeline.cursor}")
    return timeline


def print_feed(feed: list[models.AppBskyFeedDefs.FeedViewPost]) -> None:
    """Print author and text for all posts in the feed."""
    for feed_view in feed:
        post = feed_view.post.record
        author = feed_view.post.author

        print(f"{author.display_name}: {post.text}")
    return
