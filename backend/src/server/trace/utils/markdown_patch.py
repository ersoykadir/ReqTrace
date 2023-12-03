"""
Markdown patch to remove markdown formatting from text
"""
from markdown import Markdown
from io import StringIO


def unmark_element(element, stream=None):
    """Unmark an element and its children."""
    if stream is None:
        stream = StringIO()
    if element.text:
        stream.write(element.text)
    for sub in element:
        unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail)
    return stream.getvalue()


# patching Markdown
Markdown.output_formats["plain"] = unmark_element
__md = Markdown(output_format="plain")
__md.stripTopLevelTags = False


def unmark(text):
    """Unmark markdown text"""
    return __md.convert(text)
