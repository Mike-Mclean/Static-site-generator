from enum import Enum
import re
from htmlnode import *
from split_nodes import *
from textnode import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    return markdown.strip().split("\n\n")

def is_ordered_list(markdown):
    lines = markdown.strip().split('\n')

    if not lines:
        return False

    current_line = 1
    for line in lines:
        expected_start = f"{current_line}. "
        if not line[0:3] == expected_start:
            return False
        current_line += 1
    return True

def block_to_block_type(markdown):
    match = re.findall(r"^[#]{1,6}\s+", markdown)
    if match:
        return BlockType.HEADING
    if markdown[0:3] == "```":
        return BlockType.CODE
    if markdown[0] == ">":
        return BlockType.QUOTE
    if markdown[0:2] == "- ":
        return BlockType.UNORDERED_LIST
    if is_ordered_list(markdown):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def get_tag(block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            return "p"
        case BlockType.HEADING:
            return "h"
        case BlockType.CODE:
            return ["pre", "code"]
        case BlockType.QUOTE:
            return "blockquote"
        case BlockType.UNORDERED_LIST:
            return ["li", "ul"]
        case BlockType.ORDERED_LIST:
            return ["li", "ol"]

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children

def manage_split_lines(text):
    pass

def markdown_to_HTML_node(markdown):
    block_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        block_tag = get_tag(block_type)
        children = text_to_children(block)
        block_node = ParentNode(tag=block_tag, children=children)
        block_nodes.append(block_node)

    html_node = ParentNode(tag='div', children=block_nodes)
    return html_node

if __name__ == "__main__":
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
    node = markdown_to_HTML_node(md)
    print(node.to_html())

