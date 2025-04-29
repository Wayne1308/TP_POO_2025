from character import Warrior, Magician, Weapon
import random
import time

# Initialisation des combattants
fighters = [
    Warrior("Thor", Weapon("Hammer", 3.0)),
    Magician("Gandalf"),
    Magician("Merlin"),
    Warrior("Gimli", Weapon("Axe", 4.0))
]

# Fonction de simulation du combat
def fight_simulation(fighters):
    round_count = 1
    while True:
        alive_fighters = [f for f in fighters if not f.is_dead]

        if len(alive_fighters) <= 1:
            break

        print(f"\n--- Round {round_count} ---")
        random.shuffle(alive_fighters)

        for attacker in alive_fighters:
            if attacker.is_dead:
                continue

            # Toutes les cibles sauf lui-même et mortes
            targets = [f for f in alive_fighters if f != attacker and not f.is_dead]
            for target in targets:
                print(f"{attacker.name} attacks {target.name}!")
                attacker.attack(target)
                print(f"{target}")
                time.sleep(0.5)

        round_count += 1

    print("\n--- Fin du combat ---")
    for f in fighters:
        print(f)

    winner = [f for f in fighters if not f.is_dead]
    if len(winner) == 1:
        print(f"\nLe gagnant est : {winner[0].name}!")
    else:
        print("\nTous les combattants sont morts ou match nul.")


if __name__ == "__main__":
    fight_simulation(fighters) 