"""
Project 2
NFL Player Stats Lookup
Christian Doss
11/5/2026
"""


nfl_players = {
    "Trey McBride": {
       "season stats": { "receptions": 26, "yards": 211, "touchdowns": 2  
       }, "weekly":[
            {"week": 1, "receptions": 9, "yards": 95, "touchdowns": 1},
            {"week": 2, "receptions": 8, "yards": 41, "touchdowns": 1},
            {"week": 3, "receptions": 9, "yards": 75, "touchdowns": 0}
       ]
    },
        "Jaxon Smith-Njigba": {
       "season stats": { "receptions": 27, "yards": 405, "touchdowns": 6  
       }, "weekly":[
            {"week": 1, "receptions": 8, "yards": 112, "touchdowns": 1},
            {"week": 2, "receptions": 9, "yards": 155, "touchdowns": 3},
            {"week": 3, "receptions": 10, "yards": 128, "touchdowns": 2}
       ]
    },
    "Puka Nacua": {
       "season stats": { "receptions": 5, "yards": 74, "touchdowns": 0 },
       "weekly":[
            {"week": 1, "receptions": 8, "yards": 74, "touchdowns": 0},
            {"week": 2, "receptions": 0, "yards": 0, "touchdowns": 0},
            {"week": 3, "receptions": 0, "yards": 0, "touchdowns": 0}
       ]
    },
    "Deebo Samuel": {
           "season stats": { "receptions": 5, "yards": 74, "touchdowns": 0 },
           "weekly":[
                {"week": 1, "receptions": 6, "yards": 48, "touchdowns": 1},
                {"week": 2, "receptions": 3, "yards": 31, "touchdowns": 0},
                {"week": 3, "receptions": 0, "yards": 80, "touchdowns": 1}
           ]
        }
}

search_history = []
app_name = "NFC West Wide Receiver Lookup Tool"

program_active = True

while program_active:
    print(f'\nWelcome to the {app_name}!\n Main Menu:\n 1). Look Up a Player\n 2). View Session Search History\n 3). Exit Program')

    choice = input("Enter your choice from the Menu!: ")

    if choice == "1":
        user_selection = input("\nPick from one of these NFC West Wide Receivers:\n Trey McBride, Jaxon Smith-Njigba, Puka Nacua, Deebo Samuel:  ")

        if user_selection in nfl_players:
            search_history.append(user_selection)
            print(f"\nDo you want to see the seasonal or weekly stats for {user_selection}?")
            stat_type = input("Type 'season' or 'weekly': ")

            if stat_type == "season":
                print(f"\n{user_selection} 2026 Season Totals")
                for stat, value in nfl_players[user_selection]["season stats"].items():
                    print(f"{stat}: {value}")

            elif stat_type == "weekly":
                print(f"\n{user_selection}'s Weekly Game Log")
                for game in nfl_players[user_selection]["weekly"]:
                    print(f"Week {game['week']}: {game['receptions']} rec, {game['yards']} yds, {game['touchdowns']} TD")

            else:
                print("INVALID CHOICE")
        
        else:
            print("Player not found")
    
    elif choice == "2":
        print("\nSearch History")
        if not search_history:
            print("You haven't search for any players yet.")
        
        else:
            for player in search_history:
                print(player)
    elif choice == "3":
        print("\nThanks for using the player lookup tool! Goodbye!")
        program_active = False

    else:
        print("Invalid Entry! Try again!")