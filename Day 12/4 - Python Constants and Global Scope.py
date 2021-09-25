#  Global scope can be increadibly usefu especially when we are defining constants. Global constants are varibales which we define in the global scope and do not want to change them ever again. Conventially these are named in upper case with underscore in between if needed. This helps us in diffrentiating them as constants so that we don't change them.

# For example:- 
PI = 3.142
URL = "https://github.com"
TWITTER_HANDLE = "@tushar_dimri"

def print_constants():
    print(PI)
    print(URL)
    print(TWITTER_HANDLE)

print_constants()