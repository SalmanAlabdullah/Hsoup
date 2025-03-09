from model import Model
from sql import database
from Field import *



Model.db = database('data.sqlite')
Model.connection = Model.db.connect()



class Post(Model):
    title = Text()
    content = Char()


class Users(Model):
    username  = Text()
    email  = Char()


if __name__ == '__main__':
    post = Post()
    user = Users()
