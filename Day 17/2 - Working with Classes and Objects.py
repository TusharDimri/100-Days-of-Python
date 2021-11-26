class User:
    pass

user_1 = User()

# Adding Attributes to a Class in Python
user_1.id = "001"
user_1.username = "Tushar"

print(user_1.id)
print(user_1.username)

user_2 = User()
# This object will not have any attributes. The attributes created earlier were for previous object.


# Constructor:-
class Users:
    def __init__(self, name, user_id):
        # Self refers to the object that invoked the constructor.
        print("New user being created...")
        self.username = name
        self.id = user_id
        self.followers = 0

usr_1 = Users("Tushar", "001")
# usr_2 = Users() This line will generate an error.
print(usr_1.username)
print(usr_1.id)
print(usr_1.followers)