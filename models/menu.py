from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        # Ask user for author name
        self.user = input("Enter your author name: ")
        self.user_blog = None
        # check if they've already got account
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt.user_for_account()
        # if not, prompt them to create one
        
    def _user_has_account(self):
        blog = Database.fine_one('blogs', {'author': self.user}) 
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter your title: ")
        description = input("Enter your description")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        # Users read or write blogs?
        read_or_write = input("Do you want to Read (R) or Write (W) blogs? ")
        # if read
            # list blogs in database
            # allow user to pick one
            # displays
        if read_or_write == "R":
            self._list_blogs()
            self._view_blogs()

        # if write
            # check if user has a blog
            # if they do, prompt to write a post
            # if not, prompt to create new blog
        elif read_or_write == "W":
            pass
        else:
            print("Thank you for blogging")

    def _list_blogs(self):
        blogs = Database.find(collection='blog',
                              query={})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blogs(self):
        blog_to_see = input("Enter the ID of the blog you'd like to read")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, title: {}\n\n{}".format(post['create_date'], post['title'], post['content']))




   
        
