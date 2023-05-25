from mongoengine import Document, StringField, EmailField, IntField, ListField , DateTimeField, ObjectIdField
from datetime import datetime

class question_test(Document):
   question_id = ObjectIdField(required= True)
   test_id = ObjectIdField(required= True)
   marks_assigned = IntField()
   