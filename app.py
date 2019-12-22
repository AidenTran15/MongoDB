from database import Database
from models.post import Post
 
Database.initialize()

post = Blog(author="Jose",
            title="Sample title",
            description="Saple description")

blog.new_post()

blog.save_to_mongo()

Blog.from_mongo()

blog.get_posts()
