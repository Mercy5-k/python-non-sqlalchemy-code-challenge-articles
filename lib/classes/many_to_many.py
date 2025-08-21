class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
     def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("name must be a non-empty string")
        self._name = name
        
        @property
        def name(self): 
            return self._name
            
            @name.setter
            def name(self, value):
                # keep name immutable
                pass
                
                def articles(self):
                    return [article for article in Article.all() if article.author == self]
                    pass
                    
                    def magazines(self):
                        return list({article.magazine for article in self.articles()})
                        pass
                        
                        def add_article(self, magazine, title):
                            return Article(self, magazine, title)
                            pass
                            
                            def topic_areas(self):
                                categories ={magazine.category for magazine in self.magazines()}
                                return list(categories) if categories else None
                                pass

class Magazine:
    all_magazines = [] # Class variable to hold all magazine instances

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all_magazines.append(self)

    # Properties for name and category
    @property
    def name(self):
        return self._name

    @name.setter
    def name (self, value):
        if isinstance(value, str) and 2 <= len(value) <=16:
            self._name = value
        # if invalid, ignore change (tests expect this behavior unless using exceptions)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str)and len(value) > 0:
            self._category = value
        # if invalid, ignore change

    # Returns all articles associated with this magazine
    def articles(self):
        return [article for article in Article.all_articles if article.magazine is self]

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
        if not Article.all_articles:
            return None
        return max(cls.all_magazines, key=lambda mag: len(mag.articles()))
        # This method returns the magazine with the most articles, or None if there are no articles
        pass