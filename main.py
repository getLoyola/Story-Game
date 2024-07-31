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

def new_quest(character):
    quests = ['Find the lost artifact', 'Rescue the village elder', 'Collect rare herbs', 'Defeat the dark wizard', 'Explore the ancient ruins']
    quest = random.choice(quests)
    print(f"You have accepted a new quest: {quest}")
    character['quests'].append(quest)

def help_child(character):
    print("You help the child find their way home.")
    print("The child's parents reward you with some gold.")
    character['inventory'].append("gold")

def hidden_passage(character):
    passages = ['a secret cave', 'an old library', 'a hidden vault', 'a mystical chamber']
    passage = random.choice(passages)
    print(f"You find {passage}!")
    if passage == 'a secret cave':
        print("The cave is dark and damp.")
        treasure(character)
    elif passage == 'an old library':
        print("The library contains ancient books.")
        print("You find a book of spells.")
        character['inventory'].append("book of spells")
    elif passage == 'a hidden vault':
        print("The vault is filled with old treasures.")
        treasure(character)
    elif passage == 'a mystical chamber':
        print("The chamber is filled with glowing crystals.")
        print("You gain insight and some experience.")
        character['experience'] += 30
        print(f"You gain 30 experience points. Total experience: {character['experience']}")

def magical_portal(character):
    portals = ['a realm of fire', 'a frozen wasteland', 'an underwater city', 'a celestial haven']
    portal = random.choice(portals)
    print(f"You step through the portal and find yourself in {portal}.")
    if portal == 'a realm of fire':
        print("You encounter fire elementals!")
        combat(character)
    elif portal == 'a frozen wasteland':
        print("You find a frozen treasure chest.")
        treasure(character)
    elif portal == 'an underwater city':
        print("You find ancient relics.")
        character['inventory'].append("ancient relic")
    elif portal == 'a celestial haven':
        print("You are blessed with celestial guidance.")
        character['experience'] += 100
        print(f"You gain 100 experience points. Total experience: {character['experience']}")

def blacksmith(character):
    print("You enter the blacksmith's shop.")
    print("The blacksmith offers to upgrade your weapon for a price.")
    if "gold" in character['inventory']:
        print("1. Upgrade weapon (10 gold)")
        print("2. Leave")
        choice = input("What would you like to do? (1/2): ")
        if choice == '1':
            if any(item in character['inventory'] for item in ['sword', 'shield']):
                character['inventory'].remove("gold")
                print("Your weapon has been upgraded!")
            else:
                print("You don't have the required items to upgrade.")
        elif choice == '2':
            print("You leave the blacksmith's shop.")
        else:
            print("Invalid choice. You leave the blacksmith's shop.")
    else:
        print("You don't have any gold to upgrade your weapon.")

def inn(character):
    print("You enter the inn.")
    print("The innkeeper offers you a room for the night.")
    if "gold" in character['inventory']:
        print("1. Stay the night (5 gold)")
        print("2. Leave")
        choice = input("What would you like to do? (1/2): ")
        if choice == '1':
            character['inventory'].remove("gold")
            print("You stay the night and regain full health.")
            character['health'] = 100
        elif choice == '2':
            print("You leave the inn.")
        else:
            print("Invalid choice. You leave the inn.")
    else:
        print("You don't have any gold to stay the night.")

def check_inventory(character):
    print("Inventory:")
    for item in character['inventory']:
        print(f"- {item}")
    if not character['inventory']:
        print("Your inventory is empty.")

def rest(character):
    print(f"{character['name']} rests and regains some health.")
    character['health'] = min(100, character['health'] + 10)
    print(f"Current health: {character['health']}")

def check_quests(character):
    print("Active Quests:")
    for quest in character['quests']:
        print(f"- {quest}")
    if not character['quests']:
        print("You have no active quests.")
    print("Completed Quests:")
    for quest in character['completed_quests']:
        print(f"- {quest}")
    if not character['completed_quests']:
        print("You have no completed quests.")

def quest_complete(character, quest):
    if quest in character['quests']:
        character['quests'].remove(quest)
        character['completed_quests'].append(quest)
        print(f"Quest '{quest}' completed!")
    else:
        print("You have not accepted this quest.")

def level_up(character):
    experience_needed = 100
    if character['experience'] >= experience_needed:
        character['experience'] -= experience_needed
        print("Congratulations! You've leveled up!")

def dark_forest_encounter(character):
    print("You enter the Dark Forest.")
    print("1. Seek out the guardian")
    print("2. Search for hidden paths")
    choice = input("What would you like to do? (1/2): ")
    if choice == '1':
        print("You find the forest guardian.")
        print("The guardian offers to train you.")
        character['experience'] += 50
        print(f"You gain 50 experience points. Total experience: {character['experience']}")
    elif choice == '2':
        print("You find a hidden path leading to an ancient altar.")
        character['inventory'].append("ancient artifact")
    else:
        print("Invalid choice. You leave the Dark Forest.")

def shadow_cave_encounter(character):
    print("You enter the Shadow Cave.")
    print("1. Investigate the shadows")
    print("2. Search for treasure")
    choice = input("What would you like to do? (1/2): ")
    if choice == '1':
        print("You encounter shadowy figures.")
        print("They attack you!")
        combat(character)
    elif choice == '2':
        print("You find a treasure chest hidden in the cave.")
        treasure(character)
    else:
        print("Invalid choice. You leave the Shadow Cave.")

def crypt_encounter(character):
    print("You enter the Crypt.")
    print("1. Explore the tombs")
    print("2. Search for artifacts")
    choice = input("What would you like to do? (1/2): ")
    if choice == '1':
        print("You find an old scroll.")
        character['inventory'].append("ancient scroll")
    elif choice == '2':
        print("You discover a hidden relic.")
        character['inventory'].append("relic")
    else:
        print("Invalid choice. You leave the Crypt.")

def haunted_mansion_encounter(character):
    print("You enter the Haunted Mansion.")
    print("1. Investigate the ghostly presence")
    print("2. Search for hidden passages")
    choice = input("What would you like to do? (1/2): ")
    if choice == '1':
        print("You encounter a ghost!")
        combat(character)
    elif choice == '2':
        print("You find a hidden passage leading to a secret room.")
        treasure(character)
    else:
        print("Invalid choice. You leave the Haunted Mansion.")

def forgotten_tomb_encounter(character):
    print("You enter the Forgotten Tomb.")
    print("1. Examine the sarcophagi")
    print("2. Search for hidden traps")
    choice = input("What would you like to do? (1/2): ")
    if choice == '1':
        print("You find a hidden compartment with a valuable artifact.")
        character['inventory'].append("valuable artifact")
    elif choice == '2':
        print("You avoid traps and find an old map.")
        character['inventory'].append("old map")
    else:
        print("Invalid choice. You leave the Forgotten Tomb.")

def lost_city_encounter(character):
    print("You arrive at the Lost City.")
    print("1. Explore the ruins")
    print("2. Search for clues")
    choice = input("What would you like to do? (1/2): ")
    if choice == '1':
        print("You find a hidden chamber with treasures.")
        treasure(character)
    elif choice == '2':
        print("You discover ancient writings.")
        character['inventory'].append("ancient writings")
    else:
        print("Invalid choice. You leave the Lost City.")

def ancient_temple_encounter(character):
    print("You enter the Ancient Temple.")
    print("1. Offer a sacrifice")
    print("2. Search for relics")
    choice = input("What would you like to do? (1/2): ")
    if choice == '1':
        print("You make an offering and gain some blessings.")
        character['experience'] += 20
        print(f"You gain 20 experience points. Total experience: {character['experience']}")
    elif choice == '2':
        print("You find an ancient relic.")
        character['inventory'].append("ancient relic")
    else:
        print("Invalid choice. You leave the Ancient Temple.")

def sacred_grove_encounter(character):
    print("You enter the Sacred Grove.")
    print("1. Commune with nature")
    print("2. Explore the grove")
    choice = input("What would you like to do? (1/2): ")
    if choice == '1':
        print("You gain wisdom and some experience.")
        character['experience'] += 30
        print(f"You gain 30 experience points. Total experience: {character['experience']}")
    elif choice == '2':
        print("You find a hidden glade.")
        character['inventory'].append("mystical herb")
    else:
        print("Invalid choice. You leave the Sacred Grove.")

def starlight_clearing_encounter(character):
    print("You reach the Starlight Clearing.")
    print("1. Stare at the stars")
    print("2. Look for hidden secrets")
    choice = input("What would you like to do? (1/2): ")
    if choice == '1':
        print("You gain insight from the stars.")
        character['experience'] += 50
        print(f"You gain 50 experience points. Total experience: {character['experience']}")
    elif choice == '2':
        print("You find a celestial artifact.")
        character['inventory'].append("celestial artifact")
    else:
        print("Invalid choice. You leave the Starlight Clearing.")
