import random

def introduction():
    print("Welcome to the Adventure Game!")
    print("In this world, you will embark on a journey filled with challenges and mysteries.")
    name = input("Enter your character's name: ")
    character = {
        'name': name,
        'health': 100,
        'inventory': [],
        'location': 'Starting Point',
        'quests': [],
        'completed_quests': [],
        'experience': 0
    }
    return character

def main_game_loop(character):
    while character['health'] > 0:
        print(f"\n{character['name']}, you are at {character['location']}.")
        print("1. Explore")
        print("2. Check Inventory")
        print("3. Rest")
        print("4. Check Quests")
        print("5. Exit Game")
        choice = input("What would you like to do? (1/2/3/4/5): ")
        if choice == '1':
            explore(character)
        elif choice == '2':
            check_inventory(character)
        elif choice == '3':
            rest(character)
        elif choice == '4':
            check_quests(character)
        elif choice == '5':
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def explore(character):
    locations = {
        'Starting Point': ['Forest', 'Cave', 'Village'],
        'Forest': ['Starting Point', 'Lake', 'Hidden Grove'],
        'Cave': ['Starting Point', 'Dungeon'],
        'Lake': ['Forest', 'Misty Marsh'],
        'Dungeon': ['Cave', 'Abandoned Mine'],
        'Village': ['Starting Point', 'Blacksmith', 'Inn'],
        'Blacksmith': ['Village'],
        'Inn': ['Village'],
        'Hidden Grove': ['Forest', 'Ancient Ruins'],
        'Ancient Ruins': ['Hidden Grove', 'Desert'],
        'Desert': ['Ancient Ruins', 'Oasis'],
        'Oasis': ['Desert', 'Mountain'],
        'Mountain': ['Oasis', 'Castle'],
        'Castle': ['Mountain'],
        'Misty Marsh': ['Lake', 'Swamp'],
        'Swamp': ['Misty Marsh', 'Enchanted Forest'],
        'Enchanted Forest': ['Swamp', 'Magic Tower'],
        'Magic Tower': ['Enchanted Forest'],
        'Abandoned Mine': ['Dungeon'],
        'Dark Forest': ['Ancient Ruins', 'Shadow Cave'],
        'Shadow Cave': ['Dark Forest', 'Crypt'],
        'Crypt': ['Shadow Cave', 'Haunted Mansion'],
        'Haunted Mansion': ['Crypt', 'Forgotten Tomb'],
        'Forgotten Tomb': ['Haunted Mansion', 'Lost City'],
        'Lost City': ['Forgotten Tomb', 'Mystic Pond'],
        'Mystic Pond': ['Lost City', 'Ancient Temple'],
        'Ancient Temple': ['Mystic Pond', 'Sacred Grove'],
        'Sacred Grove': ['Ancient Temple', 'Celestial Shrine'],
        'Celestial Shrine': ['Sacred Grove', 'Starlight Clearing'],
        'Starlight Clearing': ['Celestial Shrine', 'Astral Plane'],
        'Astral Plane': ['Starlight Clearing', 'Ethereal Realm'],
        'Ethereal Realm': ['Astral Plane']
    }
    current_location = character['location']
    print(f"You are at {current_location}.")
    print("You can go to the following locations:")
