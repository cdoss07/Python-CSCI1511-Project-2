"""
Project 2
NFL Player Stats Lookup
Christian Doss
11/5/2026
"""

class Menu:
    def __init__(self, players_stats):
        self.players_stats = players_stats
        self.search_history = []
        self.app_name = "NFC West Wide Receiver Lookup Tool"

    def display_menu(self):
        print(f'\nWelcome to the {self.app_name}!')
        print(f'Main Menu: ')
        print(f'1. Look Up a Player')
        print(f'2. View Session Search History')
        print(f'3. Exit Program')

    def run_lookup(self):
        print(f'Pick from one of these NFC West Wide Receivers: ')
        print(f'Trey McBride, Jaxon Smith-Njigba, Puka Nacua, Deebo Samuel:  ')

        user_selection = input("Enter your selection: ").strip()

        if user_selection in self.players_stats:
            player = self.players_stats[user_selection]
            self.search_history.append(player.name)

            print(f"\nDo you want to see the seasonal or weekly stats for {player.name}?")
            stat_type = input("Type 'season' or 'weekly': ").strip()

            if stat_type == 'season':
                print(player.season_stats())
        
            elif stat_type == "weekly":
                print(player.weekly_stats())

            else:
                print("INVALID CHOICE")

        else:
            print("Player not found")

    def view_history(self):
        print("\nSearch History")
        if not self.search_history:
            print("You haven't searched for any players yet")
        else:
            for player in self.search_history
            print(player)