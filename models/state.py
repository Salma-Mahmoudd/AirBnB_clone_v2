#!/usr/bin/python3
"""State Module for HBNB project"""
import models
from models.city import City
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """getter attribute that returns the list of City instances"""
            city_objs = []
            for obj in models.storage.all(City).values():
                if obj.state_id == self.id:
                    city_objs.append(obj)
            return city_objs
