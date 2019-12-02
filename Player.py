class Player:

    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.loses = 0

    def __str__(self):
        return f"name: {self.name}, wins: {self.wins}, loses: {self.loses}"
