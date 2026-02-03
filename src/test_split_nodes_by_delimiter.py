import unittest

from split_nodes_by_delimiter import (
    split_nodes_by_delimiter,
    split_text_node_by_delimiter,
)
from textnode import TextNode, TextType


class TestSplitNodesByDelimiter(unittest.TestCase):
    def test_empty_node_list(self):
        node_list = []
        nodes_after = split_nodes_by_delimiter(node_list, "`", TextType.CODE)
        self.assertEqual(nodes_after, [])

    def test_nontext_nodes(self):
        node_list = [
            TextNode("`This is code`", TextType.CODE),
            TextNode("**This is Bold text**", TextType.BOLD),
            TextNode("_This is Italic Text_", TextType.ITALIC),
        ]
        nodes_after = split_nodes_by_delimiter(node_list, "`", TextType.CODE)
        self.assertEqual(node_list, nodes_after)

    def test_text_nodes_with_delimiters(self):
        node_list = [
            TextNode("`This is code`", TextType.CODE),
            TextNode("**This is Bold text**", TextType.TEXT),
            TextNode("_This is Italic Text_", TextType.ITALIC),
            TextNode("This is a text node with `Inline code in it` and also with **bold text**", TextType.TEXT),
        ]
        nodes_after = split_nodes_by_delimiter(node_list, "`", TextType.CODE)
        self.assertEqual(nodes_after, [
            TextNode("`This is code`", TextType.CODE),
            TextNode("**This is Bold text**", TextType.TEXT),
            TextNode("_This is Italic Text_", TextType.ITALIC),
            TextNode("This is a text node with ", TextType.TEXT),
            TextNode("Inline code in it", TextType.CODE),
            TextNode(" and also with **bold text**", TextType.TEXT)
        ])

class TstSplitTextNodeByDelimiter(unittest.TestCase):
    def test_should_handle_only_text_nodes(self):
        code_node = TextNode("`This is code node` **This is bold text**", TextType.CODE)
        code_node_after = split_text_node_by_delimiter(code_node, "**", TextType.BOLD)
        self.assertEqual(code_node_after, [code_node])

    def test_node_with_bold_delimiters(self):
        node = TextNode(
            "**Bold**This is some **super** cool and interesting text", TextType.TEXT
        )
        split_by_bold = split_text_node_by_delimiter(node, "**", TextType.BOLD)
        self.assertEqual(
            split_by_bold,
            [
                TextNode("Bold", TextType.BOLD, None),
                TextNode("This is some ", TextType.TEXT, None),
                TextNode("super", TextType.BOLD, None),
                TextNode(" cool and interesting text", TextType.TEXT, None),
            ],
        )


if __name__ == "__main__":
    unittest.main()