def mystical_market(character):
    """
    This function represents a visit to a mystical market where the player can buy and sell magical items.
    """
    print("You enter the mystical market. It is bustling with magical items and mysterious vendors.")
    market_items = {
        'potion of healing': 20,
        'elixir of strength': 50,
        'scroll of wisdom': 40,
        'enchanted ring': 100,
        'magic wand': 150
    }
    print("Items available for purchase:")
    for idx, (item, price) in enumerate(market_items.items(), start=1):
        print(f"{idx}. {item} - {price} gold")
    
    print("1. Buy an item")
    print("2. Sell an item")
    print("3. Leave the market")
    choice = input("What would you like to do? (1/2/3): ")

    if choice == '1':
        buy_item(character, market_items)
    elif choice == '2':
        sell_item(character)
    elif choice == '3':
        print("You decide to leave the mystical market.")
    else:
        print("Invalid choice. You leave the market.")

def buy_item(character, market_items):
    print("Which item would you like to buy? (Enter number)")
    choice = input()
    try:
        item = list(market_items.keys())[int(choice) - 1]
        price = market_items[item]
        if "gold" in character['inventory']:
            gold_amount = int(character['inventory'][character['inventory'].index('gold')].split()[0])
            if gold_amount >= price:
                character['inventory'].remove('gold')
                character['inventory'].append(item)
                print(f"You bought {item} for {price} gold.")
            else:
                print("You don't have enough gold.")
        else:
            print("You don't have any gold.")
    except (IndexError, ValueError):
        print("Invalid choice. You leave the market.")

def sell_item(character):
    if not character['inventory']:
        print("You have nothing to sell.")
        return
    print("Items in your inventory:")
    for idx, item in enumerate(character['inventory'], start=1):
        print(f"{idx}. {item}")
    print("Which item would you like to sell? (Enter number)")
    choice = input()
    try:
        item = character['inventory'][int(choice) - 1]
        # Simulate selling price based on item
        if item in ['potion of healing', 'elixir of strength', 'scroll of wisdom']:
            price = 10
        elif item in ['enchanted ring', 'magic wand']:
            price = 50
        else:
            price = 5
        character['inventory'].remove(item)
        character['inventory'].append(f"{price} gold")
        print(f"You sold {item} for {price} gold.")
    except (IndexError, ValueError):
        print("Invalid choice. You leave the market.")

def mystical_market(character):
    """
    This function represents a visit to a mystical market where the player can buy and sell magical items.
    """
    print("You enter the mystical market. It is bustling with magical items and mysterious vendors.")
    market_items = {
        'potion of healing': 20,
        'elixir of strength': 50,
        'scroll of wisdom': 40,
        'enchanted ring': 100,
        'magic wand': 150
    }
    print("Items available for purchase:")
    for idx, (item, price) in enumerate(market_items.items(), start=1):
        print(f"{idx}. {item} - {price} gold")
    
    print("1. Buy an item")
    print("2. Sell an item")
    print("3. Leave the market")
    choice = input("What would you like to do? (1/2/3): ")

    if choice == '1':
        buy_item(character, market_items)
    elif choice == '2':
        sell_item(character)
    elif choice == '3':
        print("You decide to leave the mystical market.")
    else:
        print("Invalid choice. You leave the market.")

def buy_item(character, market_items):
    print("Which item would you like to buy? (Enter number)")
    choice = input()
    try:
        item = list(market_items.keys())[int(choice) - 1]
        price = market_items[item]
        if "gold" in character['inventory']:
            gold_amount = int(character['inventory'][character['inventory'].index('gold')].split()[0])
            if gold_amount >= price:
                character['inventory'].remove('gold')
                character['inventory'].append(item)
                print(f"You bought {item} for {price} gold.")
            else:
                print("You don't have enough gold.")
        else:
            print("You don't have any gold.")
    except (IndexError, ValueError):
        print("Invalid choice. You leave the market.")

def ancient_runes(character):
    """
    This function represents an interaction with ancient runes found in a mysterious location.
    The runes can provide various benefits or challenges based on the player's choices.
    """
    print("You find yourself in front of an ancient set of runes, glowing with a mysterious light.")
    print("The runes seem to offer various choices.")
    print("1. Read the runes")
    print("2. Touch the runes")
    print("3. Leave the runes alone")
    choice = input("What would you like to do? (1/2/3): ")

    if choice == '1':
        read_runes(character)
    elif choice == '2':
        touch_runes(character)
    elif choice == '3':
        print("You decide to leave the runes alone and move on.")
    else:
        print("Invalid choice. You leave the area.")


def read_runes(character):
    print("You study the runes carefully. They start to reveal a hidden message.")
    outcomes = [
        "You gain 50 experience points.",
        "You find a hidden treasure chest.",
        "You are cursed with a temporary weakness.",
        "You discover a secret quest."
    ]
    result = random.choice(outcomes)
    if result == "You gain 50 experience points.":
        character['experience'] += 50
        print(result)
    elif result == "You find a hidden treasure chest.":
        treasure(character)
    elif result == "You are cursed with a temporary weakness.":
        character['health'] -= 20
        print(result)
        print(f"Current health: {character['health']}")
    elif result == "You discover a secret quest.":
        new_quest(character)
        print(result)

def touch_runes(character):
    print("You touch the runes and they start to glow intensely.")
    print("Suddenly, you feel a surge of energy.")
    effects = [
        "You gain 20 health points.",
        "You are teleported to a random location.",
        "You receive a magical item.",
        "You gain 100 experience points."
    ]
    effect = random.choice(effects)
    if effect == "You gain 20 health points.":
        character['health'] = min(100, character['health'] + 20)
        print(effect)
    elif effect == "You are teleported to a random location.":
        locations = ['Dark Forest', 'Shadow Cave', 'Crypt']
        location = random.choice(locations)
        print(f"You are teleported to the {location}.")
        if location == 'Dark Forest':
            dark_forest_encounter(character)
        elif location == 'Shadow Cave':
            shadow_cave_encounter(character)
        elif location == 'Crypt':
            crypt_encounter(character)
    elif effect == "You receive a magical item.":
        magical_items = ['ancient scroll', 'enchanted sword', 'mystical gem']
        item = random.choice(magical_items)
        character['inventory'].append(item)
        print(f"You receive a {item}.")
    elif effect == "You gain 100 experience points.":
        character['experience'] += 100
        print(effect)

def legendary_forge(character):
    """
    This function represents a visit to the legendary forge where players can enhance their equipment
    with powerful enchantments, trade rare materials, or seek guidance from the forge master.
    """
    print("You arrive at the Legendary Forge, a place of immense power and craftsmanship.")
    print("The forge master offers several services.")
    print("1. Enchant an item")
    print("2. Trade rare materials")
    print("3. Seek guidance from the forge master")
    print("4. Leave the forge")
    choice = input("What would you like to do? (1/2/3/4): ")

    if choice == '1':
        enchant_item(character)
    elif choice == '2':
        trade_rare_materials(character)
    elif choice == '3':
        seek_guidance(character)
    elif choice == '4':
        print("You decide to leave the Legendary Forge.")
    else:
        print("Invalid choice. You leave the forge.")

def enchant_item(character):
    if not character['inventory']:
        print("You have no items to enchant.")
        return
    print("Items available for enchantment:")
    for idx, item in enumerate(character['inventory'], start=1):
        print(f"{idx}. {item}")
    print("Which item would you like to enchant? (Enter number)")
    choice = input()
    try:
        item = character['inventory'][int(choice) - 1]
        if item in ['sword', 'shield', 'armor']:
            enchantments = ['Fire', 'Ice', 'Lightning', 'Earth']
            enchantment = random.choice(enchantments)
            print(f"Your {item} has been enchanted with {enchantment} power!")
            character['inventory'].append(f"{item} (Enchanted with {enchantment})")
            character['inventory'].remove(item)
        else:
            print("This item cannot be enchanted.")
    except (IndexError, ValueError):
        print("Invalid choice. You leave the forge.")

def trade_rare_materials(character):
    materials = ['dragon scale', 'phoenix feather', 'unicorn horn']
    print("Materials available for trade:")
    for idx, material in enumerate(materials, start=1):
        print(f"{idx}. {material}")
    print("Which material would you like to trade for? (Enter number)")
    choice = input()
    try:
        material = materials[int(choice) - 1]
        print(f"You receive a {material} in exchange for some of your inventory.")
        character['inventory'].append(material)
    except (IndexError, ValueError):
        print("Invalid choice. You leave the forge.")

def seek_guidance(character):
    print("The forge master offers you wisdom and insight.")
    guidance = [
        "You gain 50 experience points.",
        "You are given a special blueprint for an item.",
        "You receive a hint about a hidden quest.",
        "You are blessed with a temporary boost in health."
    ]
    advice = random.choice(guidance)
    if advice == "You gain 50 experience points.":
        character['experience'] += 50
        print(advice)
    elif advice == "You are given a special blueprint for an item.":
        print("You receive a blueprint for a powerful item.")
        character['inventory'].append("blueprint for a powerful item")
    elif advice == "You receive a hint about a hidden quest.":
        hidden_quest = "Defeat the legendary beast"
        print(f"You receive a hint about a hidden quest: '{hidden_quest}'")
        character['quests'].append(hidden_quest)
    elif advice == "You are blessed with a temporary boost in health.":
        character['health'] = min(100, character['health'] + 30)
        print(advice)

