import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_full_eq(self):
        node = HTMLNode("Text", "Value", None, {"prop": "prop_val"})
        node2 = HTMLNode("Text", "Value", None, {"prop": "prop_val"})
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("Text", "Value", None, {"prop": "prop_val"})
        node2 = HTMLNode("Text", "Value", None, {"props": "prop_vals"})
        self.assertNotEqual(node, node2)

    def test_children_eq(self):
        children = HTMLNode("Text", "Value", None, {"prop": "prop_val"})
        children2 = HTMLNode("Text", "Value", None, {"props": "prop_vals"})
        node = HTMLNode("Text", "Value", children, {"prop": "prop_val"})
        node2 = HTMLNode("Text", "Value", children2, {"props": "prop_val"})
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, None, {'class': 'primary'})",
        )


if __name__ == "__main__":
    unittest.main()
