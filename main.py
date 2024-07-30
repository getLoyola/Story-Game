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