def enchanted_grove(character):
    """
    This function represents an interaction with the Enchanted Grove, where the player can perform rituals,
    seek ancient wisdom, or interact with mystical creatures.
    """
    print("You step into the Enchanted Grove, where the air is filled with magic and the sounds of nature.")
    print("1. Perform a ritual")
    print("2. Seek ancient wisdom")
    print("3. Interact with mystical creatures")
    print("4. Leave the grove")
    choice = input("What would you like to do? (1/2/3/4): ")

    if choice == '1':
        perform_ritual(character)
    elif choice == '2':
        seek_wisdom(character)
    elif choice == '3':
        interact_creatures(character)
    elif choice == '4':
        print("You decide to leave the Enchanted Grove.")
    else:
        print("Invalid choice. You leave the grove.")

def perform_ritual(character):
    rituals = [
        "You perform a ritual of healing and restore 50 health points.",
        "You perform a ritual of strength and gain 10 temporary strength points.",
        "You perform a ritual of luck and find a hidden item.",
        "You perform a ritual of protection and gain a temporary shield."
    ]
    ritual = random.choice(rituals)
    if ritual == "You perform a ritual of healing and restore 50 health points.":
        character['health'] = min(100, character['health'] + 50)
        print(ritual)
        print(f"Current health: {character['health']}")
    elif ritual == "You perform a ritual of strength and gain 10 temporary strength points.":
        character['strength'] = character.get('strength', 0) + 10
        print(ritual)
    elif ritual == "You perform a ritual of luck and find a hidden item.":
        hidden_items = ['ancient coin', 'mystic gem', 'rare artifact']
        item = random.choice(hidden_items)
        character['inventory'].append(item)
        print(f"You find a {item}.")
    elif ritual == "You perform a ritual of protection and gain a temporary shield.":
        character['shield'] = character.get('shield', 0) + 20
        print(ritual)

def seek_wisdom(character):
    wisdom = [
        "You gain insight into a hidden location.",
        "You receive knowledge about a powerful enemy.",
        "You discover a new skill.",
        "You are told of a legendary artifact."
    ]
    wisdom_received = random.choice(wisdom)
    if wisdom_received == "You gain insight into a hidden location.":
        locations = ['ancient ruins', 'hidden valley', 'forgotten shrine']
        location = random.choice(locations)
        print(f"You gain insight into a hidden location: {location}.")
        print(f"You can now visit the {location}.")
    elif wisdom_received == "You receive knowledge about a powerful enemy.":
        print("You receive knowledge about a powerful enemy: The Dark Sorcerer.")
        character['quests'].append("Defeat the Dark Sorcerer")
    elif wisdom_received == "You discover a new skill.":
        skills = ['archery', 'alchemy', 'swordsmanship']
        skill = random.choice(skills)
        character['skills'] = character.get('skills', [])
        character['skills'].append(skill)
        print(f"You discover a new skill: {skill}.")
    elif wisdom_received == "You are told of a legendary artifact.":
        print("You are told of a legendary artifact: The Crystal of Eternity.")
        character['quests'].append("Find the Crystal of Eternity")

def interact_creatures(character):
    creatures = [
        'a friendly unicorn',
        'a wise old owl',
        'a mischievous fairy',
        'a helpful forest spirit'
    ]
    creature = random.choice(creatures)
    print(f"You encounter {creature}.")
    if creature == 'a friendly unicorn':
        print("The unicorn offers you a magical blessing.")
        character['health'] = min(100, character['health'] + 20)
        print(f"Your health is now {character['health']}.")
    elif creature == 'a wise old owl':
        print("The owl shares ancient knowledge with you.")
        print("You gain 30 experience points.")
        character['experience'] += 30
    elif creature == 'a mischievous fairy':
        print("The fairy plays a trick on you.")
        print("You lose 10 health points.")
        character['health'] = max(0, character['health'] - 10)
        print(f"Your health is now {character['health']}.")
    elif creature == 'a helpful forest spirit':
        print("The spirit guides you to a hidden treasure.")
        treasure(character)

def hidden_labyrinth(character):
    """
    This function represents an exploration of a hidden labyrinth with various challenges and rewards.
    The player can choose to navigate the labyrinth, solve puzzles, or find hidden treasures.
    """
    print("You enter the Hidden Labyrinth, a maze of twisting corridors and dark passages.")
    print("1. Navigate the labyrinth")
    print("2. Solve a puzzle")
    print("3. Search for hidden treasures")
    print("4. Leave the labyrinth")
    choice = input("What would you like to do? (1/2/3/4): ")

    if choice == '1':
        navigate_labyrinth(character)
    elif choice == '2':
        solve_puzzle(character)
    elif choice == '3':
        search_treasures(character)
    elif choice == '4':
        print("You decide to leave the Hidden Labyrinth.")
    else:
        print("Invalid choice. You leave the labyrinth.")

def navigate_labyrinth(character):
    outcomes = [
        "You find a shortcut and gain 50 experience points.",
        "You encounter a wandering monster and lose 20 health points.",
        "You get lost and spend extra time, gaining 10 experience points.",
        "You find a helpful guide who offers you a clue."
    ]
    result = random.choice(outcomes)
    if result == "You find a shortcut and gain 50 experience points.":
        character['experience'] += 50
        print(result)
    elif result == "You encounter a wandering monster and lose 20 health points.":
        character['health'] = max(0, character['health'] - 20)
        print(result)
        print(f"Current health: {character['health']}")
    elif result == "You get lost and spend extra time, gaining 10 experience points.":
        character['experience'] += 10
        print(result)
    elif result == "You find a helpful guide who offers you a clue.":
        print("The guide tells you about a secret exit.")
        character['quests'].append("Find the secret exit of the labyrinth")

def solve_puzzle(character):
    puzzles = [
        "A riddle about a hidden passage",
        "A mathematical puzzle",
        "A logic challenge",
        "A memory test"
    ]

    puzzle = random.choice(puzzles)
    print(f"You encounter a puzzle: {puzzle}")
    answer = input("Solve the puzzle (type your answer): ")
    # For simplicity, consider any answer correct
    if answer:
        print("You solve the puzzle successfully!")
        reward = random.choice(["You find a hidden key.", "You gain 40 experience points.", "You receive a magical item."])
        if reward == "You find a hidden key.":
            character['inventory'].append("hidden key")
            print(reward)
        elif reward == "You gain 40 experience points.":
            character['experience'] += 40
            print(reward)
        elif reward == "You receive a magical item.":
            magical_items = ['crystal shard', 'mystic cloak', 'enchanted boots']
            item = random.choice(magical_items)
            character['inventory'].append(item)
            print(f"{reward} {item} has been added to your inventory.")
    else:
        print("You fail to solve the puzzle and are forced to leave the area.")

def search_treasures(character):
    treasures = [
        "a chest full of gold",
        "a magical artifact",
        "a rare gem",
        "an ancient scroll"
    ]
    treasure = random.choice(treasures)
    print(f"You find {treasure}.")
    if treasure == "a chest full of gold":
        character['inventory'].append("gold")
        print("You gain 100 gold.")
    elif treasure == "a magical artifact":
        character['inventory'].append("magical artifact")
        print("You find a magical artifact.")
    elif treasure == "a rare gem":
        character['inventory'].append("rare gem")
        print("You find a rare gem.")
    elif treasure == "an ancient scroll":
        character['inventory'].append("ancient scroll")
        print("You find an ancient scroll.")

def dragon_sanctuary(character):
    """
    This function represents a visit to the Dragon Sanctuary, where players can encounter dragons,
    seek powerful allies, or face dangerous trials.
    """
    print("You arrive at the Dragon Sanctuary, a majestic place filled with ancient dragons and mystical energy.")
    print("1. Seek a dragon ally")
    print("2. Face a dragon trial")
    print("3. Explore the sanctuary")
    print("4. Leave the sanctuary")
    choice = input("What would you like to do? (1/2/3/4): ")

    if choice == '1':
        seek_dragon_ally(character)
    elif choice == '2':
        face_dragon_trial(character)
    elif choice == '3':
        explore_sanctuary(character)
    elif choice == '4':
        print("You decide to leave the Dragon Sanctuary.")
    else:
        print("Invalid choice. You leave the sanctuary.")

def seek_dragon_ally(character):
    dragons = [
        'Fire Dragon',
        'Ice Dragon',
        'Earth Dragon',
        'Lightning Dragon'
    ]
    dragon = random.choice(dragons)
    print(f"You seek out the {dragon}.")
    if dragon == 'Fire Dragon':
        print("The Fire Dragon agrees to aid you in battle.")
        character['allies'].append('Fire Dragon')
    elif dragon == 'Ice Dragon':
        print("The Ice Dragon offers you a powerful ice spell.")
        character['inventory'].append('Ice Spell')
    elif dragon == 'Earth Dragon':
        print("The Earth Dragon grants you enhanced strength.")
        character['strength'] = character.get('strength', 0) + 20
    elif dragon == 'Lightning Dragon':
        print("The Lightning Dragon provides you with a lightning-infused weapon.")
        character['inventory'].append('Lightning Sword')

