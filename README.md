## Intro
Welcome to the tinder-like matchapp designed and developed by Group 22 
It is a very simple program that allows user to 
- register their information in database as an user
- login to see their profile with their unique userid that is automatically generated 
- change/delete their profile information
  -- after deletion, their information will be removed from database
- match people that based on their information
- like/unlike people that were matched
- find people they liked/unliked and people also liked them back (users that are mutually liked with the login user)

## Demo [click here to redirect]([https://github.com/Qiyiiii/py_g22/tree/main/demo]).
- very simple program with data preloaded into different lists (Users, Interests, Actions) each time when the program starts
- user will be directly loged in and can only interact with users that were preloaded
- user can match with other user based on the number of interests that are shared
- user can view users he liked/unliked
- user can view his profile
- user can view people he liked and also liked him

## matchapp [click here to redirect]([(https://github.com/Qiyiiii/py_g22/tree/main/matchapp)])
- still a very simple program but with sqllite embeded and more encapsulated design and use <b1>Flask</b1> to serve frontend content 
- users now can do whatever that is decribed in the [Intro](#introduction-1)
- can be deplyed on the website


# to work under virtual env:
source venv/bin/activate

# demo is a Low-Level Prototypes for our project
# with text based interface and pre-loaded data

# matchapp is the project that we will focus on
# with GUI and SQLlite db
# Python 3.9.12
