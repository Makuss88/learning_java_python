class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0


user = User("0001", "gzes",)

print(user.followers)
print(user.username)
