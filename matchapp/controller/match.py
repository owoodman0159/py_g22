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