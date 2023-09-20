#!/usr/bin/python3
"""Place Module for HBNB project"""
import models
from os import getenv
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table

place_amenity = Table(
        'place_amenity', Base.metadata,
        Column(
            'place_id', String(60),
            ForeignKey('places.id'), nullable=False),
        Column(
            'amenity_id', String(60),
            ForeignKey('amenities.id'), nullable=False))


class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship(
            "Review", cascade="all, delete", backref="place")
        amenities = relationship(
                "Amenity", secondary="place_amenity", viewonly=False)
    else:
        @property
        def reviews(self):
            """getter function for reviews attribute"""
            result = []
            for rev in models.storage.all(Review).values():
                if rev.place_id == self.id:
                    result.append(rev)
            return result

        @property
        def amenities(self):
            """Getter attribute amenities that returns the list of Amenity"""
            result = []
            for amn in models.storage.all(Amenity).values():
                if amn.id in self.amenities_ids:
                    result.append(amn)
            return result

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute amenities"""
            if type(obj) == Amenity:
                self.amenities_ids.append(obj.id)
