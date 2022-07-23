l = [5, 7, 3 , 5, 4]

#  Without using List Comrehension:
l1 = []
for i in l:
    l1.append(i+1)
print(l1)

# Using List Comrehenension:
l2 = [i+1 for i in l]
print(l2)

name = "Tushar"
name_list = [letter for letter in name]
print(name_list)

range_list = [i*2 for i in range(1,5)]
print(range_list)

# Conditional List Comprehension:
even_list = [i for i in range(1, 11) if i%2==0]
print(even_list)

names = ["Kurt", "Jimmy", "Eric", "Stevie", "John", "Freddie", "Steven"]
names = [name.upper() for name in names if len(name)>=5]
print(names)