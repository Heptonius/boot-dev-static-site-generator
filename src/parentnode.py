from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props, value=None)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have tag")
    
        if self.children is None or len(self.children) == 0:
            raise ValueError("ParentNode must have children")
        
        children_content = "".join(list(map(lambda x: x.to_html(), self.children)))

        return f"<{self.tag}>{children_content}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"