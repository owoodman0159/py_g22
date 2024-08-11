# Intro
Welcome to the **tinder-like matchapp** designed and developed by **Group 22** 
It is a very simple program that allows user to 
- register their information in database as an user
- login to see their profile with their unique userid that is automatically generated 
- change/delete their profile information
  -- after deletion, their information will be removed from database
- match people that based on their information
- like/unlike people that were matched
- find people they liked/unliked and people also liked them back (users that are mutually liked with the login user)

# demo [click here to redirect]([https://github.com/Qiyiiii/py_g22/tree/main/demo]).
- very simple program with data preloaded into different lists (Users, Interests, Actions) each time when the program starts
- user will be directly loged in and can only interact with users that were preloaded
- user can match with other user based on the number of interests that are shared
- user can view users he liked/unliked
- user can view his profile
- user can view people he liked and also liked him

# matchapp [click here to redirect]([(https://github.com/Qiyiiii/py_g22/tree/main/matchapp)])
- still a very simple program but with sqllite embeded and more encapsulated design and use **Flask** to serve frontend content 
- users now can do whatever that is decribed in the [**Intro**](#intro)
- can be deployed on the website

# archetecture:
- Three **entity class** called User, Interest, and Actions, they are stored in the database
- encapsulation:
  -- information are stored under database.db with schema.sql and some preloaded information in data.sql
  -- only dai.py (as Database Access Interface) can access database.db and do CRUD operations on it
  -- match.py and profile.py under controller directory can access functions in dai.py, and they represent two main functions that our program can do
  -- Lastly, Flask can serve frontend content and use functions from match.py as well as profile.py to do the update
  --
  

# to work under virtual env:
source venv/bin/activate

# demo is a Low-Level Prototypes for our project
# with text based interface and pre-loaded data

# matchapp is the project that we will focus on
# with GUI and SQLlite db
# Python 3.9.12
