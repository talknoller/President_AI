class Card:
    def __init__(self, value, tie):
        self.value = value
        self.tie = tie

    def __str__(self):
        return str(self.value) + " " + self.tie

    def __eq__(self, other):
        return self.tie == other.tie and self.value == other.value
