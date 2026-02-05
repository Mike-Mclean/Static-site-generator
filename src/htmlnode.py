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
            formatted_str += f'{attribute}="{value}" '
        return formatted_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    