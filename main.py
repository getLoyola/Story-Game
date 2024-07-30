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
    for idx, loc in enumerate(locations[current_location], start=1):
        print(f"{idx}. {loc}")
    choice = input("Where would you like to go? (enter number): ")
    try:
        next_location = locations[current_location][int(choice) - 1]
        character['location'] = next_location
        print(f"You travel to {next_location}.")
        encounter(character)
    except (IndexError, ValueError):
        print("Invalid choice. You stay at the current location.")

def encounter(character):
    if character['location'] == 'Village':
        village_encounter(character)
    elif character['location'] in ['Forest', 'Lake', 'Swamp']:
        forest_encounter(character)
    elif character['location'] == 'Cave':
        cave_encounter(character)
    elif character['location'] == 'Dungeon':
        dungeon_encounter(character)
    elif character['location'] == 'Desert':
        desert_encounter(character)
    elif character['location'] == 'Castle':
        castle_encounter(character)
    elif character['location'] == 'Enchanted Forest':
        enchanted_forest_encounter(character)
    elif character['location'] == 'Mystic Pond':
        mystic_pond_encounter(character)
    elif character['location'] == 'Celestial Shrine':
        celestial_encounter(character)
    elif character['location'] == 'Astral Plane':
        astral_plane_encounter(character)
    elif character['location'] == 'Ethereal Realm':
        ethereal_realm_encounter(character)
    elif character['location'] == 'Dark Forest':
        dark_forest_encounter(character)
    elif character['location'] == 'Shadow Cave':
        shadow_cave_encounter(character)
    elif character['location'] == 'Crypt':
        crypt_encounter(character)
    elif character['location'] == 'Haunted Mansion':
        haunted_mansion_encounter(character)
    elif character['location'] == 'Forgotten Tomb':
        forgotten_tomb_encounter(character)
    elif character['location'] == 'Lost City':
        lost_city_encounter(character)
    elif character['location'] == 'Ancient Temple':
        ancient_temple_encounter(character)
    elif character['location'] == 'Sacred Grove':
        sacred_grove_encounter(character)
    elif character['location'] == 'Starlight Clearing':
        starlight_clearing_encounter(character)
    else:
        general_encounter(character)

def general_encounter(character):
    encounters = ['nothing', 'an enemy', 'a treasure', 'an NPC', 'a hidden passage', 'a magical portal']
    result = random.choice(encounters)
    if result == 'nothing':
        print("You find nothing of interest.")
    elif result == 'an enemy':
        print("You encounter an enemy!")
        combat(character)
    elif result == 'a treasure':
        print("You find a treasure!")
        treasure(character)
    elif result == 'an NPC':
        print("You meet a wandering NPC!")
        npc_interaction(character)
    elif result == 'a hidden passage':
        print("You discover a hidden passage!")
        hidden_passage(character)
    elif result == 'a magical portal':
        print("You find a magical portal!")
        magical_portal(character)

def combat(character):
    enemy_health = random.randint(20, 50)
    print(f"Enemy health: {enemy_health}")
    while enemy_health > 0 and character['health'] > 0:
        print(f"Your health: {character['health']}")
        print("1. Attack")
        print("2. Run")
        action = input("What do you want to do? (1/2): ")
        if action == '1':
            damage = random.randint(5, 20)
            enemy_health -= damage
            print(f"You deal {damage} damage to the enemy.")
            if enemy_health <= 0:
                print("You defeated the enemy!")
                character['experience'] += 50
                print(f"You gain 50 experience points. Total experience: {character['experience']}")
                return
            enemy_damage = random.randint(5, 15)
            character['health'] -= enemy_damage
            print(f"The enemy deals {enemy_damage} damage to you.")
            if character['health'] <= 0:
                print("You have been defeated.")
                return
        elif action == '2':
            print("You run away from the enemy.")
            return
        else:
            print("Invalid action. The enemy attacks!")
            enemy_damage = random.randint(5, 15)
            character['health'] -= enemy_damage
            print(f"The enemy deals {enemy_damage} damage to you.")
            if character['health'] <= 0:
                print("You have been defeated.")
                return

def treasure(character):
    treasures = ['gold', 'a magical item', 'a health potion', 'a powerful artifact', 'a rare gem']
    found = random.choice(treasures)
    print(f"You found {found}!")
    if found == 'gold':
        amount = random.randint(10, 100)
        character['inventory'].append(f"{amount} gold")
    elif found == 'a magical item':
        character['inventory'].append("magical item")
    elif found == 'a health potion':
        character['inventory'].append("health potion")
    elif found == 'a powerful artifact':
        character['inventory'].append("powerful artifact")
    elif found == 'a rare gem':
        character['inventory'].append("rare gem")

def npc_interaction(character):
    npcs = ['A wandering merchant', 'A wise old sage', 'A mysterious stranger', 'A lost child', 'An old friend']
    npc = random.choice(npcs)
    print(f"You meet {npc}.")
    if npc == 'A wandering merchant':
        print("The merchant offers you a trade.")
        trade(character)
    elif npc == 'A wise old sage':
        print("The sage offers you a quest.")
        new_quest(character)
    elif npc == 'A mysterious stranger':
        print("The stranger shares a cryptic message with you.")
    elif npc == 'A lost child':
        print("You help the child find their way home.")
        help_child(character)
    elif npc == 'An old friend':
        print("You reunite with an old friend who shares valuable information.")

def trade(character):
    items = ['a potion', 'a map', 'an enchanted ring', 'a scroll']
    print("Items for sale:")
    for idx, item in enumerate(items, start=1):
        print(f"{idx}. {item}")
    choice = input("What would you like to buy? (enter number or 0 to cancel): ")
    try:
        if int(choice) == 0:
            print("You decide not to buy anything.")
            return
        item = items[int(choice) - 1]
        if 'gold' in character['inventory']:
            print(f"You buy {item}.")
            character['inventory'].append(item)
            character['inventory'].remove('gold')
        else:
            print("You don't have enough gold.")
    except (IndexError, ValueError):
        print("Invalid choice. The merchant leaves.")
