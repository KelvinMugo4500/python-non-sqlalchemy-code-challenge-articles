import pytest
from classes.many_to_many import Article, Author, Magazine

class TestArticle:

    def test_article_initialization(self):
        """Article is initialized with a title."""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        assert article_1.title == "How to wear a tutu with style"

    def test_title_is_immutable_str(self):
        """title is an immutable string"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        
        with pytest.raises(AttributeError):
            article_1.title = 500
