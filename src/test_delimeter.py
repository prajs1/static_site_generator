import unittest

from inline_extractors import split_nodes_delimeter
from textnode import TextNode, TextType


class TestSplitDelimeter(unittest.TestCase):
    def test_text_no_deli(self):
        nodes = [
            TextNode("abc", TextType.TEXT),
            TextNode("cba", TextType.TEXT),
            TextNode("dsa", TextType.TEXT),
            TextNode("asd", TextType.TEXT),
        ]
        new = split_nodes_delimeter(nodes, "", TextType.TEXT)
        self.assertEqual(nodes, new)

    def test_text_deli_not_present(self):
        nodes = [
            TextNode("abc", TextType.TEXT),
            TextNode("cba", TextType.TEXT),
            TextNode("dsa", TextType.TEXT),
            TextNode("asd", TextType.TEXT),
        ]
        new = split_nodes_delimeter(nodes, "_", TextType.TEXT)
        self.assertEqual(nodes, new)

    def test_text_deli_exception(self):
        nodes = [
            TextNode("abc", TextType.TEXT),
            TextNode("cba", TextType.TEXT),
            TextNode("_dsa", TextType.TEXT),
            TextNode("asd", TextType.TEXT),
        ]

        with self.assertRaises(ValueError) as ar:
            new = split_nodes_delimeter(nodes, "_", TextType.ITALIC)
            self.assertEqual(ar.exception, "Invalid Markdown syntax")

    def test_italic(self):
        cases = [
            ("_", "italic", TextType.ITALIC),
            ("**", "bold", TextType.BOLD),
            ("`", "code", TextType.CODE),
        ]
        for case in cases:
            deli, text, text_type = case
            nodes = [
                TextNode(
                    f"This text have an {deli}{text}{deli} inside it", TextType.TEXT
                )
            ]
            expected = [
                TextNode("This text have an ", TextType.TEXT),
                TextNode(text, text_type),
                TextNode(" inside it", TextType.TEXT),
            ]
            new_nodes = split_nodes_delimeter(nodes, deli, text_type)
            self.assertEqual(new_nodes, expected)

    def test_italic_multi(self):
        cases = [
            ("_", "italic", TextType.ITALIC),
            ("**", "bold", TextType.BOLD),
            ("`", "code", TextType.CODE),
        ]
        for case in cases:
            deli, text, text_type = case
            nodes = [
                TextNode(
                    f"This text have an {deli}{text}{deli} inside it, and there {deli}it is as well{deli} as well",
                    TextType.TEXT,
                )
            ]
            expected = [
                TextNode("This text have an ", TextType.TEXT),
                TextNode(text, text_type),
                TextNode(" inside it, and there ", TextType.TEXT),
                TextNode("it is as well", text_type),
                TextNode(" as well", TextType.TEXT),
            ]
            new_nodes = split_nodes_delimeter(nodes, deli, text_type)
            self.assertEqual(new_nodes, expected)


if __name__ == "__main__":
    unittest.main()
