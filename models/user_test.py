from mongoengine import Document, StringField, EmailField, IntField, ListField , DateTimeField, ObjectIdField, ReferenceField
from datetime import datetime
from models.test import Test
from models.user import User


class user_test(Document):
   test_id = ReferenceField(Test)
   user_id = ReferenceField(User)
   created_at = DateTimeField(default=datetime.now())
   updated_at = DateTimeField(default=datetime.now())
   