"""
Project 2
NFL Player Stats Lookup
Christian Doss
11/5/2026
"""

from player_setup import WideReceiver, TightEnd

class Records:
    def __init__(self, dict):
        self.dict = dict

    def player_records(self):
        stats = {}

        for name, data in self.dict.items():
            try:
                season_stats = data["season stats"]
                weekly_stats = data["weekly"]

                if name == "Trey McBride":
                    stats[name] =TightEnd(name, season_stats, weekly_stats)
                else:
                    stats[name] = WideReceiver(name, season_stats, weekly_stats)

            except (KeyError, TypeError) as error:
                print(f"Error loading stats for {name}")
                continue
        return stats