from mongoengine import Document, StringField, EmailField, IntField, ListField , DateTimeField, ObjectIdField, ReferenceField
from datetime import datetime
from models.test import Test
from models.mcq import Mcq


class question_test(Document):
   mcq_id = ReferenceField(Mcq)
   test_id = ReferenceField(Test)
   marks_assigned = IntField()
   created_at = DateTimeField(default=datetime.now())
   updated_at = DateTimeField(default=datetime.now())
   