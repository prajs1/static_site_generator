import unittest

from block_extractors import BlockType, block_to_block_type, markdown_to_blocks


class TestBlockExtractos(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ]
        self.assertEqual(blocks, expected)

    def test_markdown_to_blocks_empty_lines(self):
        md = """
This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line


- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ]
        self.assertEqual(blocks, expected)

    def test_block_to_block_type(self):
        cases = [
            ("This is some normal paragraph.", BlockType.PARAGRAPH),
            ("# This shoul be heading", BlockType.HEADING),
            ("### This should be heading as well", BlockType.HEADING),
            ("##### And this should be heading as well", BlockType.HEADING),
            ("- This\n- should\n- be an\n- unordered list", BlockType.UNORDERED_LIST),
            ("1. This\n2. should be\n3. ordered list", BlockType.ORDERED_LIST),
            ("1. This\n2. should not be\n4. ordered list", BlockType.PARAGRAPH),
            (">And this\n> should be\n>quote", BlockType.QUOTE),
            ("> And this\n> should be\n> quote as well", BlockType.QUOTE),
            (">And this\n>should be\n>quote as well as well", BlockType.QUOTE),
            ("- And this\n1. should be \n>a paragraph", BlockType.PARAGRAPH),
            ("```\nThis is somecode block\n```", BlockType.CODE),
            ("````\nAnd this should not be code block```", BlockType.PARAGRAPH),
            ("```And\n this should not be code block as well```", BlockType.PARAGRAPH),
            ("```\nAnd this should not be code block as well as well```", BlockType.PARAGRAPH),
        ]
        for case in cases:
            block, expected = case
            result = block_to_block_type(block)
            self.assertEqual(result, expected)
