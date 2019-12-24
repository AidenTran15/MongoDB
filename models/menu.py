from database import Database
from models.blog import Blog


class menu(object):
    def __init__(self):
        # Ask user for author name
        self.user = input("Enter your author name: ")
        # check if they've already got account
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt.user_for_account()
        # if not, prompt them to create one
        
    def _user_has_account(self):
        return Database.fine_one('blogs', {'author': self.user}) is not None    

    def _prompt_user_for_account(self):
        title = input("Enter your title: ")
        description = input("Enter your description")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()

    def run_menu(self):
        # Users read or write blogs?
        # if read
            # list blogs in database
            # allow user to pick one
            # displays
        # if write
            # check if user has a blog
            # if they do, prompt to write a post
            # if not, prompt to create new blog
        pass
