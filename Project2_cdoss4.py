"""
Project 2
NFL Player Stats Lookup
Christian Doss
11/5/2026
"""
import sys
from menu import Menu
from player_data import nfl_players
from player_setup import Player
from player_records import Records

def main():
    records = Records(nfl_players)

    try:
        player_stats = records.player_records()

    except Exception as e:
        print(f"INVALID OPTION: {e}")
        sys.exit(1)

    menu = Menu(player_stats)

    while True:
        menu.display_menu()
        choice = input("Select an option from the Menu!:")

        if choice == "1":
            menu.run_lookup()
        elif choice == "2":
            menu.view_history()
        elif choice == "3":
            print("\nThanks for using the player lookup tool! Goodbye!")
            break
        else:
            print("Invalid Entry! Try again!")

if __name__ == "__main__":
    main()