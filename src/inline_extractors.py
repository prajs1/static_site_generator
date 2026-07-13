import re

from textnode import TextNode, TextType


def split_nodes_delimeter(
    old_nodes: list[TextNode], delimeter: str, text_type: TextType
) -> list[TextNode]:
    if delimeter == "":
        return old_nodes
    new = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new.append(node)
            continue
        deli_count = node.text.count(delimeter)
        if deli_count == 0:
            new.append(node)
            continue
        elif deli_count % 2 != 0:
            raise ValueError("Invalid Markdown syntax")
        splitted = node.text.split(delimeter)
        for i in range(len(splitted)):
            if i % 2 == 0:
                type = TextType.TEXT
            else:
                type = text_type
            new.append(TextNode(splitted[i], type))
    return new

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    return split_nodes_img_link(old_nodes, TextType.IMAGE)

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    return split_nodes_img_link(old_nodes, TextType.LINK)

def split_nodes_img_link(old_nodes: list[TextNode], text_type: TextType) -> list[TextNode]:
    extract_func = extract_wrapper(text_type)
    new = []
    for node in old_nodes:
        matches = extract_func(node.text)
        if len(matches) == 0:
            new.append(node)
            continue
        rest = node.text
        for i in range(len(matches)):
            if text_type == TextType.IMAGE:
                split_text = f"![{matches[i][0]}]({matches[i][1]})"
            elif text_type == TextType.LINK:
                split_text = f"[{matches[i][0]}]({matches[i][1]})"
            nodes = rest.split(split_text, 1)
            if nodes[0] != "":
                new.append(TextNode(nodes[0], TextType.TEXT))
            new.append(TextNode(matches[i][0], text_type, matches[i][1]))
            rest = nodes[1]
        if rest != "":
            new.append(TextNode(rest, TextType.TEXT))
    return new


def extract_wrapper(text_type: TextType) -> list[tuple[str, str]]:
    def inner_func(text: str):
        if text_type == TextType.IMAGE:
            return extract_markdown_images(text)
        if text_type == TextType.LINK:
            return extract_markdown_links(text)
    return inner_func


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [
        TextNode(text, TextType.TEXT)
    ]
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    cases = [
        ("**", TextType.BOLD),
        ("_", TextType.ITALIC),
        ("`", TextType.CODE),
    ]
    for case in cases:
        deli, ttype = case
        nodes = split_nodes_delimeter(nodes, deli, ttype)
    return nodes
