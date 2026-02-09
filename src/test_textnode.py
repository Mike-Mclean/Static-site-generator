import unittest

from textnode import *

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This node has a link", TextType.LINKS, "https://www.boot.dev")
        node2 = TextNode("This node does not", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This node has a link", TextType.LINKS, "https://www.boot.dev")
        expected_repr = "TextNode(This node has a link, link, https://www.boot.dev)"
        self.assertEqual(repr(node), expected_repr)

    def test_repr_2(self):
        node = TextNode("This node has a link", TextType.LINKS, "https://www.boot.dev")
        not_expected_repr = "TextNode(This node has a link, link)"
        self.assertNotEqual(repr(node), not_expected_repr)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()
