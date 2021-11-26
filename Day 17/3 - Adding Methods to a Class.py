# Methods are the functions of a class.

class Car:
    def __init__(self, name, seats):
        self.name = name
        self.seats = seats

    def enter_race_mode(self):
        self.seats = 1
        
car1 = Car("XYZ", 4)
print(car1.name)
print(car1.seats)
car1.enter_race_mode()
print(car1.seats)


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.id = user_id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Tushar")
user_2 = User("002", "ABC")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)