from database import Database
from models.post import Post
 
Database.initialize()

post = Post.from_mongo('511a513064c414baa5b2fd6e0d9ffe5')
print(post)