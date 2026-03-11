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

This is a paragraph text in a p
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


    def test_unordered_list(self):
        md = """
- This is an unordered list
- With multiple
- items that I'm
- using for testing

##This is a heading
"""
        node = markdown_to_HTML_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is an unordered list</li><li>With multiple</li><li>items that I'm</li><li>using for testing</li></ul><h2>This is a heading</h2></div>"
        )

    def test_ordered_list(self):
        md = """
1. This is an ordered list
2. With multiple
3. items that I'm
4.  using for testing

##This is a heading
"""
        node = markdown_to_HTML_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is an ordered list</li><li>With multiple</li><li>items that I'm</li><li>using for testing</li></ol><h2>This is a heading</h2></div>"
        )

if __name__ == "__main__":
    unittest.main()
