import random


class Tournois:
    def __init__(self, tournament_name, round, players):
        self.tournament_name = tournament_name
        self.round = round
        self.players = players
        self.pairs_history = []

    @classmethod
    def tournament_management(cls, name, round, players):
        if round == 0:
            pass

    def set_pairs(self, players):
        pairs = []
        for i in range(0, len(players), 2):
            pairs.append([players[i], players[i + 1]]) if i + 1 < len(
                players
            ) else pairs.append([players[i], ""])
        self.pairs_history.append(pairs)

        self.define_winners(pairs)

    def define_winners(self, matches):
        winners = []
        losers = []
        nuls = []
        for match in matches:
            scores = [random.randint(0, 2) for _ in range(2)]
            print(match)
            if scores[0] > scores[1]:
                winners.append([match[0], 1])
                losers.append([match[1], 0])
            elif scores[1] > scores[0]:
                winners.append([match[1], 0])
                losers.append([match[0], 1])
            else:
                nuls.append([match[0], 0.5])
                nuls.append([match[1], 0.5])

        print(winners)
        print(" -------------")
        print(losers)
        print("-------------")
        print(nuls)


t = Tournois(
    "turnois_paris_2023",
    "0",
    [
        "Alice",
        "Bob",
        "Charlie",
        "Dave",
        "Eve",
        "Frank",
        "Grace",
        "Heidi",
        "Ivan",
        "Judy",
        "Kevin",
        "Linda",
        "Mike",
        "Nancy",
        "Oscar",
        "Patty",
        "Quentin",
        "Randy",
        "Sarah",
        "Tom",
    ],
)
t.set_pairs(
    [
        "Alice",
        "Bob",
        "Charlie",
        "Dave",
        "Eve",
        "Frank",
        "Grace",
        "Heidi",
        "Ivan",
        "Judy",
        "Kevin",
        "Linda",
        "Mike",
        "Nancy",
        "Oscar",
        "Patty",
        "Quentin",
        "Randy",
        "Sarah",
        "Tom",
        "Dany",
    ]
)
