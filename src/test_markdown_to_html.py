import unittest

from markdown_to_html import markdown_to_html


class TestMarkdownToHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        expected = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(html, expected)

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```"""
        expected = "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(html, expected)

    def test_heading1(self):
        md = "# Main Title"
        expected = "<div><h1>Main Title</h1></div>"

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(html, expected)

    def test_heading2(self):
        md = "## Main Title"
        expected = "<div><h2>Main Title</h2></div>"

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(html, expected)

    def test_heading3(self):
        md = "### Main Title"
        expected = "<div><h3>Main Title</h3></div>"

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(html, expected)

    def test_heading4(self):
        md = "#### Main Title"
        expected = "<div><h4>Main Title</h4></div>"

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(html, expected)

    def test_heading5(self):
        md = "##### Main Title"
        expected = "<div><h5>Main Title</h5></div>"

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(html, expected)

    def test_heading6(self):
        md = "###### Main Title"
        expected = "<div><h6>Main Title</h6></div>"

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(html, expected)

    def test_blockquote(self):
        md = """
> This is a quote
> with **bold** and _italic_
> across multiple lines"""
        expected = '<div><blockquote>This is a quote with <b>bold</b> and <i>italic</i> across multiple lines</blockquote></div>'

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(html, expected)

    def test_unordered_list(self):
        md = """
- First unordered item with **bold**
- Second unordered item with `code`
- Third unordered item with a [link](https://boot.dev)"""
        expected = '<div><ul><li>First unordered item with <b>bold</b></li><li>Second unordered item with <code>code</code></li><li>Third unordered item with a <a href="https://boot.dev">link</a></li></ul></div>'

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(html, expected)

    def test_ordered_list(self):
        md = """
1. First ordered item
2. Second ordered item with _italic_
3. Third ordered item with **bold** and `code`"""
        expected = '<div><ol><li>First ordered item</li><li>Second ordered item with <i>italic</i></li><li>Third ordered item with <b>bold</b> and <code>code</code></li></ol></div>'

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(html, expected)
    def test_complex(self):
        md = """
# Main Title

This paragraph has **bold text**, _italic text_, `inline code`, and a [link](https://example.com).

## Section Two

> This is a quote
> with **bold** and _italic_
> across multiple lines

- First unordered item with **bold**
- Second unordered item with `code`
- Third unordered item with a [link](https://boot.dev)

1. First ordered item
2. Second ordered item with _italic_
3. Third ordered item with **bold** and `code`

### Code Section"""
        expected = '<div><h1>Main Title</h1><p>This paragraph has <b>bold text</b>, <i>italic text</i>, <code>inline code</code>, and a <a href="https://example.com">link</a>.</p><h2>Section Two</h2><blockquote>This is a quote with <b>bold</b> and <i>italic</i> across multiple lines</blockquote><ul><li>First unordered item with <b>bold</b></li><li>Second unordered item with <code>code</code></li><li>Third unordered item with a <a href="https://boot.dev">link</a></li></ul><ol><li>First ordered item</li><li>Second ordered item with <i>italic</i></li><li>Third ordered item with <b>bold</b> and <code>code</code></li></ol><h3>Code Section</h3></div>'

        self.maxDiff = None
        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(html, expected)


if __name__ == "__main__":
    unittest.main()
