import random
import sys

def print_intro():
    print("""
    ~~~ Murloc's Stranglethorn Adventure ~~~
    You are a brave Murloc exploring the tropical coast of Stranglethorn.
    Face wild beasts, discover treasures, and make choices that shape your journey!
    """)

def get_choice(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        choice = input("Choose an option: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice) - 1
        print("Invalid choice. Try again.")

def combat(enemy, player_hp, player_attack, gold):
    enemy_hp = enemy['hp']
    print(f"A wild {enemy['name']} appears!")
    while enemy_hp > 0 and player_hp > 0:
        print(f"Your HP: {player_hp} | {enemy['name']} HP: {enemy_hp}")
        action = get_choice(["Attack", "Run"])
        if action == 0:
            dmg = random.randint(player_attack-1, player_attack+2)
            print(f"You hit the {enemy['name']} for {dmg} damage!")
            enemy_hp -= dmg
            if enemy_hp <= 0:
                print(f"You defeated the {enemy['name']}!")
                gold_reward = random.randint(2, 8)
                gold[0] += gold_reward
                print(f"You found {gold_reward} gold!")
                return True, player_hp
            enemy_dmg = random.randint(enemy['attack']-1, enemy['attack']+1)
            print(f"The {enemy['name']} hits you for {enemy_dmg} damage!")
            player_hp -= enemy_dmg
        else:
            if random.random() < 0.5:
                print("You escaped!")
                return False, player_hp
            else:
                print("You failed to escape!")
                enemy_dmg = random.randint(enemy['attack']-1, enemy['attack']+1)
                print(f"The {enemy['name']} hits you for {enemy_dmg} damage!")
                player_hp -= enemy_dmg
    if player_hp <= 0:
        print("You have been defeated...")
        sys.exit()
    return True, player_hp

def explore(player_hp, player_attack, inventory, gold):
    events = [
        ("You find a shiny shell on the beach.", lambda: inventory.append("Shiny Shell")),
        ("A wild Jungle Panther leaps from the bushes!", lambda: combat({'name': 'Jungle Panther', 'hp': 8, 'attack': 3}, player_hp, player_attack, gold)),
        ("You discover a hidden chest.", lambda: inventory.append("Gold Coin")),
        ("A giant crab blocks your path!", lambda: combat({'name': 'Giant Crab', 'hp': 10, 'attack': 2}, player_hp, player_attack, gold)),
        ("You rest under a palm tree and recover 2 HP.", lambda: min(player_hp+2, 12)),
    ]
    event, effect = random.choice(events)
    print(event)
    result = effect()
    if isinstance(result, tuple):
        _, player_hp = result
    elif isinstance(result, int):
        player_hp = result
    return player_hp

def main():
    print_intro()
    player_hp = 12
    player_attack = 3
    inventory = []
    gold = [10]  # Start with 10 gold
    while True:
        print(f"\nWhat will you do? (Gold: {gold[0]})")
        choice = get_choice([
            "Explore the coast",
            "Check inventory",
            "Rest",
            "End adventure"
        ])
        if choice == 0:
            player_hp = explore(player_hp, player_attack, inventory, gold)
        elif choice == 1:
            print("Inventory:", inventory if inventory else "(empty)")
            print(f"Gold: {gold[0]}")
        elif choice == 2:
            print("You rest and recover 3 HP.")
            player_hp = min(player_hp + 3, 12)
        else:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
