from prettytable import PrettyTable

table = PrettyTable()  # Creating a PrettyTable object

# print(table)
# Note that table is an object of class PrettyTable


table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)

# To learn about how we got to this end result, read prettytable documentation:
# https://github.com/jazzband/prettytable

print(table.align)

table.align = 'l'  # Left Alignment
print(table)

table.align = 'r'  # Right Alignment
print(table)