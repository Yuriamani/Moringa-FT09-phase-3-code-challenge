from database.setup import create_tables
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Create an author instance
    author = Author(name=author_name)
    author.save()  # This method should insert the author into the database

    # Create a magazine instance
    magazine = Magazine(name=magazine_name, category=magazine_category)
    magazine.save()  # This method should insert the magazine into the database

    # Create an article instance
    article = Article(title=article_title, content=article_content, author=author, magazine=magazine)
    article.save()  # This method should insert the article into the database

    # Fetch all magazines
    magazines = Magazine.get_all()
    print("\nMagazines:")
    for mag in magazines:
        print(mag)

    # Fetch all authors
    authors = Author.get_all()
    print("\nAuthors:")
    for auth in authors:
        print(auth)

    # Fetch all articles
    articles = Article.get_all()
    print("\nArticles:")
    for art in articles:
        print(art)


if __name__ == "__main__":
    main()
