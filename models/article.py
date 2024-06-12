# models/article.py

from database.connection import get_db_connection

class Article:
    def __init__(self, title=None, content=None, author=None, magazine=None):
        self._title = title
        self._content = content
        self._author = author
        self._magazine = magazine

    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                       (self.title, self.content, self.author.id, self.magazine.id))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles')
        articles = cursor.fetchall()
        conn.close()
        return articles
