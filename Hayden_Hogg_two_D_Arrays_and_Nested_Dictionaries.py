# Hayden Hogg - 2d Arrays and Nested Dictionaries
#may 3rd, 2024

#This will show all the wepons, cosmetics and protection and what they all do
weapons = ('2. Sword damage 2', '1. Axe damage 10', '2. Crucifix damage 100')
cosmetics = ('1. Health Potion gives plus 5 health points', '2. Map gives location of everyone in the house',
             '1. Torch gives light to the whole house')
protection = ('3. jewlery Can not get hit by the monster for 10 seconds',
              '2. helmet gives extra 2 hearts', '3. Shield can fight back to the monster')
sorted_protection = sorted(protection)
sorted_cosmetics = sorted(cosmetics)
sorted_weapons = sorted(weapons)

# shows what they get for there inventory and what they have
print("Adam's Inventory:")
for item in sorted_weapons:
    print(item)
    print("Kim's Inventory:")
for item in sorted_weapons:
    print(item)

print("Berry Inventory:")
for item in sorted_weapons:
    print(item)

#This organizes and assins the name,age,sex of the characters 
people = {1: {'name': 'Adam', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Berry', 'age': '29', 'sex': 'Male'},
          3: {'name': 'Kim', 'age': '23', 'sex': 'Female'}}
#prints their name,age and sex of all three characters
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])

print(people[2]['name'])
print(people[2]['age'])
print(people[2]['sex'])

print(people[3]['name'])
print(people[3]['age'])
print(people[3]['sex'])
#This will print out all the scary locations the game is in and in order
Scary_Locations = ("1. Haunted Forest is one of the scarist places at night", "2. Ghost Ship with a bunch of skeletons is hard to fight all the time.",
                   "3. Haunted Mansion is where it all takes place and you never know when the monster will pop out")
sorted_location = sorted(Scary_Locations)

print("Scary_Locations")
for item in sorted_location:
    print(item)


