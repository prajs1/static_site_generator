from enum import Enum
from parentnode import ParentNode
from leafnode import LeafNode
from inline_extractors import text_to_textnodes
from textnode import text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "p"
    HEADING = "h"
    CODE = "code"
    QUOTE = "blockquote"
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()
        if blocks[i] == "":
            blocks.pop(i)
    return blocks


def block_to_block_type(block: str) -> BlockType:
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    splited_block = block.splitlines()
    if splited_block[0] == "```" and splited_block[-1] == "```":
        return BlockType.CODE
    counter_quote = 0
    counter_order = 0
    counter_unordered = 0
    counter_order_increment = 1
    for line in splited_block:
        if line.startswith(">"):
            counter_quote += 1
        elif line.startswith("- "):
            counter_unordered += 1
        elif line.startswith(f"{counter_order_increment}. "):
            counter_order += 1
            counter_order_increment += 1
    len_split = len(splited_block)
    if len_split == counter_quote:
        return BlockType.QUOTE
    if len_split == counter_unordered:
        return BlockType.UNORDERED_LIST
    if len_split == counter_order:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def block_to_heading(block: str) -> ParentNode:
    number = len(block.split(' ')[0])
    textnodes = text_to_textnodes(block[number+1:])
    children = []
    for textnode in textnodes:
        children.append(text_node_to_html_node(textnode))
    return ParentNode(tag=f"h{number}", children=children)


def block_to_list(block: str, block_type: BlockType) -> ParentNode:
    if block_type == BlockType.UNORDERED_LIST:
        chars_del = 2
    else:
        chars_del = 3
    split = [s[chars_del:] for s in block.splitlines()]
    lis = []
    for line in split:
        textnodes = text_to_textnodes(line)
        children = []
        for textnode in textnodes:
            children.append(text_node_to_html_node(textnode))
        lis.append(ParentNode(tag="li", children=children))
    return ParentNode(tag=block_type.value, children=lis)
    
