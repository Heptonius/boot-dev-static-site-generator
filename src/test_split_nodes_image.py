import unittest

from split_nodes_image import split_nodes_image
from textnode import TextNode, TextType


class TestExtractMarkdownImages(unittest.TestCase):
    def test_empty_case(self):
        no_nodes = []
        result = split_nodes_image(no_nodes)
        self.assertListEqual(result, [])

    def test_pure_text_md(self):
        nodes = [
            TextNode("This is a purely text based node!", TextType.TEXT),
            TextNode("This is another very textly text node!", TextType.TEXT),
        ]
        result = split_nodes_image(nodes)
        self.assertListEqual(result, [
            TextNode("This is a purely text based node!", TextType.TEXT),
            TextNode("This is another very textly text node!", TextType.TEXT),
        ])

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main() 