def face_dragon_trial(character):
    trials = [
        'Trial of Fire',
        'Trial of Ice',
        'Trial of Earth',
        'Trial of Lightning'
    ]
    trial = random.choice(trials)
    print(f"You face the {trial}.")
    if trial == 'Trial of Fire':
        if 'Fire Resistance' in character['inventory']:
            print("You successfully pass the Trial of Fire with your Fire Resistance.")
            character['experience'] += 50
        else:
            print("You fail the Trial of Fire and take 30 damage.")
            character['health'] = max(0, character['health'] - 30)
    elif trial == 'Trial of Ice':
        if 'Ice Protection' in character['inventory']:
            print("You successfully pass the Trial of Ice with your Ice Protection.")
            character['experience'] += 50
        else:
            print("You fail the Trial of Ice and take 30 damage.")
            character['health'] = max(0, character['health'] - 30)
    elif trial == 'Trial of Earth':
        print("You successfully pass the Trial of Earth and gain a strength boost.")
        character['strength'] = character.get('strength', 0) + 20
        character['experience'] += 50
    elif trial == 'Trial of Lightning':
        if 'Lightning Shield' in character['inventory']:
            print("You successfully pass the Trial of Lightning with your Lightning Shield.")
            character['experience'] += 50
        else:
            print("You fail the Trial of Lightning and take 30 damage.")
            character['health'] = max(0, character['health'] - 30)

def explore_sanctuary(character):
    discoveries = [
        'a hidden dragon egg',
        'a secret chamber with treasure',
        'an ancient dragon tome',
        'a mystical dragon scale'
    ]
    discovery = random.choice(discoveries)
    print(f"While exploring, you find {discovery}.")
    if discovery == 'a hidden dragon egg':
        print("You find a hidden dragon egg and can choose to keep it or leave it.")
        print("1. Keep the egg")
        print("2. Leave the egg")
        choice = input("What would you like to do? (1/2): ")
        if choice == '1':
            character['inventory'].append('Dragon Egg')
            print("You keep the dragon egg.")
        elif choice == '2':
            print("You leave the dragon egg behind.")
    elif discovery == 'a secret chamber with treasure':
        print("You find a secret chamber filled with treasure!")
        treasure(character)
    elif discovery == 'an ancient dragon tome':
        print("You find an ancient dragon tome and gain knowledge.")
        character['experience'] += 30
        character['inventory'].append('Dragon Tome')
    elif discovery == 'a mystical dragon scale':
        print("You find a mystical dragon scale.")
        character['inventory'].append('Mystical Dragon Scale')

def cursed_tower(character):
    """
    This function represents an exploration of a cursed tower with various floors, each presenting unique challenges and rewards.
    The player can choose to ascend the tower, solve floor-specific challenges, or find hidden secrets.
    """
    print("You enter the Cursed Tower, a towering structure shrouded in dark magic and mystery.")
    print("1. Ascend the tower")
    print("2. Solve a floor challenge")
    print("3. Search for hidden secrets")
    print("4. Leave the tower")
    choice = input("What would you like to do? (1/2/3/4): ")

    if choice == '1':
        ascend_tower(character)
    elif choice == '2':
        solve_floor_challenge(character)
    elif choice == '3':
        search_secrets(character)
    elif choice == '4':
        print("You decide to leave the Cursed Tower.")
    else:
        print("Invalid choice. You leave the tower.")

def ascend_tower(character):
    floors = [
        'Floor of Shadows',
        'Floor of Flames',
        'Floor of Ice',
        'Floor of Echoes'
    ]
    floor = random.choice(floors)
    print(f"You ascend to the {floor}.")
    if floor == 'Floor of Shadows':
        print("You face shadowy figures and must fight to proceed.")
        # Placeholder for combat function
        combat(character)
    elif floor == 'Floor of Flames':
        print("You must navigate through intense flames.")
        if 'Fire Resistance' in character['inventory']:
            print("You pass through the flames unharmed.")
            character['experience'] += 50
        else:
            print("You take 20 damage from the flames.")
            character['health'] = max(0, character['health'] - 20)
    elif floor == 'Floor of Ice':
        print("You must cross a slippery ice floor.")
        if 'Ice Protection' in character['inventory']:
            print("You cross the ice safely.")
            character['experience'] += 50
        else:
            print("You slip and take 15 damage.")
            character['health'] = max(0, character['health'] - 15)
    elif floor == 'Floor of Echoes':
        print("You encounter echoes of past adventurers.")
        outcomes = [
            "You find a clue to the tower's secret.",
            "You receive a mysterious item.",
            "You gain insight into a powerful spell."
        ]
        outcome = random.choice(outcomes)
        if outcome == "You find a clue to the tower's secret.":
            print("You find a clue that helps you understand the tower's mysteries.")
            character['quests'].append("Discover the tower's secret")
        elif outcome == "You receive a mysterious item.":
            mysterious_items = ['Enchanted Ring', 'Phantom Cloak', 'Spectral Blade']
            item = random.choice(mysterious_items)
            character['inventory'].append(item)
            print(f"You receive a {item}.")
        elif outcome == "You gain insight into a powerful spell.":
            print("You gain a powerful spell.")
            character['inventory'].append('Powerful Spell')

def solve_floor_challenge(character):
    challenges = [
        'Solve a riddle about the tower',
        'Complete a combat trial',
        'Navigate a magical maze',
        'Decipher an ancient script'
    ]
    challenge = random.choice(challenges)
    print(f"You encounter a challenge: {challenge}")
    answer = input("Solve the challenge (type your answer): ")
    if answer:
        print("You solve the challenge successfully!")
        reward = random.choice(["You gain 50 experience points.", "You find a hidden treasure.", "You receive a rare item."])
        if reward == "You gain 50 experience points.":
            character['experience'] += 50
            print(reward)
        elif reward == "You find a hidden treasure.":
            treasure(character)
        elif reward == "You receive a rare item.":
            rare_items = ['Ancient Amulet', 'Mystic Staff', 'Golden Chalice']
            item = random.choice(rare_items)
            character['inventory'].append(item)
            print(f"{reward} {item} has been added to your inventory.")
    else:
        print("You fail the challenge and are forced to retreat.")

def search_secrets(character):
    secrets = [
        'a hidden passage',
        'a forgotten spellbook',
        'a cursed artifact',
        'a hidden stash of gold'
    ]
    secret = random.choice(secrets)
    print(f"While searching, you find {secret}.")
    if secret == 'a hidden passage':
        print("You discover a hidden passage leading to a secret room.")
        # Placeholder for secret room function
        secret_room(character)
    elif secret == 'a forgotten spellbook':
        print("You find a forgotten spellbook and gain a new spell.")
        character['inventory'].append('Forgotten Spellbook')
    elif secret == 'a cursed artifact':
        print("You find a cursed artifact. It’s powerful but comes with risks.")
        character['inventory'].append('Cursed Artifact')
    elif secret == 'a hidden stash of gold':
        print("You find a hidden stash of gold!")
        character['inventory'].append('Gold')

def ancient_ruins(character):
    """
    This function represents an exploration of the Ancient Ruins, where players can discover lost relics,
    solve ancient puzzles, or interact with remnants of a long-lost civilization.
    """
    print("You enter the Ancient Ruins, a place filled with the remnants of a once-great civilization.")
    print("1. Discover lost relics")
    print("2. Solve an ancient puzzle")
    print("3. Explore the ruins")
    print("4. Leave the ruins")
    choice = input("What would you like to do? (1/2/3/4): ")

    if choice == '1':
        discover_relics(character)
    elif choice == '2':
        solve_ancient_puzzle(character)
    elif choice == '3':
        explore_ruins(character)
    elif choice == '4':
        print("You decide to leave the Ancient Ruins.")
    else:
        print("Invalid choice. You leave the ruins.")

def discover_relics(character):
    relics = [
        'an ancient sword',
        'a mystical pendant',
        'a golden chalice',
        'a rare tome'
    ]
    relic = random.choice(relics)
    print(f"You discover {relic}.")
    if relic == 'an ancient sword':
        print("The sword is old but still sharp. It adds to your inventory.")
        character['inventory'].append('Ancient Sword')
    elif relic == 'a mystical pendant':
        print("The pendant glows with a strange light. It enhances your magical abilities.")
        character['inventory'].append('Mystical Pendant')
    elif relic == 'a golden chalice':
        print("The chalice is ornate and valuable. It can be sold for a high price.")
        character['inventory'].append('Golden Chalice')
    elif relic == 'a rare tome':
        print("The tome contains ancient knowledge. You gain 50 experience points.")
        character['experience'] += 50
        character['inventory'].append('Rare Tome')

