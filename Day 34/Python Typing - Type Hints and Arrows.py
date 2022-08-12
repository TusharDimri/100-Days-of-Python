# age:int
# name: str
# can_drive:bool

def canDrive(age: int)->bool:
    if age >= 18:
        return True
    else:
        # return "Can't Drive"  # Wrong Data Type
        return False

print(canDrive(18))       
# canDrive("18")  # Wrong Data Type       