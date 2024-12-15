from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///./database/magazine.db')
Base = declarative_base()

class Magazine(Base):
    __tablename__ = 'magazines'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    
    articles = relationship('Article', back_populates='magazine')

    def __init__(self, id, name, category="General"):
        self.id = id
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be of type str.")
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be of type str.")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters.")
        self._category = value

    def articles(self):
        return self.articles  

    def contributors(self):
        return [article.author for article in self.articles] 
    
    def article_titles(self):
        if not self.articles:
            return None
        return [article.title for article in self.articles]

    def contributing_authors(self):
        author_article_count = {}

        for article in self.articles:
            author = article.author
            if author in author_article_count:
                author_article_count[author] += 1
            else:
                author_article_count[author] = 1

        contributing_authors = [author for author, count in author_article_count.items() if count > 2]

        if not contributing_authors:
            return None

        return contributing_authors
    
    def __repr__(self):
        return f'Magazine {self.name}: {self.category}'
    
 

    