def solve_ancient_puzzle(character):
    puzzles = [
        'A puzzle involving ancient symbols',
        'A complex mathematical problem',
        'A logic riddle',
        'A word game'
    ]
        puzzle = random.choice(puzzles)
    print(f"You encounter an ancient puzzle: {puzzle}")
    answer = input("Solve the puzzle (type your answer): ")
    if answer:
        print("You solve the puzzle successfully!")
        reward = random.choice(["You find a hidden relic.", "You gain 40 experience points.", "You discover a new spell."])
        if reward == "You find a hidden relic.":
            relics = ['Ancient Shield', 'Enchanted Dagger', 'Mystic Robe']
            relic = random.choice(relics)
            character['inventory'].append(relic)
            print(f"You find a {relic}.")
        elif reward == "You gain 40 experience points.":
            character['experience'] += 40
            print(reward)
        elif reward == "You discover a new spell.":
            spells = ['Fireball', 'Frostbolt', 'Lightning Strike']
            spell = random.choice(spells)
            character['inventory'].append(spell)
            print(f"You discover a new spell: {spell}.")
    else:
        print("You fail to solve the puzzle and are forced to leave the ruins.")

def explore_ruins(character):
    explorations = [
        'a hidden chamber with treasures',
        'an ancient altar with mysterious runes',
        'a secret passage leading to a forgotten crypt',
        'a well-preserved mural depicting ancient history'
    ]
    exploration = random.choice(explorations)
    print(f"While exploring, you find {exploration}.")
    if exploration == 'a hidden chamber with treasures':
        print("You find a hidden chamber filled with treasures!")
        treasure(character)
    elif exploration == 'an ancient altar with mysterious runes':
        print("The altar holds mysterious runes that you can study.")
        runes = [
            'Runes of Strength',
            'Runes of Wisdom',
            'Runes of Agility',
            'Runes of Protection'
        ]
        rune = random.choice(runes)
        print(f"You study the {rune}.")
        character['inventory'].append(rune)
    elif exploration == 'a secret passage leading to a forgotten crypt':
        print("The passage leads to a forgotten crypt with ancient secrets.")
        print("You find a powerful artifact in the crypt.")
        artifacts = ['Ancient Crown', 'Cursed Amulet', 'Mystic Staff']
        artifact = random.choice(artifacts)
        character['inventory'].append(artifact)
        print(f"You find a {artifact}.")
    elif exploration == 'a well-preserved mural depicting ancient history':
        print("The mural depicts the history of the ancient civilization.")
        print("You gain insight into the ruins’ history and lore.")
        character['experience'] += 30

def enchanted_forest(character):
    """
    This function represents an exploration of the Enchanted Forest, a magical place full of mystical creatures,
    hidden pathways, and ancient magic.
    """
    print("You step into the Enchanted Forest, a lush and vibrant place filled with magical energy.")
    print("1. Interact with magical creatures")
    print("2. Find a hidden pathway")
    print("3. Discover ancient magic")
    print("4. Leave the forest")
    choice = input("What would you like to do? (1/2/3/4): ")

    if choice == '1':
        interact_creatures(character)
    elif choice == '2':
        find_pathway(character)
    elif choice == '3':
        discover_magic(character)
    elif choice == '4':
        print("You decide to leave the Enchanted Forest.")
    else:
        print("Invalid choice. You leave the forest.")

def interact_creatures(character):
    creatures = [
        'a talking fox',
        'a wise old owl',
        'a mischievous sprite',
        'a gentle unicorn'
    ]
    creature = random.choice(creatures)
    print(f"You encounter {creature}.")
    if creature == 'a talking fox':
        print("The talking fox offers you a riddle.")
        answer = input("Solve the riddle (type your answer): ")
        if answer:
            print("You solve the riddle!")
            print("The fox rewards you with a magical charm.")
            character['inventory'].append('Magical Charm')
        else:
            print("You fail to solve the riddle. The fox disappears.")
    elif creature == 'a wise old owl':
        print("The owl offers you wisdom.")
        wisdom = random.choice(['Insight into a hidden path', 'Knowledge of an ancient spell'])
        print(f"The owl imparts {wisdom}.")
        character['inventory'].append(wisdom)
    elif creature == 'a mischievous sprite':
        print("The sprite plays a prank on you.")
        print("You lose 10 experience points.")
        character['experience'] = max(0, character['experience'] - 10)
    elif creature == 'a gentle unicorn':
        print("The unicorn grants you a blessing.")
        print("You gain 30 experience points and a healing potion.")
        character['experience'] += 30
        character['inventory'].append('Healing Potion')


def find_pathway(character):
    pathways = [
        'a path leading to a hidden grove',
        'a trail leading to a mystical waterfall',
        'a secret way to an ancient ruin',
        'a hidden entrance to a magical glade'
    ]
    pathway = random.choice(pathways)
    print(f"You find {pathway}.")
    if pathway == 'a path leading to a hidden grove':
        print("You find a hidden grove with rare herbs.")
        print("You gather herbs for crafting potions.")
        character['inventory'].append('Rare Herbs')
    elif pathway == 'a trail leading to a mystical waterfall':
        print("The waterfall has magical properties.")
        print("You gain a temporary boost in magic power.")
        character['inventory'].append('Magic Boost')
    elif pathway == 'a secret way to an ancient ruin':
        print("You discover an ancient ruin.")
        print("Explore the ruin to find hidden treasures.")
        # Placeholder for ruin exploration function
        ancient_ruins(character)
    elif pathway == 'a hidden entrance to a magical glade':
        print("You enter a magical glade.")
        print("The glade has powerful enchantments.")
        character['inventory'].append('Enchanted Gem')

def discover_magic(character):
    magics = [
        'a spell of invisibility',
        'a potion of strength',
        'an enchanted map',
        'a magical staff'
    ]
    magic = random.choice(magics)
    print(f"You discover {magic}.")
    if magic == 'a spell of invisibility':
        print("The spell allows you to become invisible for a short time.")
        character['inventory'].append('Spell of Invisibility')
    elif magic == 'a potion of strength':
        print("The potion grants you enhanced strength for a while.")
        character['inventory'].append('Potion of Strength')
    elif magic == 'an enchanted map':
        print("The map reveals hidden locations in the forest.")
        character['inventory'].append('Enchanted Map')
    elif magic == 'a magical staff':
        print("The staff is imbued with magical properties.")
        character['inventory'].append('Magical Staff')

def mysterious_cave(character):
    """
    This function represents an exploration of the Mysterious Cave, a dark and enigmatic place full of secrets,
    hidden dangers, and ancient treasures.
    """
    print("You enter the Mysterious Cave, a place shrouded in darkness and mystery.")
    print("1. Search for hidden treasures")
    print("2. Solve a cave riddle")
    print("3. Encounter cave creatures")
    print("4. Leave the cave")
    choice = input("What would you like to do? (1/2/3/4): ")

    if choice == '1':
        search_treasures(character)
    elif choice == '2':
        solve_cave_riddle(character)
    elif choice == '3':
        encounter_creatures(character)
    elif choice == '4':
        print("You decide to leave the Mysterious Cave.")
    else:
        print("Invalid choice. You leave the cave.")

def search_treasures(character):
    treasures = [
        'a chest of gold coins',
        'a mystical gem',
        'an ancient relic',
        'a rare artifact'
    ]
    treasure = random.choice(treasures)
    print(f"You find {treasure}.")
    if treasure == 'a chest of gold coins':
        print("The chest contains a large amount of gold.")
        character['inventory'].append('Gold Coins')
        print("You gain 100 gold coins.")
        # Placeholder for currency handling
        character['gold'] = character.get('gold', 0) + 100
    elif treasure == 'a mystical gem':
        print("The gem glows with a magical light.")
        character['inventory'].append('Mystical Gem')
        print("The gem may have magical properties.")
    elif treasure == 'an ancient relic':
        print("The relic is old and valuable.")
        character['inventory'].append('Ancient Relic')
        print("You gain 50 experience points.")
        character['experience'] += 50
    elif treasure == 'a rare artifact':
        print("The artifact is rare and powerful.")
        character['inventory'].append('Rare Artifact')
        print("You gain a special ability from the artifact.")
        # Placeholder for special abilities
        character['abilities'].append('Special Ability')


def solve_cave_riddle(character):
    riddles = [
        'I speak without a mouth and hear without ears. I have nobody, but I come alive with the wind. What am I?',
        'I’m not alive, but I grow; I don’t have lungs, but I need air; I don’t have a mouth, but water kills me. What am I?',
        'The more of this there is, the less you see. What is it?',
        'I can be cracked, made, told, and played. What am I?'
    ]
    riddle = random.choice(riddles)
    print(f"You encounter a riddle: {riddle}")
    answer = input("Solve the riddle (type your answer): ")
    if answer:
        print("You solve the riddle!")
        reward = random.choice(["You find a hidden treasure.", "You gain 40 experience points.", "You discover a new spell."])
        if reward == "You find a hidden treasure.":
            search_treasures(character)
        elif reward == "You gain 40 experience points.":
            character['experience'] += 40
            print(reward)
        elif reward == "You discover a new spell.":
            spells = ['Heal', 'Teleport', 'Shield']
            spell = random.choice(spells)
            character['inventory'].append(spell)
            print(f"You discover a new spell: {spell}.")
    else:
        print("You fail to solve the riddle and are forced to leave the cave.")

