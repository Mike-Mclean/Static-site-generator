from textnode import TextType, TextNode
from extract_from_mds import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if not node.text_type is TextType.TEXT:
            new_nodes.append(node)
            continue
        node_sections = node.text.split(delimiter)
        if len(node_sections) % 2 == 0:
            raise Exception("No closing delimiter in one or more parts of the markdown. Invlaid Markdown syntax")
        for index in range(len(node_sections)):
            if index % 2 == 0 and node_sections[index] != '':
                new_nodes.append(TextNode(node_sections[index], TextType.TEXT))
            elif index % 2 != 0:
                new_nodes.append(TextNode(node_sections[index], text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not node.text_type is TextType.TEXT:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        images = extract_markdown_images(remaining_text)
        for image in images:
            alt = image[0]
            url = image[1]
            before, remaining_text = remaining_text.split(f"![{alt}]({url})", 1)
            new_nodes.extend([
                TextNode(before, TextType.TEXT),
                TextNode(alt, TextType.IMAGES, url),
            ])
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not node.text_type is TextType.TEXT:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        links = extract_markdown_links(remaining_text)
        for link in links:
            alt = link[0]
            url = link[1]
            before, remaining_text = remaining_text.split(f"[{alt}]({url})", 1)
            new_nodes.extend([
                TextNode(before, TextType.TEXT),
                TextNode(alt, TextType.LINKS, url),
            ])
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    nodes_to_process = [node]
    delimiters = {"**": TextType.BOLD, "_": TextType.ITALIC, "`": TextType.CODE}
    for delimiter in delimiters:
        new_nodes = split_nodes_delimiter(nodes_to_process, delimiter, delimiters[delimiter])
        nodes_to_process = new_nodes

    new_nodes = split_nodes_image(nodes_to_process)
    nodes_to_process = new_nodes
    new_nodes = split_nodes_link(nodes_to_process)

    return new_nodes


if __name__ == "__main__":
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

    nodes = text_to_textnodes(text)

    for node in nodes:
        print(node)