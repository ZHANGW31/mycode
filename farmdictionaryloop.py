farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

#Easy

for farm in farms:
    if farm["name"] == "NE Farm":
        for animals in farm["agriculture"]:
            print(animals)

#Medium

user_input = input("Please choose a farm (NE Farm, W Farm, or SE Farm): ")

for farm in farms:
    if farm["name"] == user_input:
        for agriculture in farm["agriculture"]:
            print(agriculture)

#Hard

user_input = input("Please choose a farm from which we will return the animals from (NE Farm, W Farm, or SE Farm): ")

for farm in farms:
    if farm["name"] == user_input:
        for agriculture in farm["agriculture"]:
            if agriculture != "carrots" and agriculture != "celery":
                print(agriculture)
