# Hello World Initializing Function
# print("Hello World")


counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

if "El Paso" not in counties:
    print("False")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
    for value in county_dict.values():
        print(value)


for item in voting_data:
    print(f"{item['county']} county has {item['county']} registered voters.")

