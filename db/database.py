class UsersDb:

    def __init__(self):
        self.users_list = []

    def add_user(self, user):
        self.users_list.append(user)

    def get_all_users(self):
        return self.users_list
 
    def find_by_username(self, username):
        for user in self.users_list:
            if user.username == username:
                return user
        return None

    def user_login(self, username, password):
        for user in self.users_list:
            if username == user.username and password == user.password:
                return user
        return None