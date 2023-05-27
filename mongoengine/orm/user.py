from mongoengine import Document, StringField, EmailField, IntField, ListField , DateTimeField
from datetime import datetime

class User(Document):
    email= EmailField(required=True)
    username = StringField(max_length=50)
    password = StringField(max_length=50)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    address = StringField(max_length=100)
    pincode = StringField(max_length=50)
    created_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(default=datetime.now())