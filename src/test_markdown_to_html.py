from split_blocks import markdown_to_HTML_node
import unittest

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here"""
        node = markdown_to_HTML_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_HTML_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>\nThis is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
##This is a heading

This is paragraph text in a p
tag here
"""
        node = markdown_to_HTML_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>This is a heading</h2><p>This is a paragraph text in a p tag here</p></div>"
        )

    def test_quote(self):
        md = """
> This is a quote

##This is a heading

This is paragraph text in a p
tag here
"""
        node = markdown_to_HTML_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote</blockquote><h2>This is a heading</h2><p>This is paragraph text in a p tag here</p></div>"
        )

if __name__ == "__main__":
    unittest.main()
