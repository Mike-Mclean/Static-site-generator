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

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_links(self):
        node = TextNode("This is a links node", TextType.LINKS, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a links node")
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})

    def test_images(self):
        node = TextNode("This is an image node", TextType.IMAGES, "https://ca.canadapooch.com/cdn/shop/files/SuspenderBoots_Red_Side_2-min_329x.jpg?v=1761773713")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://ca.canadapooch.com/cdn/shop/files/SuspenderBoots_Red_Side_2-min_329x.jpg?v=1761773713", "alt": "This is an image node"})

if __name__ == "__main__":
    unittest.main()
