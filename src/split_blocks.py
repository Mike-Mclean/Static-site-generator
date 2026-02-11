from enum import Enum
import re
from htmlnode import *
from split_nodes import *

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

def split_list(md_list):
    pass

def markdown_to_HTML_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        split_block = text_to_textnodes(block)
    return split_block

if __name__ == "__main__":
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
    nodes = markdown_to_HTML_node(md)
    for node in nodes:
        print(node)
