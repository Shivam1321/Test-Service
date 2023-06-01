from mongoengine import Document, StringField, EmailField, IntField, ListField , DateTimeField, ObjectIdField, ReferenceField , EnumField, EmbeddedDocument,EmbeddedDocumentField
from datetime import datetime
from models.test import Test
from models.user import User
from enum import Enum
class Status(Enum):
   PASSED = 'passed'
   FAILED = 'failed'
   PENDING = 'pending'

#user response ->list[string]
# google apis
class user_response(EmbeddedDocument):
   question_no = IntField()
   answer_given_index = IntField()


class user_test(Document):
   test_id = ReferenceField(Test)
   user_id = ReferenceField(User)
   answers_list = ListField(EmbeddedDocumentField(user_response))
   marks_obtained = IntField()
   status = EnumField(Status,choices =[Status.PASSED, Status.FAILED, Status.PENDING])
   created_at = DateTimeField(default=datetime.now())
   updated_at = DateTimeField(default=datetime.now())
   