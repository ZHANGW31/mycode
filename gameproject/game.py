import random

#Project Name: Dice-Dungeon

#Brief overview:

#This RPG game is a dungeon-crawler mixed with roguelike elements, and puzzles and character progression!



#Planned Features - (Work in progress will be denoted with (WIP), completed will be denoted (complete), planned will be denoted (planned))

# 1. Player Character Classes (complete)
# 2. Player Class choices (complete)
# 3. Player Class Attributes based on Player input (complete)
# 4. Player Class inventory (WIP)
# 5. Monster Class with attributes (complete)
# 6. Random Monster Generator Function (complete)
# 7. Item Class with complete attributes (complete)
# 8. Random Item generator function (WIP)
# 9. Random Item name generator functionality - using an external text document with over 1000 adjectives and nouns , randomly generate combinations of nouns and adjectives for
# item names, for example: a random item name can be: autonomous-striker, or diverse-phase, or distant-hemisphere etc etc...
# 10. Combat System (WIP)
    # Action Phase - Allow player to choose to use items to boost stats (planned)
    # Attack Phase - Allow player to choose from (4) different attacks unique to class (planned) , Dice roll mechanic that impacts attack damage and critical damage
    # Defense Phase - When attacked, player or monster will have a defense phase, defense dice roll to negate some damage done or avoid damage completely.
# 11. Consumable items like health potions, or temporary attack/defense/speed boosts.

#


#Classes: Mage, Assassin, Warrior, Knight
#Dice Heros
#Mage : 10 ATK, 3 DEF, 7 SPD, 20 MP (unique) , 20 HP
#Assassin : 9 ATK, 2 DEF, 9 SPD, 20 STAM (unique), 20 HP
#Warrior : 11 ATK, 4 DEF, 5 SPD, 20 RAGE (unique), 20 HP
#Knight : 9 ATK, 7 DEF, 6 SPD, 30 HP

#Item name generator from external source

#Ran once at the start of the program.
#These too lists get text data from an external text file.
name_gen_adjectives = []
name_gen_nouns = []

#read from file and store into list
with open('english-adjectives.txt') as f:
    name_gen_adjectives = [line.rstrip() for line in f]

with open('english-nouns.txt') as f:
    name_gen_nouns = [line.rstrip() for line in f]

print(name_gen_adjectives)
print(name_gen_nouns)

#Classes

#player character is based on player choice in class
class Player_Character:

    #Player inventory is a list that stores all items that player possesses.
    player_inventory = []

    player_stats = {}
    def __init__(attack, defense, health, speed, quirk_points):
        player_stats["attack"] = attack
        player_stats["defense"] = defense
        player_stats["health"] = health
        player_stats["speed"] = speed
        player_stats["quirk_points"] = quirk_points

class Monster:
    monster_stats = {}

    attack = random.randint(1,7)
    defense = random.randint(5,9)
    health = random.randint(35,100)
    speed = random.randint(3,8)


    def __init__(attack, defense, speed, health):
        monster_stats["attack"] = attack
        monster_stats["defense"] = defense
        monster_stats["health"] = health
        monster_stats["speed"] = speed

#Functions

#This function is used to generate a reward for player once they clear a room.
def room_reward():
    #player can choose to boost their max attack, defense or health.
    reward_choice = ["attack", "defense", "health"]

#This is the function that generates the random item
def random_item_gen():
    item_name =""
    attack = random.randint(1,5)
    defense = random.randint(1,5)
    health = random.randint(2,10)

    item = item_drop(item_name, attack, defense, health)

    #returns an object that can be added to the player's inventory
    return item


#Item drop class holds the unique values of the items dropped.
class item_drop():
    item_stats = {}
    def __init__(item_name, attack, defense, health):
        item_stats["attack"] = attack
        item_stats["defense"] = defense
        item_stats["health"] = health



#Core Game logic here

while True:
#Select a class

#initialize attributes to be 0 until user picks a class.
    attack = 0
    defense = 0
    health = 0
    speed = 0
    quirk_points = 0

#initialize 

#get user input, and set attributes based on class selected.

    pick_a_class = input("Please choose a class!")
        if pick_a_class.lower() == "mage":
            attack = 10
            defense = 3
            health = 20
            speed = 7
            quirk_points = 20
        elif pick_a_class.lower() == "assassin":
            attack = 9
            defense = 2
            health = 20
            speed = 9
            quirk_points = 20
        elif pick_a_class.lower() == "Warrior":
            attack = 11
            defense = 4
            health = 20
            speed = 5
            quirk_points = 20
        elif pick_a_class.lower() == "Knight":
            attack = 9
            defense = 7
            health = 30
            speed = 6
            quirk_points = 0