def encounter_creatures(character):
    creatures = [
        'a cave troll',
        'a giant spider',
        'a swarm of bats',
        'a rock golem'
    ]
    creature = random.choice(creatures)
    print(f"You encounter {creature}.")
    if creature == 'a cave troll':
        print("The cave troll is aggressive. Prepare for battle!")
        # Placeholder for combat function
        combat(character)
    elif creature == 'a giant spider':
        print("The giant spider attacks from above!")
        # Placeholder for combat function
        combat(character)
    elif creature == 'a swarm of bats':
        print("The bats are numerous and disorienting.")
        print("You lose 10 experience points due to their distraction.")
        character['experience'] = max(0, character['experience'] - 10)
    elif creature == 'a rock golem':
        print("The rock golem is powerful and slow.")
        print("You manage to defeat it and gain 50 experience points.")
        character['experience'] += 50

def mystical_library(character):
    """
    This function represents an exploration of the Mystical Library, a place full of ancient books,
    magical scrolls, and hidden knowledge.
    """
    print("You step into the Mystical Library, a vast space filled with ancient tomes and magical scrolls.")
    print("1. Read ancient books")
    print("2. Study magical scrolls")
    print("3. Search for hidden knowledge")
    print("4. Leave the library")
    choice = input("What would you like to do? (1/2/3/4): ")

    if choice == '1':
        read_books(character)
    elif choice == '2':
        study_scrolls(character)
    elif choice == '3':
        search_knowledge(character)
    elif choice == '4':
        print("You decide to leave the Mystical Library.")
    else:
        print("Invalid choice. You leave the library.")

def read_books(character):
    books = [
        'a tome of ancient lore',
        'a book on magical creatures',
        'a history of the arcane arts',
        'a guide to powerful spells'
    ]
    book = random.choice(books)
    print(f"You read {book}.")
    if book == 'a tome of ancient lore':
        print("You gain insight into ancient knowledge.")
        character['experience'] += 40
    elif book == 'a book on magical creatures':
        print("You learn about magical creatures.")
        print("You gain 30 experience points and a magical creature companion.")
        character['experience'] += 30
        character['companions'].append('Magical Creature')
    elif book == 'a history of the arcane arts':
        print("You gain knowledge of the arcane arts.")
        print("You learn a new spell.")
        spells = ['Arcane Missile', 'Mystic Shield', 'Teleport']
        spell = random.choice(spells)
        character['inventory'].append(spell)
    elif book == 'a guide to powerful spells':
        print("You gain insight into powerful spells.")
        print("You gain 50 experience points.")
        character['experience'] += 50

def study_scrolls(character):
    scrolls = [
        'a scroll of healing',
        'a scroll of fireball',
        'a scroll of teleportation',
        'a scroll of invisibility'
    ]
    scroll = random.choice(scrolls)
    print(f"You study {scroll}.")
    if scroll == 'a scroll of healing':
        print("You learn the healing spell from the scroll.")
        character['inventory'].append('Healing Spell')
    elif scroll == 'a scroll of fireball':
        print("You learn the fireball spell from the scroll.")
        character['inventory'].append('Fireball Spell')
    elif scroll == 'a scroll of teleportation':
        print("You learn the teleportation spell from the scroll.")
        character['inventory'].append('Teleportation Spell')
    elif scroll == 'a scroll of invisibility':
        print("You learn the invisibility spell from the scroll.")
        character['inventory'].append('Invisibility Spell')

def search_knowledge(character):
    knowledge = [
        'an ancient artifact',
        'a hidden manuscript',
        'a rare magical item',
        'a forgotten spell'
    ]
    item = random.choice(knowledge)
    print(f"You find {item}.")
    if item == 'an ancient artifact':
        print("The artifact is powerful and adds to your inventory.")
        character['inventory'].append('Ancient Artifact')
        print("You gain 60 experience points.")
        character['experience'] += 60
    elif item == 'a hidden manuscript':
        print("The manuscript contains lost knowledge.")
        character['inventory'].append('Hidden Manuscript')
        print("You gain a new ability.")
        character['abilities'].append('New Ability')
    elif item == 'a rare magical item':
        print("The item is rare and valuable.")
        character['inventory'].append('Rare Magical Item')
        print("You gain 50 experience points.")
        character['experience'] += 50
    elif item == 'a forgotten spell':
        print("You learn a forgotten spell.")
        spells = ['Ice Storm', 'Lightning Bolt', 'Earthquake']
        spell = random.choice(spells)
        character['inventory'].append(spell)

def shadow_lair(character):
    """
    This function represents an exploration of the Shadow Lair, a dark and foreboding place inhabited by shadowy
    creatures and filled with hidden dangers.
    """
    print("You enter the Shadow Lair, a place shrouded in darkness and mystery.")
    print("1. Confront shadow creatures")
    print("2. Search for hidden traps")
    print("3. Find a lost artifact")
    print("4. Leave the lair")
    choice = input("What would you like to do? (1/2/3/4): ")

    if choice == '1':
        confront_creatures(character)
    elif choice == '2':
        search_traps(character)
    elif choice == '3':
        find_artifact(character)
    elif choice == '4':
        print("You decide to leave the Shadow Lair.")
    else:
        print("Invalid choice. You leave the lair.")

def confront_creatures(character):
    creatures = [
        'a shadow demon',
        'a wraith',
        'a dark knight',
        'a shadow hound'
    ]
    creature = random.choice(creatures)
    print(f"You encounter {creature}.")
    if creature == 'a shadow demon':
        print("The shadow demon is a powerful foe!")
        print("Prepare for a tough battle.")
        # Placeholder for combat function
        combat(character)
    elif creature == 'a wraith':
        print("The wraith moves silently and strikes from the shadows.")
        print("You defeat the wraith and gain 30 experience points.")
        character['experience'] += 30
    elif creature == 'a dark knight':
        print("The dark knight challenges you to a duel.")
        print("You manage to defeat the dark knight and gain 50 experience points.")
        character['experience'] += 50
    elif creature == 'a shadow hound':
        print("The shadow hound attacks swiftly.")
        print("You successfully fend off the hound and find a hidden cache of items.")
        items = ['Shadow Cloak', 'Phantom Dagger', 'Night Vision Amulet']
        item = random.choice(items)
        character['inventory'].append(item)
        print(f"You find a {item}.")


def search_traps(character):
    traps = [
        'a pitfall trap',
        'a spike trap',
        'a magical rune trap',
        'a poison gas trap'
    ]
    trap = random.choice(traps)
    print(f"You find {trap}.")
    if trap == 'a pitfall trap':
        print("You manage to avoid the pitfall trap.")
        print("You gain 20 experience points for your agility.")
        character['experience'] += 20
    elif trap == 'a spike trap':
        print("You carefully disarm the spike trap.")
        print("You gain 30 experience points for your skill.")
        character['experience'] += 30
    elif trap == 'a magical rune trap':
        print("You decipher the runes and avoid the trap.")
        print("You find a magical rune and add it to your inventory.")
        character['inventory'].append('Magical Rune')
    elif trap == 'a poison gas trap':
        print("You quickly neutralize the poison gas.")
        print("You gain 40 experience points for your quick thinking.")
        character['experience'] += 40

def find_artifact(character):
    artifacts = [
        'a cursed relic',
        'an ancient tome',
        'a shadow gem',
        'a powerful staff'
    ]
    artifact = random.choice(artifacts)
    print(f"You find {artifact}.")
    if artifact == 'a cursed relic':
        print("The relic is cursed but valuable.")
        character['inventory'].append('Cursed Relic')
        print("You gain 30 experience points but suffer a minor curse.")
        character['experience'] += 30
        # Placeholder for minor curse effects
    elif artifact == 'an ancient tome':
        print("The tome contains ancient knowledge.")
        character['inventory'].append('Ancient Tome')
        print("You gain 50 experience points from the knowledge.")
        character['experience'] += 50
    elif artifact == 'a shadow gem':
        print("The shadow gem pulses with dark energy.")
        character['inventory'].append('Shadow Gem')
        print("You gain 40 experience points.")
        character['experience'] += 40
    elif artifact == 'a powerful staff':
        print("The staff radiates immense power.")
        character['inventory'].append('Powerful Staff')
        print("You gain 60 experience points and a new magical ability.")
        character['experience'] += 60
        character['abilities'].append('New Magical Ability')

def ancient_ruins(character):
    """
    This function represents an exploration of the Ancient Ruins, a place full of old structures, forgotten lore,
    and hidden treasures.
    """
    print("You explore the Ancient Ruins, a site filled with old structures and mysterious artifacts.")
    print("1. Explore the ruins")
    print("2. Decode ancient inscriptions")
    print("3. Search for hidden treasures")
    print("4. Leave the ruins")
    choice = input("What would you like to do? (1/2/3/4): ")

    if choice == '1':
        explore_ruins(character)
    elif choice == '2':
        decode_inscriptions(character)
    elif choice == '3':
        search_treasures(character)
    elif choice == '4':
        print("You decide to leave the Ancient Ruins.")
    else:
        print("Invalid choice. You leave the ruins.")

