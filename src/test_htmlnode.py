import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("a", "This is an anchor", props=props)
        expected_str = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(expected_str, node.props_to_html())

    def test_props_to_html_2(self):
        node = HTMLNode("a", "This is an anchor")
        not_expected_str = ' href="https://www.google.com" target="_blank"'
        self.assertNotEqual(not_expected_str, node.props_to_html())

    def test_props_to_html_3(self):
        node = HTMLNode("a", "This is an anchor")
        self.assertEqual("", node.props_to_html())

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = LeafNode("a", "This is an anchor", props=props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">This is an anchor</a>')

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