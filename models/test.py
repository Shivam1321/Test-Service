from mongoengine import Document, StringField, EmailField, IntField, ListField , DateTimeField, ObjectIdField , ReferenceField , EmbeddedDocument , EmbeddedDocumentField
from datetime import datetime
from models.user import User

class Mcq(EmbeddedDocument):
   question = StringField(max_length=100)
   category = StringField(max_length=100)
   answers = ListField(StringField(max_length=200))
   right_answer = StringField(max_length=200)
   right_answer_index = IntField(min_value=0,max_value=3)
   marks_assigned = IntField()

class Test(Document):
   # category = StringField(required= True)
   mcqs = ListField(EmbeddedDocumentField(Mcq))
   passing_marks = IntField()
   total_marks = IntField()
   created_by = ReferenceField(User)
   created_at = DateTimeField(default=datetime.now())
   updated_at = DateTimeField(default=datetime.now())