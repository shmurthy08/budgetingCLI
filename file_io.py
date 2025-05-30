### Connect to Firebase api for auth and retrieving data
import hashlib
import os



def get_user(username, password=None):
    """get user from local json file"""
    user_file = f"users/{username}.json"
    if not os.path.exists(user_file):
        return None
    
    with open(user_file, 'r') as f:
        user_data = eval(f.read())  
    
    if password:
        # Hash the password using hashlib
        hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if user_data.get('password') == hash_password:
            return user_data
        else:
            return None
    return user_data


def create_user(username, password):
    """put user to local json file"""
    # Hash the password using hashlib
    os.makedirs("users", exist_ok=True)
    hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    user_data = {
        'username': username,
        'password': hash_password,
        'goals': {},
        'spending': {},
        'current_streak': 0,
        'max_streak': 0,
        'streak_phrases': [
            f"Good job {username} :D",
            f"WOOOOOOO {username}! LET'S GOOOOOOO!",
            f"Woowwwwww you are doing so well {username}!",
            f"Keep it up {username}!",
            f"Keep going {username}!",
        ],
        'streak_reset_phrases': [
            f"Don't worry {username}, you got this!",
            f"Keep trying {username}, you can do it!",
            f"Don't give up {username}!",
            f"If you did it once you can do it again {username}!",
        ]
    }
    # store user_data to local json file
    with open(f"users/{username}.json", 'w') as f:
        f.write(str(user_data))
    return user_data
    

def update_user(username, user_data):
    """update user in local json file"""
    with open(f"users/{username}.json", 'w') as f:
        f.write(str(user_data))
        
