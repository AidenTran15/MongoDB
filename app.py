from database import Database
from models.menu import Menu


Database.initialize()

menu = Menu()

menu.run_menu()

