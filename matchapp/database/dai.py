import sqlite3

# Data Access Interface

# With respect to how to set up sqllite db
# https://www.ionos.ca/digitalguide/websites/web-development/sqlite3-python/

# Profile CRUD

def create_user( cursor, name, email, gender, location, age):
    """
    Create a new user and Insert into database 
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

def remove_user_with_id(cursor, id):
    """
    Delete an existing user and remove from  into database 
    """
    # TODO: 
    pass

def update_user_gender(curosr, id, new_gender):
    """
    Change User with the specific uid (id) to have a new gender (new_gender)
    """
    # TODO: 
    pass

def update_user_age(curosr, id, new_age):
    """
    Change User with the specific uid(id) to have a new age (new_age)
    """
    # TODO: 
    pass


def update_user_location(curosr, id, new_location):
    """
    Change User with the specific uid(id) to have a new location (new_location)
    """
    # TODO: 
    pass

def update_user_name(curosr, id, new_name):
    """
    Change User with the specific uid(id) to have a new name (new_name)
    """
    # TODO: 
    pass


# Action CRUD

def add_action(cursor, uid1, uid2, action):
    """
    add a specific user interaction from user with (uid1) to user with (uid2) 
    to boolean action True -> like
    or False -> unlike
    """
    # TODO: 
    pass
def change_action(cursor, uid1, uid2, action):
    """
    change a specific user interaction from user with (uid1) to user with (uid2)
    to boolean action True -> like
    or False -> unlike
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

connection = sqlite3.connect("matchapp.db")
connection.commit()
cursor = connection.cursor()

create_user(cursor, 'Alex', 'alex@example.com', 'Male', 'New York', 25)
# remove_user_with_id( cursor , 1)
