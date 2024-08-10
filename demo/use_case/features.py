from entity.user import User
from entity.interest import Interest
from entity.action import Action
import numpy as np

def generateID(users):
    if len(users) == 0:
        return 0
    else:
        return max([user.uid for user in users])+1
def createUser(users, name, age,gender,location):
    new_id = generateID(users)
    users.append(User(new_id, name, age, gender, location))
    return new_id
def get_user_with_id(users, uid):
    for user in users:
        if user.uid == uid:
            return user
    return -1
def print_user_profile(user):
    print(f'name: {user.name} \n')
    print(f'age: {user.age} \n')
    print(f'location: {user.location} \n')
    print(f'gender: {user.gender} \n')
def match(users, interests, actions, uid):
    matched = [action.uid2 for action in actions if action.uid1 == uid]
    user_interest = set(interest.interest for interest in interests if interest.uid == uid)  
    records = []
    for user in users:
        if user.uid not in matched and user.uid != uid:
            user_interest_other = set(interest.interest for interest in interests if interest.uid == user.uid)  
            common_interests = len(user_interest_other.intersection(user_interest))
            records.append((user.uid, common_interests))
    if not records:
        return None
    return records[np.argmax([record[1] for record in records])][0]

def get_mutual_like(users, uid, actions):
    matched = [action.uid2 for action in actions if action.uid1 == uid and action.action == 1]
    # print(matched)
    mut = []
    for target_uid in matched:

        if uid in [action.uid2 for action in actions if (action.uid1 == target_uid and action.action == 1)]:
            mut.append((target_uid, (get_user_with_id(users, target_uid).name)))

    return mut
def like_user(actions, uid1, uid2):
    actions.append(Action(uid1, uid2, 1))
def unlike_user(actions, uid1, uid2):
    actions.append(Action(uid1, uid2, 0))
def add_interest(interests, uid, interest):
    interests.append(Interest(uid, interest))