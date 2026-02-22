import unittest

from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType

class TestSplitMarkdownLinks(unittest.TestCase):
    def test_empty_case(self):
        no_nodes = []
        result = split_nodes_link(no_nodes)
        self.assertListEqual(result, [])

    def test_pure_text_md(self):
        nodes = [
            TextNode("This is a purely text based node!", TextType.TEXT),
            TextNode("This is another very textly text node!", TextType.TEXT),
        ]
        result = split_nodes_link(nodes)
        self.assertListEqual(result, [
            TextNode("This is a purely text based node!", TextType.TEXT),
            TextNode("This is another very textly text node!", TextType.TEXT),
        ])

    def test_split_link(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png) and an ![image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.maxDiff = None
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" and an ![image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main() 