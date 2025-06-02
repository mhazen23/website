from textnode import TextNode

class HTMLNode:
    def __init__(self, tag=None, value=None, children=(), props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
   
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        else:
            result = ""
            for key, value in self.props.items():
                result += f' {key}="{value}"'
        return result

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value,(),props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        else:
            if self.tag is None:
                return self.value
            else:
                return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("need tag")
        elif len(self.children) == 0:
            raise ValueError("need children")
        else:
            node = f'<{self.tag}{self.props_to_html()}>'
            if len(self.children) == 1:
                return f"{node}{self.children[0].to_html()}</{self.tag}>"
            else:
                for child in self.children:
                     node += child.to_html()
            return f"{node}</{self.tag}>"
                




