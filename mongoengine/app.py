from mongoengine import connect
from orm.user import User
connect(db='OnlineTest')

user = User(email = 'test@gmail.com')
user.first_name = 'Shivam'
user.last_name = 'mondal'
user.save()