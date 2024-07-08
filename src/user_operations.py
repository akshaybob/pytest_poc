"module deals with user related operations"

def create_user(msg,status=200):
    # database oprations for creating new user entry
    user = {'status': status, 'msg': msg}
    return user

def update_user(element='user_id',update_value='name'):
    user = {'user_id': 1, 'name': 'akshay', 'city':'pune'}
    user[element]=update_value
    return user
    

def delete_user():
    user = {'user_id': 1, 'name': 'akshay', 'city':'pune'}
    user.clear()
    return user
    
    
