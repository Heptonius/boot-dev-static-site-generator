import re


def extract_markdown_images(text): 
    markdown_image_regex = r'!\[([a-zA-Z0-9\s]+)\]\(((?:(?:http|https):\/\/[a-zA-Z0-9@:%._\\+~#?&\/\=\-]+))\)'
    return re.findall(markdown_image_regex, text)

def extract_markdown_links(text):
    markdown_link_regex = r'(?<!\!)\[([a-zA-Z0-9\s]+)\]\(((?:(?:http|https):\/\/[a-zA-Z0-9@:%._\\+~#?&\/\=\-]+))\)'
    return re.findall(markdown_link_regex, text)