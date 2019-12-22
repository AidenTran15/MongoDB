import uuid
import datetime
from models.post import Post

class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title= title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content")
        date = input("Enter post date, or leave black for today (in format DDMMYYYY): ")
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=datetime.datetime.strptime(date, "%d%m%Y"))

    def get_posts(self):
        pass

    def save_to_mongo(self):
        pass

    def json(self):
        pass
    def get_from_mongo(self):