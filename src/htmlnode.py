class HTMLNode:
    def __init__(self, tag: str = None,
                 value: str = None,
                 children: list = None,
                 props: dict = None
                 ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        formatted_str = ""
        for attribute, value in self.props.items():
            formatted_str += f' {attribute}="{value}"'
        return formatted_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag: str=None, value: str=None, props: dict=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        props = self.props_to_html()
        return f"<{self.tag}{props}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props: dict = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is not defined")
        if not self.children:
            raise ValueError("Children are not defined")
        children_str = ""
        for node in self.children:
            children_str += node.to_html()
        return f"<{self.tag}>{children_str}</{self.tag}>"
