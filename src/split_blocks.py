from enum import Enum
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
    if markdown[0] == "#":
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
            return "pre"
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
    return " ".join(text.strip().split("\n"))

def get_heading_level(text):
    current_char = text[0]
    heading_count = 0
    while current_char == '#':
        heading_count += 1
        current_char = text[heading_count]
    if heading_count >= 6:
        raise Exception("Invalid heading depth")
    return heading_count

def markdown_to_HTML_node(markdown):
    block_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        block_tag = get_tag(block_type)
        if block_type == BlockType.CODE:
            code_text_node = TextNode(text=block.strip("`"), text_type=TextType.CODE)
            child = text_node_to_html_node(code_text_node)
            block_node = ParentNode(tag=block_tag, children=[child])
        else:
            if block_type == BlockType.HEADING:
                block_tag += str(get_heading_level(block))
                block = block.strip("#")
            if block_type == BlockType.QUOTE:
                block = block.strip(">")
            inline_block = manage_split_lines(block)
            children = text_to_children(inline_block)
            block_node = ParentNode(tag=block_tag, children=children)
        block_nodes.append(block_node)

    html_node = ParentNode(tag='div', children=block_nodes)
    return html_node

if __name__ == "__main__":
    md = """
> This is a quote

##This is a heading

This is paragraph text in a p
tag here
"""
    print(markdown_to_blocks(md))
    node = markdown_to_HTML_node(md)
    print(node.to_html())