def explore_ruins(character):
    """
    This function handles exploration within the Ancient Ruins, allowing the player to uncover secrets and hidden areas.
    """
    print("You delve deeper into the Ancient Ruins, discovering hidden chambers and forgotten areas.")
    areas = [
        'an underground vault',
        'a hidden library',
        'a forgotten temple',
        'a secret passage'
    ]
    area = random.choice(areas)
    print(f"You find {area}.")
    if area == 'an underground vault':
        print("The vault contains old treasures.")
        print("You find a chest with gold and artifacts.")
        character['inventory'].append('Vault Treasures')
        character['gold'] = character.get('gold', 0) + 150
        print("You gain 150 gold coins.")
    elif area == 'a hidden library':
        print("The library contains ancient scrolls and books.")
        print("You gain knowledge and a new spell.")
        character['inventory'].append('Ancient Scroll')
        spells = ['Summon Elemental', 'Arcane Blast', 'Time Stop']
        spell = random.choice(spells)
        character['inventory'].append(spell)
    elif area == 'a forgotten temple':
        print("The temple holds ancient secrets.")
        print("You discover a powerful relic.")
        character['inventory'].append('Temple Relic')
        print("You gain 70 experience points.")
        character['experience'] += 70
    elif area == 'a secret passage':
        print("The passage leads to hidden rooms.")
        print("You find rare items and a new ability.")
        items = ['Elven Boots', 'Shadow Dagger']
        item = random.choice(items)
        character['inventory'].append(item)
        character['abilities'].append('Enhanced Agility')
        print(f"You find a {item} and gain Enhanced Agility.")

def enchanted_forest(character):
    """
    This function represents an exploration of the Enchanted Forest, a magical place filled with mystical creatures,
    hidden paths, and ancient magic.
    """
    print("You enter the Enchanted Forest, a place where magic and mystery abound.")
    print("1. Encounter mystical creatures")
    print("2. Explore hidden paths")
    print("3. Discover ancient magic")
    print("4. Leave the forest")
    choice = input("What would you like to do? (1/2/3/4): ")

    if choice == '1':
        encounter_mystical_creatures(character)
    elif choice == '2':
        explore_paths(character)
    elif choice == '3':
        discover_magic(character)
    elif choice == '4':
        print("You decide to leave the Enchanted Forest.")
    else:
        print("Invalid choice. You leave the forest.")

def encounter_mystical_creatures(character):
    """
    This function handles encounters with mystical creatures in the Enchanted Forest.
    """
    creatures = [
        'a unicorn',
        'a griffin',
        'a fairy',
        'a dragon'
    ]
    creature = random.choice(creatures)
    print(f"You encounter {creature}.")
    if creature == 'a unicorn':
        print("The unicorn is gentle and grants you a blessing.")
        character['inventory'].append('Unicorn Horn')
        print("You gain 30 experience points and a magical blessing.")
        character['experience'] += 30
        # Placeholder for magical blessing effects
    elif creature == 'a griffin':
        print("The griffin is majestic and offers guidance.")
        print("You gain 50 experience points and a map to hidden places.")
        character['experience'] += 50
        character['inventory'].append('Griffin Map')
    elif creature == 'a fairy':
        print("The fairy offers you a choice of gifts.")
        gifts = ['a potion of invisibility', 'a charm of strength', 'a scroll of wisdom']
        gift = random.choice(gifts)
        character['inventory'].append(gift)
        print(f"You receive {gift}.")
    elif creature == 'a dragon':
        print("The dragon is powerful and fierce.")
        print("You must defeat the dragon to continue.")
        # Placeholder for combat function
        combat(character)

def explore_paths(character):
    """
    This function allows the player to explore hidden paths in the Enchanted Forest.
    """
    paths = [
        'a hidden glade',
        'a magical spring',
        'a forgotten grove',
        'an ancient tree'
    ]
    path = random.choice(paths)
    print(f"You discover {path}.")
    if path == 'a hidden glade':
        print("The glade is peaceful and filled with rare herbs.")
        print("You find herbs for healing.")
        character['inventory'].append('Healing Herbs')
        print("You gain 20 experience points.")
        character['experience'] += 20
    elif path == 'a magical spring':
        print("The spring has magical properties.")
        print("You drink from the spring and gain 50 experience points.")
        character['experience'] += 50
        character['gold'] = character.get('gold', 0) + 50
    elif path == 'a forgotten grove':
        print("The grove is ancient and holds hidden knowledge.")
        print("You gain 40 experience points and a new spell.")
        character['experience'] += 40
        spells = ['Nature’s Blessing', 'Healing Wave', 'Bark Skin']
        spell = random.choice(spells)
        character['inventory'].append(spell)
    elif path == 'an ancient tree':
        print("The tree is wise and offers you advice.")
        print("You gain 30 experience points and a magical item.")
        character['experience'] += 30
        items = ['Enchanted Ring', 'Mystic Pendant']
        item = random.choice(items)
        character['inventory'].append(item)

def discover_magic(character):
    """
    This function allows the player to discover ancient magic hidden in the Enchanted Forest.
    """
    magic_items = [
        'a staff of light',
        'a tome of ancient spells',
        'a crystal orb',
        'a magical cloak'
    ]
    item = random.choice(magic_items)
    print(f"You find {item}.")
    if item == 'a staff of light':
        print("The staff glows with pure light.")
        character['inventory'].append('Staff of Light')
        print("You gain 60 experience points and a new light-based spell.")
        character['experience'] += 60
        character['inventory'].append('Light Beam Spell')
    elif item == 'a tome of ancient spells':
        print("The tome is filled with powerful spells.")
        character['inventory'].append('Tome of Spells')
        print("You gain 70 experience points and learn a new spell.")
        character['experience'] += 70
        spells = ['Fire Storm', 'Ice Barrier', 'Wind Fury']
        spell = random.choice(spells)
        character['inventory'].append(spell)
    elif item == 'a crystal orb':
        print("The orb shows glimpses of the future.")
        character['inventory'].append('Crystal Orb')
        print("You gain 50 experience points and insight into future events.")
        character['experience'] += 50
    elif item == 'a magical cloak':
        print("The cloak provides invisibility.")
        character['inventory'].append('Magical Cloak')
        print("You gain 40 experience points and the ability to become invisible for a short time.")
        character['experience'] += 40

def dragon_cave(character):
    """
    This function represents an exploration of the Dragon Cave, a dangerous place inhabited by powerful dragons
    and filled with hidden treasures and traps.
    """
    print("You enter the Dragon Cave, a perilous area filled with the scent of sulfur and the roar of dragons.")
    print("1. Challenge the dragon")
    print("2. Search for hidden treasures")
    print("3. Avoid traps")
    print("4. Leave the cave")
    choice = input("What would you like to do? (1/2/3/4): ")

    if choice == '1':
        challenge_dragon(character)
    elif choice == '2':
        search_cave_treasures(character)
    elif choice == '3':
        avoid_traps(character)
    elif choice == '4':
        print("You decide to leave the Dragon Cave.")
    else:
        print("Invalid choice. You leave the cave.")

def challenge_dragon(character):
    """
    This function handles the challenge of facing a dragon in the Dragon Cave.
    """
    dragons = [
        'a young dragon',
        'a fire-breathing dragon',
        'a frost dragon',
        'a legendary dragon'
    ]
    dragon = random.choice(dragons)
    print(f"You encounter {dragon}.")
    if dragon == 'a young dragon':
        print("The young dragon is fierce but not very experienced.")
        print("You defeat the dragon and gain 50 experience points.")
        character['experience'] += 50
    elif dragon == 'a fire-breathing dragon':
        print("The fire-breathing dragon is a formidable opponent.")
        # Placeholder for combat function
        combat(character)
    elif dragon == 'a frost dragon':
        print("The frost dragon breathes icy breath.")
        print("You manage to defeat the dragon and gain 60 experience points.")
        character['experience'] += 60
    elif dragon == 'a legendary dragon':
        print("The legendary dragon is incredibly powerful.")
        # Placeholder for combat function
        combat(character)
        print("You defeat the legendary dragon and gain 100 experience points.")
        character['experience'] += 100


