import unittest

from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_without_tag(self):
        node = LeafNode(None, "Hello World!")
        self.assertEqual(node.to_html(), "Hello World!")
        
    def test_leaft_to_html_should_throw_for_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()