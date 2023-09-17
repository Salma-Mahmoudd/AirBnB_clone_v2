#!/usr/bin/python3
"""State Module for HBNB project"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """getter attribute that returns the list of City instances"""
        city_objs = []
        for obj in self.all(City):
            if obj.state_id == self.id:
                city_objs.append(obj)
        return city_objs
