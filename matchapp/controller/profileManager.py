import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from use_case.dai import *

# example code
connection = sqlite3.connect("../database/matchapp.db")

cursor = connection.cursor()

create_user(cursor, 'Alex', 'alex@example123.com', 'Male', 'New York', 25)
