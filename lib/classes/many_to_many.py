class Article:
    all = []

    def __init__(self, author, magazine, title):
        # Validate author, magazine, and title
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        if not isinstance(title, str):
            raise Exception("title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("title must be between 5 and 50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title

        Article.all.append(self)

    # Properties for author, magazine, and title
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise Exception("author must be an Author instance")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        self._magazine = new_magazine
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise Exception("Author name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # name is immutable, so we do not allow changes
        pass

    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = {magazine.category for magazine in self.magazines()}
        return list(categories) if categories else None

class Magazine:
    all_magazines = []  # Class variable to hold all magazine instances

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all_magazines.append(self)

    # Properties for name and category
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Magazine name must be a string")
        if not (2 <= len(value) <= 16):
            raise Exception("Magazine name must be between 2 and 16 characters")
        self._name = value

    # Category property
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Category must be a string")
        if len(value.strip()) == 0:
            raise Exception("Category cannot be empty")
        self._category = value

    # Methods to retrieve articles, contributors, and article titles
    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        result = [author for author in set(authors) if authors.count(author) > 2]
        return result if result else None

    # Bonus
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all_magazines, key=lambda mag: len(mag.articles()))
