from mongoengine import Document, StringField, EmailField, IntField, ListField , DateTimeField, ObjectIdField , ReferenceField
from datetime import datetime
from orm.user import User

class Test(Document):
   category = StringField(required= True)
   total_marks = StringField(required= True)
   created_by = ReferenceField(User)
   passing_marks = IntField
   total_marks = IntField
   created_at = DateTimeField(default=datetime.now())
   updated_at = DateTimeField(default=datetime.now())

   