import csv
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(grey_squirrels_count)
print(black_squirrels_count)
print(red_squirrels_count)

data_dict = {
    "Fur Color": ["Grey", "Black", "Cinnamon"],
    "Count": [grey_squirrels_count, black_squirrels_count, red_squirrels_count]
}

ot = pandas.DataFrame(data_dict)
ot.to_csv("squirrel_count.csv")
