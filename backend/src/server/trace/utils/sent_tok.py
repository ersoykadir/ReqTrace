"""
Tokenize a document into sentences.
"""
import string
import nltk
from nltk.tokenize import sent_tokenize
from server.trace.utils.markdown_patch import unmark

# Download the sentence tokenizer model (if not already downloaded)
nltk.download("punkt")


def get_sentences(document_text):
    """
    Tokenize a document into sentences.
    """
    # I think we must put dots before any new line character
    # because sentence tokenizer does not work well with new lines
    text = unmark(document_text)

    # Add dots before new lines if not already added
    text_paragraphs = text.split("\n")
    text_paragraphs = [paragraph.strip() for paragraph in text_paragraphs]
    text_paragraphs = [paragraph for paragraph in text_paragraphs if paragraph != ""]
    # text_paragraphs = [(paragraph + ".") for paragraph in text_paragraphs]
    # print(text_paragraphs)
    text_paragraphs_dotted = []
    for paragraph in text_paragraphs:
        if paragraph[-1] not in string.punctuation:
            paragraph += "."
        text_paragraphs_dotted.append(paragraph)

    sentences = []
    for paragraph in text_paragraphs_dotted:
        sentences += sent_tokenize(paragraph)

    return sentences
