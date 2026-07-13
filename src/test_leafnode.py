import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, wolrd!")
        self.assertEqual(node.to_html(), "<p>Hello, wolrd!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Link here!", {"href": "www.some.link"})
        self.assertEqual(node.to_html(), '<a href="www.some.link">Link here!</a>')

    def test_leaf_repr(self):
        node = LeafNode("a", "Link here!", {"href": "www.some.link"})
        self.assertEqual(
            node.__repr__(), "LeafNode(a, Link here!, {'href': 'www.some.link'})"
        )


if __name__ == "__main__":
    unittest.main()
