import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from use_case.dataManager import *

def find_match(uid):
    """
    IMPORTANT: core algorithm of this project

    find a match for the User with (uid)

    Return:
    on success, return the uid of user that matched with the current user
    else: return -1
    """
    # TODO: HINT: check use_case/dai.py for functions needed

def like_user(uid1, uid2):
    """
    add action that User with uid1 liked the User with uid2

    Return:
    bool: True on success, False otherwise.
    """
    # TODO: HINT: use add_action(uid1, uid2, action) from use_case/dai.py

def unlike_user(uid1, uid2):
    """
    add action that User with uid1 unliked the User with uid2

    Return:
    bool: True on success, False otherwise.
    """
    # TODO: HINT: use add_action(uid1, uid2, action) from use_case/dai.py

# def get_scores(uid):
#     """
#     get scores of other users to the user with (uid)

#     Return:
#     List: list of (score and userid)
#     """
#     # TODO: 

# def get_score(uid1, uid2):
#     """
#     get scores between user with uid1 and user with uid2

#     Return:
#     int: score of two users
#     """
#     # TODO: 


# def get_top_5_user(uid):
#     """
#     return (uid, score) of top 5 users that mutually liked by user with uid

#     Return:
#     List: (uid, score) of users with top 5 scores 
#     """
#     # TODO: return the list of top 5 users
#     return []