import random


class Tournois:
    def __init__(self, name, players):
        self.tournament_name = name
        self.players = players
        self.scores = {player: 0 for player in self.players}
        self.rounds_played = 0
        self.past_pairs = []

    def calculate_score(self, winner, loser, score):
        if loser != None:
            self.scores[winner] += score
            self.scores[loser] += 0
        else:
            self.scores[winner] += score

    def create_pairs(self):
        # Create random player pairs for the current round
        pairs = 0
        if self.rounds_played == 0:
            random.shuffle(self.players)
            if len(self.players) % 2 == 1:
                self.players.append(None)

            pairs = [
                (self.players[i], self.players[i + 1])
                for i in range(0, len(self.players), 2)
            ]
            self.past_pairs.append(pairs)
            self.have_played_before(self.players)

    def have_played_before(self, players):
        print(players)
        for pair in self.past_pairs:
            if pair in players:
                print(pair)
                print(" Au jucat impreuna")
            else:
                print(pair)
                print("nu au jucat deja impreuine")

        # for pair in pairs:
        #     if None in pair:
        #         self.calculate_score(pair[0], pair[1], 0.5)

        # # Verify if pairs have played before and calculate scores
        # for pair in pairs:
        #     if None in pair:
        #         if pair[0] == None:
        # self.calculate_score(pair[1], pair[0], 0.5)
        #         else:
        #             self.calculate_score(pair[0], pair[1], 0.5)
        #         continue
        #     if self.have_played_before(pair):
        #         continue
        #     winner, loser = self.calculate_winner(pair)
        #     self.calculate_score(winner, loser, 1)
        #     self.past_pairs.append(pair)
        # self.past_pairs.extend(pairs)
        # self.rounds_played += 1
        # self.players = [
        #     self.players[i]
        #     for i in range(len(self.players))
        #     if self.scores[self.players[i]] < self.rounds_played * 2
        # ]

    # def have_played_before(self, pair):
    #     if pair in self.past_pairs:
    #         return True
    #     if (pair[1], pair[0]) in self.past_pairs:
    #         return True
    #     return False

    # def calculate_winner(self, pair):
    #     return (pair[0], pair[1]) if random.choice([True, False]) else (pair[1], pair[0])

    # def get_winner(self):
    #     self.scores = [(player, score) for player, score in enumerate(self.scores)]
    #     self.scores.sort(key=lambda x: x[1], reverse=True)
    #     # print(self.scores[0])
    #     return self.scores[0]

    # # def play_round(self):
    # #     while len(self.players) > 1:
    # #         self.create_pairs()
    # #         self.scores = [(player, 0) for player in self.players]
    # #         self.scores = [0] * len(self.players)
    # #     return self.get_winner()[0]

    # def play_tournament(self):
    #     # self.play_round()
    #     self.players = [self.get_winner()[0]]
    #     self.scores = [0]
    #     return self.get_winner()

    # # def print_scores(self):
    # #     for player, score in self.scores:
    # #         print(f"{self.players[player]}: {score}")


turneu = Tournois(
    "paris_2023",
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
        "Dan",
    ],
)
# turneu.play_tournament()
turneu.create_pairs()
