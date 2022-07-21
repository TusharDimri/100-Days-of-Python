import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = squirrel_data["Primary Fur Color"].unique()
print(colors)
count = []
for color in colors:
    count.append(squirrel_data[squirrel_data["Primary Fur Color"] == color]["Primary Fur Color"].count())

print(count)

squirrel_dict = {
    "Colors": colors,
    "Count":count
}

squirrel_color = pd.DataFrame(squirrel_dict)
squirrel_color.to_csv("Squirrel Color Count.csv")