# handle db connection and use methods from dai
from database.dai import *

connection = sqlite3.connect("../database/matchapp.db")
