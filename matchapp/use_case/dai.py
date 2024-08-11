import sqlite3

# Data Access Interface

# With respect to how to set up sqllite db
# https://www.ionos.ca/digitalguide/websites/web-development/sqlite3-python/

# Profile CRUD

def create_user( cursor, name, email, gender, location, age):
    """
    Create a new user and Insert into database 

    Return: uid of the created user
    """

    # Perform Insert to the table
    cursor.execute('''
        INSERT INTO User (name, email, gender, location, age)
        VALUES (?, ?, ?, ?, ?)
        ''', (name, email, gender, location, age))
    
    # Save change
    cursor.connection.commit()

    # Get id of the new user
    user_id = cursor.lastrowid
    
    print(f"User {name} added successfully with ID {user_id}. ")

def get_user_info(cursor, uid):
    """
    Get the profile information of the User with (uid) from the database

    Returns: Tuple(name, email, gender, location, age)
    """
    # TODO: 
    pass

def remove_user_with_id(cursor, uid):
    """
    Delete an existing user and remove from  into database 

    Return:
    when removed successfully, return True
    else False
    """
    # TODO: 
    pass

def update_user_gender(curosr, uid, new_gender):
    """
    Change User with the specific uid (uid) to have a new gender (new_gender)

    Return:
    when removed successfully, return True
    else False
    """
    # TODO: 
    pass

def update_user_age(curosr, uid, new_age):
    """
    Change User with the specific uid(uid) to have a new age (new_age)

    Return:
    when removed successfully, return True
    else False
    """
    # TODO: 
    pass


def update_user_location(curosr, uid, new_location):
    """
    Change User with the specific uid(uid) to have a new location (new_location)

    Return:
    when removed successfully, return True
    else False
    """
    # TODO: 
    pass

def update_user_name(curosr, uid, new_name):
    """
    Change User with the specific uid(uid) to have a new name (new_name)

    Return:
    when removed successfully, return True
    else False
    """
    # TODO: 
    pass


# Action CRUD

def add_action(cursor, uid1, uid2, action):
    """
    add a specific user interaction from user with (uid1) to user with (uid2) 
    to boolean action True -> like
    or False -> unlike

    Return:
    when removed successfully, return True
    else False
    """
    # TODO: 
    pass
def change_action(cursor, uid1, uid2, action):
    """
    change a specific user interaction from user with (uid1) to user with (uid2)
    to boolean action True -> like
    or False -> unlike

    Return:
    when removed successfully, return True
    else False
    """
    # TODO: 
    pass

def get_user_action(cursor, uid):
    """
    Find all actions from that user to other people

    Return:
    List of actions that from User with (uid) 
    """
    # TODO:
    pass

def get_user_likes(cursor, uid):
    """
    Find all Users that the User with (uid) liked
    hint: use get_user_action(cursor, uid) 

    Return:
    List of Users that the  User with (uid) liked
    """
    # TODO:
    pass

def get_user_unlikes(cursor, uid):
    """
    Find all Users that the User with (uid) unliked
    hint: use get_user_action(cursor, uid) 

    Return:
    List of Users that the  User with (uid) unliked
    """
    # TODO:
    pass


# Interest CRUD
def add_interest(curosr, uid, interest):
    """
    add interest (interest) to User with (uid) 
    """
    # TODO: 
    pass

def remove_interest(curosr, uid, interest):
    """
    remove interest (interest) to User with (uid) 
    """
    # TODO: 
    pass

# # example code
# connection = sqlite3.connect("../database/matchapp.db")

# cursor = connection.cursor()

# create_user(cursor, 'Alex', 'alex@example.com', 'Male', 'New York', 25)

