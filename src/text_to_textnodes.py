from split_nodes_by_delimiter import split_nodes_by_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType


def text_to_textnodes(text):
    nodes = []

    if text is None or text == "":
        return nodes

    initial_text_node = TextNode(text, TextType.TEXT)

    nodes = [initial_text_node]

    nodes = split_nodes_by_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_by_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_by_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)

    return nodes
