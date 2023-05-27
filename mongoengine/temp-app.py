from mongoengine import connect
from orm.user import User
from orm.mcq import Mcq
from orm.question_test import question_test
from orm.test import Test

connect(db='OnlineTest')

user = User(email = 'test1@gmail.com')
user.first_name = 'Shivam'
user.last_name = 'mondal'
user.save()

mcq = Mcq()
mcq.text = "What is your name?"
mcq.save()
