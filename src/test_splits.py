import unittest
from split_blocks import *
from split_nodes import *
from textnode import *
from extract_from_mds import *

class TestSplits(unittest.TestCase):
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

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://www.google.com)"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINKS, "https://www.google.com")
        ]
        self.assertListEqual(nodes, expected_nodes)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_2(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [''])

    def test_block_type_heading(self):
        md = "### This is a heading"
        type = block_to_block_type(md)
        self.assertEqual(type, BlockType.HEADING)

    def test_block_type_code(self):
        md = '```this = "code block" ```'
        type = block_to_block_type(md)
        self.assertEqual(type, BlockType.CODE)

    def test_block_type_quote(self):
        md = "> This is a quote"
        type = block_to_block_type(md)
        self.assertEqual(type, BlockType.QUOTE)

    def test_block_type_unordered_list(self):
        md = """- This is an unordered list
- This is an unordered list

"""
        type = block_to_block_type(md)
        self.assertEqual(type, BlockType.UNORDERED_LIST)

    def test_block_type_ordered_list(self):
        md = """
1. This is an ordered list
2. This is an ordered list
3. This is an ordered list

"""
        type = block_to_block_type(md)
        self.assertEqual(type, BlockType.ORDERED_LIST)

    def test_block_type_paragraph(self):
        md = "This is a paragraph"
        type = block_to_block_type(md)
        self.assertEqual(type, BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()