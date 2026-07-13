import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_full_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "link")
        node2 = TextNode("This is a text node", TextType.BOLD, "link")
        self.assertEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.link.url")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_not_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.link.url")
        node2 = TextNode("This is a text node", TextType.BOLD, "link.url")
        self.assertNotEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_link(self):
        node = TextNode("This is a link node", TextType.LINK, "www.some.link")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "www.some.link"})

    def test_text_img(self):
        node = TextNode("This is an img node", TextType.IMAGE, "path/to/img")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(
            html_node.props, {"src": "path/to/img", "alt": "This is an img node"}
        )

    def test_text_type_raises(self):
        with self.assertRaises(AttributeError) as ar:
            _ = TextType.DUCK

            self.assertEqual(
                str(ar.exception), "type object 'TextType' has no attribute 'DUCK'"
            )

    def test_text_raises(self):
        node = TextNode("Should faild", "abc")
        with self.assertRaises(ValueError) as ar:
            text_node_to_html_node(node)

            self.assertEqual(str(ar.exception), "Not a known TextType value")


if __name__ == "__main__":
    unittest.main()
