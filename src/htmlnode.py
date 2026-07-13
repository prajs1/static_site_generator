class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list[HTMLNode] | None = None,
        props: dict | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        str_props = ""
        for k, v in self.props.items():
            str_props += f' {k}="{v}"'
        return str_props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, obj):
        return (
            self.tag == obj.tag
            and self.value == obj.value
            and self.children == obj.children
            and self.props == obj.props
        )
