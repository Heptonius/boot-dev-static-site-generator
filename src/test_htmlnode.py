import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node1 = HTMLNode("p", "Text in paragraph")

        self.assertEqual(str(node1), "HTMLNode(p, Text in paragraph, None, None)")

        node2 = HTMLNode("p", "Text in paragraph", None, {"href": "/categories.php", 'width': "23px"})

        self.assertEqual(str(node2), "HTMLNode(p, Text in paragraph, None, {'href': '/categories.php', 'width': '23px'})")

    def test_props_to_html(self):
        node1 = HTMLNode("p", "Text in paragraph")

        self.assertEqual(node1.props_to_html(), "")

        node2 = HTMLNode("p", "Text in paragraph", None, {"href": "/categories.php", 'width': "23px"})

        self.assertEqual(node2.props_to_html(), ' href="/categories.php" width="23px"')

        node3 = HTMLNode("p", "Text in paragraph", None, {"href": "https://google.com", "target": "_blank"})

        self.assertEqual(node3.props_to_html(), ' href="https://google.com" target="_blank"')



if __name__ == "__main__":
    unittest.main()