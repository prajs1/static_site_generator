from block_extractors import BlockType, block_to_block_type, markdown_to_blocks, block_to_heading, block_to_list
from htmlnode import HTMLNode
from inline_extractors import text_to_textnodes
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node


def markdown_to_html(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    main_children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.CODE:
            text = block[4:-3]
            code = text_node_to_html_node(TextNode(text=text, text_type=TextType.CODE))
            html_node = ParentNode(tag="pre", children=[code])
        elif block_type == BlockType.HEADING:
            html_node = block_to_heading(block)
        elif block_type == BlockType.UNORDERED_LIST or block_type == BlockType.ORDERED_LIST:
            html_node = block_to_list(block, block_type)
        else:
            if block_type == BlockType.QUOTE:
                split = [s[2:] for s in block.splitlines()]
                block = " ".join(split)
            children = text_to_htmlnodes(block)
            html_node = ParentNode(tag=block_type.value, children=children)
        main_children.append(html_node)
    return ParentNode(tag="div", children=main_children)


def text_to_htmlnodes(text: str) -> list[LeafNode]:
    text = text.replace("\n"," ").replace("\r"," ")
    textnodes = text_to_textnodes(text)
    children = []
    for textnode in textnodes:
        children.append(text_node_to_html_node(textnode))
    return children
