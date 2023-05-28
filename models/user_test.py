from mongoengine import Document, StringField, EmailField, IntField, ListField , DateTimeField, ObjectIdField, ReferenceField , EnumField
from datetime import datetime
from models.test import Test
from models.user import User
from enum import Enum
class Status(Enum):
   PASSED = 'passed'
   FAILED = 'failed'
   PENDING = 'pending'

class user_test(Document):
   test_id = ReferenceField(Test)
   user_id = ReferenceField(User)
   marks_obtained = IntField()
   status = EnumField(Status,choices =[Status.PASSED, Status.FAILED, Status.PENDING])
   created_at = DateTimeField(default=datetime.now())
   updated_at = DateTimeField(default=datetime.now())
   