from mongoengine import Document, StringField, EmailField, IntField, ListField

class User(Document):
    email= EmailField(required=True, unique= True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    address = StringField(max_length=100)
    pincode = StringField(max_length=50)