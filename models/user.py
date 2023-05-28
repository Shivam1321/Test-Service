from mongoengine import Document, StringField, EmailField, IntField, ListField , DateTimeField, EnumField
from datetime import datetime
from enum import Enum

class Type(Enum):
   SUPER_ADMIN = 'super_admin'
   ADMIN = 'admin'
   NON_ADMIN = 'non_admin'
   
class User(Document):
    email= EmailField(required=True)
    username = StringField(max_length=50)
    password = StringField(max_length=10000000)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    address = StringField(max_length=100)
    pincode = StringField(max_length=50)
    user_type = EnumField(Type , choices =[Type.SUPER_ADMIN,Type.ADMIN, Type.NON_ADMIN])
    created_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(default=datetime.now())