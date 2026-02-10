import unittest
from split_nodes import *
from textnode import *
from extract_from_mds import *

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

    def test_split_nodes_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
                            TextNode("This is text with a ", TextType.TEXT),
                            TextNode("code block", TextType.CODE),
                            TextNode(" word", TextType.TEXT),
                        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_2(self):
        matches = extract_markdown_images(
            "This is text with multiple ![image](https://i.imgur.com/zjjcJKZ.png) ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
            )
        expected_result = [("image", "https://i.imgur.com/zjjcJKZ.png"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertListEqual(expected_result, matches)

    def test_extract_markdown_images_3(self):
        matches = extract_markdown_images(
            "This is text with no images"
            )
        expected_result = []
        self.assertListEqual(expected_result, matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with multiple links [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
            )
        expected_result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(matches, expected_result)

    def test_extract_markdown_links_2(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
            )
        expected_result = [("to boot dev", "https://www.boot.dev")]
        self.assertEqual(matches, expected_result)

    def test_extract_markdown_links_3(self):
        matches = extract_markdown_links(
            "This is text with no link"
            )
        expected_result = []
        self.assertEqual(matches, expected_result)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
        "This is text with a link [to google](https://www.google.com) and [to youtube](https://www.youtube.com)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to google", TextType.LINKS, "https://www.google.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINKS, "https://www.youtube.com"
                ),
            ],
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()
