import unittest

from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_empty_string_input(self):
        test_input = ""
        result = text_to_textnodes(test_input)
        self.assertEqual(result, [])

    def test_solitary_markup_case(self):
        test_input = "This is a text with **bold text** and normal text afterwards."
        result = text_to_textnodes(test_input)
        self.assertEqual(result, [
            TextNode("This is a text with ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" and normal text afterwards.", TextType.TEXT)
        ]) 

    def test_multiple_code_blocks(self):
        test_input = "This is a text with `code 1` and `code 2` and normal text afterwards."
        result = text_to_textnodes(test_input)
        self.assertEqual(result, [
            TextNode("This is a text with ", TextType.TEXT),
            TextNode("code 1", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("code 2", TextType.CODE),
            TextNode(" and normal text afterwards.", TextType.TEXT)
        ]) 

    def test_complex_case(self):
        text_input = """This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"""
        result = text_to_textnodes(text_input)
        self.assertListEqual(
            result,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
