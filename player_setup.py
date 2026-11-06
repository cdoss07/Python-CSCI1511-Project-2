"""
Project 2
NFL Player Stats Lookup
Christian Doss
11/5/2026
"""


class Player:
    def __init__(self, name, season_stats, weekly_stats):
        self.name = name
        self.season_stats = season_stats
        self.weekly_stats = weekly_stats

    def season_summary(self):
        summary = f'\n{self.name} 2026 Season Totals'

        for stats, value in self.season_stats.items():
            summary += f'\n{stats}: {value}'
        return summary


class WideReceiver(Player):
    def __init__(self, name, season_stats, weekly_stats):
        super().__init__(name, season_stats, weekly_stats)
        self.position = "Wide Receiver"

class TightEnd(Player):
    def __init__(self, name, season_stats, weekly_stats):
        super().__init__(name, season_stats, weekly_stats)
        self.position = "Tight End"