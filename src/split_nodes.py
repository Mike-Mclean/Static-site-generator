from textnode import TextType, TextNode

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