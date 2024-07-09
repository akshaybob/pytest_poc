from src.user_operations import create_user, update_user, delete_user

def test_create_user():
    response=create_user(msg='user_created successfully')
    assert response['status'] == 200
    assert response ['msg'] == 'user_created successfully'

def test_failure_create_user():
    response = create_user(msg='server_error', status=500)
    assert response['status'] == 500
    assert response['msg'] == 'server_error'

def test_update_user():
    user = update_user('name', 'rohit')
    assert user['name'] == 'rohit'

def test_delete_user():
    user = delete_user()
    assert len(user) == 0
    