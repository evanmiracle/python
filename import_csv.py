

# import csv
import csv

with open('Z:\Python\dungeon_rooms.csv') as f:
  reader = csv.reader(f)
  your_list = [list(reader)]

print(your_list[0])
# print(reader[1])