def search_cave_treasures(character):
    """
    This function allows the player to search for treasures within the Dragon Cave.
    """
    treasures = [
        'a dragon’s hoard of gold',
        'a gem-encrusted crown',
        'a magical elixir',
        'a dragon scale shield'
    ]
    treasure = random.choice(treasures)
    print(f"You find {treasure}.")
    if treasure == 'a dragon’s hoard of gold':
        print("The hoard contains a large amount of gold.")
        character['inventory'].append('Dragon’s Gold')
        character['gold'] = character.get('gold', 0) + 500
        print("You gain 500 gold coins.")
    elif treasure == 'a gem-encrusted crown':
        print("The crown is adorned with precious gems.")
        character['inventory'].append('Gem-encrusted Crown')
        print("You gain 40 experience points and a boost in charisma.")
        character['experience'] += 40
    elif treasure == 'a magical elixir':
        print("The elixir has healing properties.")
        character['inventory'].append('Magical Elixir')
        print("You gain 30 experience points and full health restoration.")
        character['experience'] += 30
        # Placeholder for health restoration
    elif treasure == 'a dragon scale shield':
        print("The shield is made from dragon scales.")
        character['inventory'].append('Dragon Scale Shield')
        print("You gain 50 experience points and increased defense.")
        character['experience'] += 50

def avoid_traps(character):
    """
    This function handles avoiding traps within the Dragon Cave.
    """
    traps = [
        'a lava pit',
        'a collapsing ceiling',
        'a poisonous gas trap',
        'a hidden pitfall'
    ]
    trap = random.choice(traps)
    print(f"You encounter {trap}.")
    if trap == 'a lava pit':
        print("You narrowly avoid falling into the lava pit.")
        print("You gain 20 experience points for your agility.")
        character['experience'] += 20
    elif trap == 'a collapsing ceiling':
        print("You dodge falling debris from the collapsing ceiling.")
        print("You gain 30 experience points for your quick reflexes.")
        character['experience'] += 30
    elif trap == 'a poisonous gas trap':
        print("You manage to escape the poisonous gas trap.")
        print("You find an antidote and gain 40 experience points.")
        character['experience'] += 40
        character['inventory'].append('Antidote')
    elif trap == 'a hidden pitfall':
        print("You spot the hidden pitfall just in time.")
        print("You gain 25 experience points for your keen senses.")
        character['experience'] += 25

def haunted_mansion(character):
    """
    This function represents an exploration of the Haunted Mansion, a spooky place filled with ghosts, hidden rooms,
    and eerie surprises.
    """
    print("You step into the Haunted Mansion, a place full of ghosts and unsettling mysteries.")
    print("1. Investigate the haunted rooms")
    print("2. Search for hidden passages")
    print("3. Communicate with the spirits")
    print("4. Leave the mansion")
    choice = input("What would you like to do? (1/2/3/4): ")

    if choice == '1':
        investigate_rooms(character)
    elif choice == '2':
        search_passages(character)
    elif choice == '3':
        communicate_spirits(character)
    elif choice == '4':
        print("You decide to leave the Haunted Mansion.")
    else:
        print("Invalid choice. You leave the mansion.")

def investigate_rooms(character):
    """
    This function handles the investigation of haunted rooms within the Haunted Mansion.
    """
    rooms = [
        'a dusty library',
        'a grand ballroom',
        'a forgotten study',
        'a creepy attic'
    ]
    room = random.choice(rooms)
    print(f"You explore {room}.")
    if room == 'a dusty library':
        print("The library contains old, enchanted books.")
        print("You find a spellbook and gain 40 experience points.")
        character['experience'] += 40
        character['inventory'].append('Spellbook')
    elif room == 'a grand ballroom':
        print("The ballroom is filled with eerie music and ghostly figures.")
        print("You dance with a ghost and gain 50 experience points.")
        character['experience'] += 50
    elif room == 'a forgotten study':
        print("The study holds clues to the mansion’s mysteries.")
        print("You find a diary and gain 30 experience points.")
        character['experience'] += 30
        character['inventory'].append('Mansion Diary')
    elif room == 'a creepy attic':
        print("The attic is dark and full of old furniture.")
        print("You find a hidden chest with old relics.")
        relics = ['Phantom Mask', 'Ghostly Necklace']
        relic = random.choice(relics)
        character['inventory'].append(relic)
        print(f"You find a {relic}.")

def search_passages(character):
    """
    This function allows the player to search for hidden passages within the Haunted Mansion.
    """
    passages = [
        'a secret room behind a bookshelf',
        'an underground tunnel',
        'a hidden chamber behind a painting',
        'a concealed door in the fireplace'
    ]


    passage = random.choice(passages)
    print(f"You discover {passage}.")
    if passage == 'a secret room behind a bookshelf':
        print("The room contains old artifacts.")
        artifacts = ['Ancient Mirror', 'Old Lantern']
        artifact = random.choice(artifacts)
        character['inventory'].append(artifact)
        print(f"You find an {artifact}.")
    elif passage == 'an underground tunnel':
        print("The tunnel leads to a hidden vault.")
        print("You find a cache of gold and gain 60 experience points.")
        character['gold'] = character.get('gold', 0) + 300
        character['experience'] += 60
    elif passage == 'a hidden chamber behind a painting':
        print("The chamber holds a magical artifact.")
        print("You gain 70 experience points and a rare artifact.")
        character['experience'] += 70
        character['inventory'].append('Magical Artifact')
    elif passage == 'a concealed door in the fireplace':
        print("The door leads to a room filled with ghostly treasures.")
        print("You find a Ghostly Amulet and gain 50 experience points.")
        character['experience'] += 50
        character['inventory'].append('Ghostly Amulet')

def communicate_spirits(character):
    """
    This function allows the player to communicate with spirits in the Haunted Mansion.
    """
    spirits = [
        'a vengeful spirit',
        'a helpful ghost',
        'a lost soul',
        'a mischievous poltergeist'
    ]
    spirit = random.choice(spirits)
    print(f"You encounter {spirit}.")
    if spirit == 'a vengeful spirit':
        print("The spirit demands a sacrifice.")
        print("You must make a choice: give up an item or face the consequences.")
        # Placeholder for sacrifice decision
        sacrifice_item(character)
    elif spirit == 'a helpful ghost':
        print("The ghost offers you guidance and a clue.")
        print("You gain 40 experience points and a clue to the mansion’s secrets.")
        character['experience'] += 40
        character['inventory'].append('Clue')
    elif spirit == 'a lost soul':
        print("The soul seeks peace and offers a reward.")
        print("You gain 50 experience points and a rare item.")
        character['experience'] += 50
        character['inventory'].append('Rare Item')
    elif spirit == 'a mischievous poltergeist':
        print("The poltergeist plays tricks on you.")
        print("You lose 20 experience points but find a hidden cache of items.")
        character['experience'] -= 20
        items = ['Prank Box', 'Trick Item']
        item = random.choice(items)
        character['inventory'].append(item)
        print(f"You find a {item}.")

def sacrifice_item(character):
    """
    This function handles the decision-making process when dealing with a vengeful spirit.
    """
    print("Choose an item to sacrifice:")
    for idx, item in enumerate(character['inventory']):
        print(f"{idx + 1}. {item}")
    choice = input("Enter the number of the item to sacrifice: ")
    try:
        item_index = int(choice) - 1
        if 0 <= item_index < len(character['inventory']):
            item = character['inventory'].pop(item_index)
            print(f"You sacrifice the {item}.")
            # Placeholder for consequences of sacrifice
        else:
            print("Invalid choice. The spirit grows angrier.")
            # Placeholder for negative consequences
    except ValueError:
        print("Invalid input. The spirit grows angrier.")
        # Placeholder for negative consequences

def lost_city(character):
    """
    This function represents an exploration of the Lost City, a mysterious and ancient place filled with ruins,
    puzzles, and hidden treasures.
    """
    print("You arrive at the Lost City, a place shrouded in legend and mystery.")
    print("1. Solve ancient puzzles")
    print("2. Explore the ruins")
    print("3. Search for hidden treasures")
    print("4. Leave the city")
    choice = input("What would you like to do? (1/2/3/4): ")

    if choice == '1':
        solve_puzzles(character)
    elif choice == '2':
        explore_ruins(character)
    elif choice == '3':
        search_treasures(character)
    elif choice == '4':
        print("You decide to leave the Lost City.")
    else:
        print("Invalid choice. You leave the city.")

def solve_puzzles(character):
    """
    This function handles solving ancient puzzles within the Lost City.
    """
    puzzles = [
        'a riddle of the ancients',
        'a sliding tile puzzle',
        'a code to decipher',
        'a hidden lever puzzle'
    ]
    puzzle = random.choice(puzzles)
    print(f"You encounter {puzzle}.")
    if puzzle == 'a riddle of the ancients':
        print("You solve the riddle and gain 40 experience points.")
        character['experience'] += 40
        print("You find a hidden passage behind the puzzle.")
        character['inventory'].append('Ancient Key')
    elif puzzle == 'a sliding tile puzzle':
        print("You complete the sliding tile puzzle.")
        print("You gain 30 experience points and find a small treasure.")
        character['experience'] += 30
        character['inventory'].append('Small Treasure')
    elif puzzle == 'a code to decipher':
        print("You decipher the code and gain 50 experience points.")
        print("You find a map with hidden locations marked on it.")
        character['experience'] += 50
        character['inventory'].append('Hidden Locations Map')
    elif puzzle == 'a hidden lever puzzle':
        print("You discover and pull the hidden lever.")
        print("You gain 35 experience points and a magical item.")
        character['experience'] += 35
        character['inventory'].append('Magical Item')

