import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text ndoe", TextType.BOLD)
        node2 = TextNode("This is a text ndoe", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text ndoe", TextType.BOLD, "https://www.address.com")
        node2 = TextNode("This is a text ndoe", TextType.BOLD, "https://www.different.com")
    
        self.assertFalse(node == node2)    
    
    def test_repr(self):
        node = TextNode("Text", TextType.PLAIN, "https://address.com")

        self.assertEqual(str(node), "TextNode(Text, TextType.PLAIN, https://address.com)")

if __name__ == "__main__":
    unittest.main()