import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        # Test author creation
        author = Author(id=1, name="John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_magazine_creation(self):
        # Test magazine creation
        magazine = Magazine(id=1, name="Tech Weekly", category="Technology")
        self.assertEqual(magazine.name, "Tech Weekly")

    def test_article_creation(self):
        # Test article creation
        author = Author( name="John Doe")
        magazine = Magazine( name="Tech Weekly", category="Technology")
        article = Article( title="Test Article", content="This is a test article.")
        self.assertEqual(article.title, "Test Article")

    def test_author_articles(self):
        # Test fetching articles associated with an author
        author = Author( name="John Doe")
        magazine = Magazine( name="Tech Weekly", category="Technology")
        article = Article( title="Test Article", content="This is a test article.")
    

    # Add more test cases for other methods as needed...

if __name__ == "__main__":
    unittest.main()
