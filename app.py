from database import Database
from models.blog import Blog

 
Database.initialize()

blog = Blog(author="Jose",
            title="Sample title",
            description="Saple description")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo()

print(blog.get_posts())
