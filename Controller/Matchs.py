import random
from datetime import datetime


class Match:
    """Class Matchs, gestion des matchs du turnois"""

    def __init__(self, tournament_name, players, minumum_rounds=4):
        self.tournament_name = tournament_name
        self.players = players
        self.start_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S:%f")
        self.end_time = ""
        self.actual_round = 0
        self.minumum_rounds = minumum_rounds
        self.winner_is = ""
        self.rounds = {self.actual_round: {"pairs": [], "wait_list": ""}}
        self.wait_list = ""
        self.wait_room = []
        self.player_inf = {
            player: {
                "score": 0,
                "adversary": [],
                "eliminated": False,
                "winner": False,
                "rounds_played": 0,
            }
            for player in self.players
        }

    def pairs_generation(self):
        pairs, new_pairs, players, non_valid_pairs = [], [], {}, []
        # On trie les joueurs par score et on les ajoute à la liste pairs s'ils ne sont pas éliminés
        for player in sorted(
            self.player_inf.items(), key=lambda x: x[1]["score"], reverse=True
        ):
            if not player[1]["eliminated"]:
                pairs.append(player[0])

        if len(pairs) % 2 == 1:
            while True:
                random_index = random.randrange(len(pairs))
                self.wait_list = pairs.pop(random_index)
                if self.wait_list is not self.wait_room:
                    self.wait_room.append(self.wait_list)
                    break

        for i in range(0, len(pairs), 2):
            if i + 1 < len(pairs):
                if pairs[i] not in self.player_inf[pairs[i + 1]]["adversary"]:
                    new_pairs.append((pairs[i], pairs[i + 1]))
                    players[pairs[i]] = {
                        "rounds_played": 1,
                        "adversary": pairs[i + 1],
                    }
                    players[pairs[i + 1]] = {
                        "rounds_played": 1,
                        "adversary": pairs[i],
                    }
                else:
                    non_valid_pairs.append((pairs[i], pairs[i + 1]))

        # On met à jour les informations des joueurs avec les nouvelles paires générées
        self.update_player_infos(players)
        # Si des paires non valides ont été détectées, on réorganise les paires
        if non_valid_pairs:
            new_pairs = self.reorganise_pairs(non_valid_pairs)
        # On calcule les gagnants de chaque paire
        if len(new_pairs) == 0:
            return
        self.calculate_winners(new_pairs)
        self.rounds.update(
            {
                self.actual_round: {
                    "pairs": new_pairs,
                    "wait_list": self.wait_list,
                }
            }
        )
        self.actual_round += 1
        self.wait_list = ""

    def reorganise_pairs(self, pairs):
        new_pairs = []
        # On échange les adversaires des joueurs non valides pour rendre les paires valides
        if len(pairs) > 2:
            for i in range(0, len(pairs), 2):
                if i + 1 < len(pairs):
                    new_pairs.append((pairs[i][0], pairs[i + 1][1]))
                    new_pairs.append((pairs[i + 1][0], pairs[i][1]))
            return new_pairs
        else:
            return pairs

    def update_player_infos(self, data):
        params = {
            "score",
            "adversary",
            "eliminated",
            "tournament_name",
            "winner",
            "rounds_played",
        }

        for key, val in data.items():
            for param in params:
                if param in val:
                    # Si le paramètre est le score ou le nombre de tours joués, on l'ajoute au score existant du joueur
                    if param == "score" or param == "rounds_played":
                        self.player_inf[key][param] += val[param]
                    # Si le paramètre est le statut de vainqueur ou éliminé, on le met à jour
                    elif param == "winner" or param == "eliminated":
                        self.player_inf[key][param] = val[param]
                    # Si le paramètre est le adversaire, on ajoute le nouvel adversaire à la liste
                    elif param == "adversary":
                        self.player_inf[key][param].append(val[param])

    def calculate_winners(self, pairs):
        winners, losers, nulls = [], [], []
        # Pour chaque paire, on tire au hasard un nombre pour déterminer le gagnant
        for pair in pairs:
            rdm = random.random()
            if rdm < 1 / 3:
                nulls.append(pair[0])
                nulls.append(pair[1])
            elif rdm < 2 / 3:
                winners.append(pair[0])
                losers.append(pair[1])
            else:
                winners.append(pair[1])
                losers.append(pair[0])
        # On transforme les listes de paires en listes de joueurs

        if len(pairs) <= 1 and len(winners) <= 1 and self.wait_list == "":
            if len(nulls) != 0:
                self.prepare_players_infos(winners, losers, nulls)
            else:
                self.design_winner(winners, losers)
        else:
            self.prepare_players_infos(winners, losers, nulls)

    def prepare_players_infos(self, winners, losers, nulls):
        player = {}

        # Les gagnants ont un score de 1, les perdants sont éliminés et ont un score de 0,  les nulls ont un score de 0,5
        for winner in winners:
            player[winner] = {"score": 1}
        for loser in losers:
            if int(self.actual_round) >= int(self.minumum_rounds):
                player[loser] = {"score": 0, "eliminated": True}
            else:
                player[loser] = {"score": 0}
        for null in nulls:
            player[null] = {"score": 0.5}

        self.update_player_infos(player)

    def design_winner(self, winner, loser):
        player = {}
        # Les gagnants ont un score de 1, les perdants sont éliminés et ont un score de 0,  les nulls ont un score de 0,5
        for w in winner:
            player[w] = {"score": 1, "winner": True}
            self.winner_is = w
        for los in loser:
            player[los] = {"score": 0, "eliminated": True}
        self.update_player_infos(player)
        self.end_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S:%f")

    def play_tournament(self):
        while True:
            for player in self.player_inf:
                if self.player_inf[player]["winner"]:
                    return {
                        "winner": player,
                        "tournament_name": self.tournament_name,
                        "tournament_rounds": self.rounds,
                        "infos": self.player_inf,
                        "start_time": self.start_time,
                        "end_time": self.end_time,
                    }
                else:
                    self.pairs_generation()
