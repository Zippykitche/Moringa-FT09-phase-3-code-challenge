from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Article:
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    magazine_id = Column(Integer, ForeignKey('magazines.id'), nullable=False)

    author = relationship('Author', back_populates='articles')
    magazine = relationship('Magazine', back_populates='articles')

    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            raise ValueError("Title cannot be changed once the article is instantiated.")
        if not isinstance(value, str):
            raise ValueError("Title must be of type str.")
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters.")
        self._title = value
    
    @property
    def author(self):
        return self.author  

    @property
    def magazine(self):
        return self.magazine  

    def __repr__(self):
        return f'<Article {self.title}, Author: {self.author.name}, Magazine: {self.magazine.name}>'
