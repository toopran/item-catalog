# This file is for setting up database schema
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    air_date = Column(String(10), nullable=False)
    question = Column(String(250), nullable=False)
    value = Column(String(10))
    answer = Column(String(250), nullable=False)
    game_round = Column(String(50))
    show_number = Column(String(10), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'air_date': self.air_date,
            'question': self.question,
            'value': self.value,
            'answer': self.answer,
            'round': self.game_round,
            'show_number': self.show_number,
        }


engine = create_engine('sqlite:///itemcatalog.db')

Base.metadata.create_all(engine)
