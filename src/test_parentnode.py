import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, " normal text "),
                LeafNode("i", "italic text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b> normal text <i>italic text</i></p>",
        )

    def test_to_html_no_children_raises(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_empty_children_list_raises(self):
        node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_tag_raises(self):
        node = ParentNode(None, [LeafNode("span", "child")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_nested_parent_nodes(self):
        node = ParentNode(
            "div",
            [
                ParentNode("p", [LeafNode("b", "text1")]),
                ParentNode("p", [LeafNode("i", "text2")]),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<div><p><b>text1</b></p><p><i>text2</i></p></div>",
        )

    def test_to_html_deeply_nested(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section", [ParentNode("article", [LeafNode("p", "Deep nesting")])]
                )
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<div><section><article><p>Deep nesting</p></article></section></div>",
        )

    def test_to_html_mixed_leaf_and_parent_children(self):
        node = ParentNode(
            "div",
            [
                LeafNode("p", "First paragraph"),
                ParentNode(
                    "ul",
                    [
                        LeafNode("li", "Item 1"),
                        LeafNode("li", "Item 2"),
                    ],
                ),
                LeafNode("p", "Last paragraph"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<div><p>First paragraph</p><ul><li>Item 1</li><li>Item 2</li></ul><p>Last paragraph</p></div>",
        )


if __name__ == "__main__":
    unittest.main()
