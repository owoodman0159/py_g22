
from use_case.features import *
users = []
interests = []
actions = []
createUser(users, "leo", 1 , "male", "Trt")
add_interest(interests , 0 , "game")

# Create users
user1_id = createUser(users, "Leo", 25, "male", "Toronto")
user2_id = createUser(users, "Emma", 22, "female", "Vancouver")
like_user(actions, user2_id, user1_id)
user3_id = createUser(users, "Noah", 28, "male", "Montreal")
like_user(actions, user3_id, user1_id)
user4_id = createUser(users, "Olivia", 30, "female", "Calgary")
like_user(actions, user4_id, user1_id)
user5_id = createUser(users, "Ava", 27, "female", "Ottawa")
like_user(actions, user5_id, user1_id)
user6_id = createUser(users, "Liam", 26, "male", "Toronto")
like_user(actions, user6_id, user1_id)
user7_id = createUser(users, "Sophia", 24, "female", "Halifax")
like_user(actions, user7_id, user1_id)
user8_id = createUser(users, "Ethan", 29, "male", "Edmonton")
like_user(actions, user8_id, user1_id)

# Add interests
add_interest(interests, user1_id, "gaming")
add_interest(interests, user1_id, "traveling")
add_interest(interests, user1_id, "cooking")
add_interest(interests, user1_id, "photography")

add_interest(interests, user2_id, "reading")
add_interest(interests, user2_id, "gaming")
add_interest(interests, user2_id, "traveling")
add_interest(interests, user2_id, "yoga")

add_interest(interests, user3_id, "music")
add_interest(interests, user3_id, "gaming")
add_interest(interests, user3_id, "hiking")
add_interest(interests, user3_id, "photography")

add_interest(interests, user4_id, "cooking")
add_interest(interests, user4_id, "traveling")
add_interest(interests, user4_id, "gardening")
add_interest(interests, user4_id, "reading")

add_interest(interests, user5_id, "reading")
add_interest(interests, user5_id, "music")
add_interest(interests, user5_id, "gaming")
add_interest(interests, user5_id, "yoga")

add_interest(interests, user6_id, "gaming")
add_interest(interests, user6_id, "cooking")
add_interest(interests, user6_id, "soccer")
add_interest(interests, user6_id, "movies")

add_interest(interests, user7_id, "traveling")
add_interest(interests, user7_id, "reading")
add_interest(interests, user7_id, "swimming")
add_interest(interests, user7_id, "music")

add_interest(interests, user8_id, "music")
add_interest(interests, user8_id, "cooking")
add_interest(interests, user8_id, "cycling")
add_interest(interests, user8_id, "photography")


def main():
    while True:
        print("Please type 0 if you want to find your match")
        print("Please type 1 if you want to view your liked people")
        print("Please type 2 if you want to view your unliked people")
        print("Please type 3 if you want to view your profile")
        print("Please type 4 if you want to see your mutual liked users")
        print("Please type quit if you want to quit \n")
        user_input = input(f'What do you want to do? \n')
        if user_input == "0":
            user_find = match(users, interests, actions, user1_id)
            print(f'you are matched with:\n')
            print_user_profile(get_user_with_id(users, user_find))
            target_user = get_user_with_id(users, user_find)
            target_uid = target_user.uid
            user_interest = set(interest.interest for interest in interests if interest.uid == target_uid) 
            print(f'{user_interest}' + "\n") 
            user_decision = input(f'type 0 to like, type 1 to unlike \n')
            if user_decision == "0":
                like_user(actions, user1_id, target_uid)
                print("liked")
            elif user_decision == "1":
                unlike_user(actions, user1_id, target_uid)
                print("unliked")
            else:
                print("invalid decision")
        elif user_input == "1":
            print([(action.uid2, get_user_with_id(users, action.uid2).name) for action in actions if (action.uid1 == user1_id and action.action == 1)])
            print('\n')
        elif user_input == "2":
            print([(action.uid2, get_user_with_id(users, action.uid2).name) for action in actions if (action.uid1 == user1_id and action.action == 0)])
            print('\n')
        elif user_input == "3":
            print_user_profile(get_user_with_id(users, user1_id))
            want_edit = input("\n do you want to edit it? Yes-1 / No-0 \n")
            if want_edit == "1":
                print("\n")
                new_name = input("new names: ")
                get_user_with_id(users, user1_id).name = new_name
                new_gender = input("new gender: ")
                get_user_with_id(users, user1_id).gender = new_gender
                new_age = input("new age: ")
                get_user_with_id(users, user1_id).age = new_age
                new_location = input("new location: ")
                get_user_with_id(users, user1_id).location = new_location
                print("\n new profile is: \n")
                print_user_profile(get_user_with_id(users, user1_id))
        
        elif user_input == "4":
            print("\n they also liked you:")
            print(get_mutual_like(users, user1_id, actions))
            print("\n")
        elif user_input == "quit":
            break
        else:
            print("select again \n")

if __name__ == "__main__":
    main()
