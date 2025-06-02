import re
def extract_markdown_images(text):
    image_url = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image_url

def extract_markdown_links(text):
    anchor_url = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return anchor_url
