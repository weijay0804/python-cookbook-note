"""

    在不支援原生的比較運算的情形下排序物件

"""

from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self) -> str:
        return f"User : {self.user_id}"

    
user1 = User(1)
user2 = User(2)
user23 = User(23)
user99 = User(99)

users = [user1, user2, user23, user99]

if __name__ == "__main__":
    print(sorted(users, key= lambda user : user.user_id))
    print(sorted(users, key = attrgetter("user_id")))