import unittest
import os
from unittest.mock import patch
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models import storage
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = DBStorage()
        cls.db.reload()

    @classmethod
    def tearDownClass(cls):
        cls.db._session.close()


    def test_save(self):
        """Test the save() method."""
        user = User()
        user.save()
        key = f"{user.__class__.__name__}.{user.id}"
        objects = self.db.all(User)
        self.assertTrue(key in objects)

    def test_new(self):
        """Test the new() method."""
        user = User()
        self.db.new(user)
        key = f"{user.__class__.__name__}.{user.id}"
        objects = self.db.all(User)
        self.assertTrue(key in objects)

    def test_delete(self):
        """Test the delete() method."""
        user = User()
        self.db.new(user)
        self.db.save()
        self.db.delete(user)
        key = f"{user.__class__.__name__}.{user.id}"
        objects = self.db.all(User)
        self.assertTrue(key not in objects)

    def test_all(self):
        """Test the all() method."""
        user1 = User()
        user2 = User()
        self.db.new(user1)
        self.db.new(user2)
        self.db.save()
        objects = self.db.all(User)
        self.assertTrue(len(objects) == 2)

    def test_reload(self):
        """Test the reload() method."""
        user = User()
        self.db.new(user)
        self.db.save()
        self.db.reload()
        objects = self.db.all(User)
        self.assertTrue(len(objects) == 0)

    def test_save_with_state(self):
        """Test the save() method with State object."""
        state = State()
        state.save()
        key = f"{state.__class__.__name__}.{state.id}"
        objects = self.db.all(State)
        self.assertTrue(key in objects)

    def test_new_with_state(self):
        """Test the new() method with State object."""
        state = State()
        self.db.new(state)
        key = f"{state.__class__.__name__}.{state.id}"
        objects = self.db.all(State)
        self.assertTrue(key in objects)

    def test_delete_with_state(self):
        """Test the delete() method with State object."""
        state = State()
        self.db.new(state)
        self.db.save()
        self.db.delete(state)
        key = f"{state.__class__.__name__}.{state.id}"
        objects = self.db.all(State)
        self.assertTrue(key not in objects)

    def test_all_with_state(self):
        """Test the all() method with State object."""
        state1 = State()
        state2 = State()
        self.db.new(state1)
        self.db.new(state2)
        self.db.save()
        objects = self.db.all(State)
        self.assertTrue(len(objects) == 2)

    def test_reload_with_state(self):
        """Test the reload() method with State object."""
        state = State()
        self.db.new(state)
        self.db.save()
        self.db.reload()
        objects = self.db.all(State)
        self.assertTrue(len(objects) == 0)

    def test_save_with_base_model(self):
        """Test the save() method with BaseModel object."""
        base_model = BaseModel()
        base_model.save()
        key = f"{base_model.__class__.__name__}.{base_model.id}"
        objects = self.db.all(BaseModel)
        self.assertTrue(key in objects)

    def test_new_with_base_model(self):
        """Test the new() method with BaseModel object."""
        base_model = BaseModel()
        self.db.new(base_model)
        key = f"{base_model.__class__.__name__}.{base_model.id}"
        objects = self.db.all(BaseModel)
        self.assertTrue(key in objects)

    def test_delete_with_base_model(self):
        """Test the delete() method with BaseModel object."""
        base_model = BaseModel()
        self.db.new(base_model)
        self.db.save()
        self.db.delete(base_model)
        key = f"{base_model.__class__.__name__}.{base_model.id}"
        objects = self.db.all(BaseModel)
        self.assertTrue(key not in objects)

    def test_all_with_base_model(self):
        """Test the all() method with BaseModel object."""
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.db.new(base_model1)
        self.db.new(base_model2)
        self.db.save()
        objects = self.db.all(BaseModel)
        self.assertTrue(len(objects) == 2)

    def test_reload_with_base_model(self):
        """Test the reload() method with BaseModel object."""
        base_model = BaseModel()
        self.db.new(base_model)
        self.db.save()
        self.db.reload()

    def test_new2(self):
        """Test the new() method."""
        user = User()
        self.db.new(user)
        key = f"{user.__class__.__name__}.{user.id}"
        objects = self.db.all(User)
        self.assertTrue(key in objects)

    def test_delete2(self):
        """Test the delete() method."""
        user = User()
        self.db.new(user)
        self.db.save()
        self.db.delete(user)
        key = f"{user.__class__.__name__}.{user.id}"
        objects = self.db.all(User)
        self.assertTrue(key not in objects)

    def test_all2(self):
        """Test the all() method."""
        user1 = User()
        user2 = User()
        self.db.new(user1)
        self.db.new(user2)
        self.db.save()
        objects = self.db.all(User)
        self.assertTrue(len(objects) == 2)

    def test_reload2(self):
        """Test the reload() method."""
        user = User()
        self.db.new(user)
        self.db.save()
        self.db.reload()
        objects = self.db.all(User)
        self.assertTrue(len(objects) == 0)

    def test_save_with_state12(self):
        """Test the save() method with State object."""
        state = State()
        state.save()
        key = f"{state.__class__.__name__}.{state.id}"
        objects = self.db.all(State)
        self.assertTrue(key in objects)

    def test_new_with_state2(self):
        """Test the new() method with State object."""
        state = State()
        self.db.new(state)
        key = f"{state.__class__.__name__}.{state.id}"
        objects = self.db.all(State)
        self.assertTrue(key in objects)

    def test_delete_with_state2(self):
        """Test the delete() method with State object."""
        state = State()
        self.db.new(state)
        self.db.save()
        self.db.delete(state)
        key = f"{state.__class__.__name__}.{state.id}"
        objects = self.db.all(State)
        self.assertTrue(key not in objects)

    def test_all_with_state2(self):
        """Test the all() method with State object."""
        state1 = State()
        state2 = State()
        self.db.new(state1)
        self.db.new(state2)
        self.db.save()
        objects = self.db.all(State)
        self.assertTrue(len(objects) == 2)

    def test_reload_with_state2(self):
        """Test the reload() method with State object."""
        state = State()
        self.db.new(state)
        self.db.save()
        self.db.reload()
        objects = self.db.all(State)
        self.assertTrue(len(objects) == 0)
