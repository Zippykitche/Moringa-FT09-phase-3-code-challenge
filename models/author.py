from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship
from . import Base 

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    articles = relationship('Article', back_populates='author')

    def __init__(self, id, name):
        self.id = id
        self.name = name
    

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name_set'):  
            raise ValueError("Name cannot be changed after the author is instantiated.")
        if not isinstance(value, str):
            raise ValueError("Name must be of type str.")
        if len(value) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        
        self._name = value
        setattr(self, '_name_set', True)  

    def __repr__(self):
        return f'<Author {self.name}>'
     
    def articles(self):
        return self.articles  
    
    def magazines(self):
        return [article.magazine for article in self.articles] 
    
   
    

