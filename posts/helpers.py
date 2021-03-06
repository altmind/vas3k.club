import re

from posts.models import Post


MARKDOWN_IMAGES_RE = re.compile(r"!\[*\]\((.+)\)")


def extract_some_image(post):
    if post.image and post.type != Post.TYPE_LINK:
        return post.image

    text_images = MARKDOWN_IMAGES_RE.findall(post.text)
    if text_images:
        return text_images[0]

    return None
