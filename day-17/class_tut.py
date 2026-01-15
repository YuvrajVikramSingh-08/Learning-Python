class User:
    def __init__(self, username, user_id):
        print("User is being created")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(user_id="001", username="Yuvraj")
user_2 = User(user_id="002", username="Vikram")

user_1.follow(user_2)
print(user_1.followers, user_2.following, user_1.following, user_2.followers)