#!/usr/bin/python3
"""New engine instead of fileStorage"""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """Database class represent sqlalchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """create the engine"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self._session.delete(obj)

    def all(self, cls=None):
        """query objects"""
        classes = [State, City, User, Place, Review, Amenity]
        data = []
        tables = {}
        if cls:
            data = self.__session.query(cls).all()
        else:
            for i in classes:
                data = data + self.__session.query(i).all()
        for i in data:
            key = f"{i.__class__.__name__}.{i.id}"
            tables[key] = i
        return tables

    def reload(self):
        """create session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session()

    def close(self):
        """call remove()"""
        self.__session.close()
