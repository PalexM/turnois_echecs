import random


class Tournois:
    def __init__(self, tournament_name, players):
        self.tournament_name = tournament_name
        self.players = players
        self.rounds = 0
        self.player_inf = {
            player: {
                "score": 0,
                "adversary": [],
                "eliminated": False,
                "tournament_name": self.tournament_name,
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
            if player[1]["eliminated"] is not True:
                pairs.append(player[0])
        # Si la liste pairs contient un nombre impair de joueurs, on retire un joueur au hasard
        if len(pairs) % 2 == 1:
            random_index = random.randrange(len(pairs))
            removed_player = pairs.pop(random_index)
        # On génère les paires en s'assurant que chaque joueur joue contre un adversaire qu'il n'a pas encore affronté
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
                    non_valid_pairs.append(pairs[i], pairs[i + 1])

        # On met à jour les informations des joueurs avec les nouvelles paires générées
        self.update_player_infos(players)
        # Si des paires non valides ont été détectées, on réorganise les paires
        if len(non_valid_pairs) > 0:
            self.reorganise_pairs()

        # On calcule les gagnants de chaque paire
        self.calculate_winners(new_pairs)

    def reorganise_pairs(self, pairs):
        new_pairs = []
        # On échange les adversaires des joueurs non valides pour rendre les paires valides
        for i in range(0, len(pairs), 2):
            if i + 1 < len(pairs):
                new_pairs.append((pairs[i][0], pairs[i + 1][1]))
                new_pairs.append((pairs[i + 1][0], pairs[i][1]))
        return new_pairs

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
                    # Si le paramètre est les adversaires, on ajoute le nouvel adversaire à la liste
                    elif param == "adversary":
                        self.player_inf[key][param].append(val[param])

    def calculate_winners(self, pairs):
        winners, losers, nulls = [], [], []
        # Pour chaque paire, on tire au hasard un nombre pour déterminer le gagnant
        for i in range(0, len(pairs), 2):
            if random.random() < 1 / 3:
                nulls.append(pairs[i])
                nulls.append(pairs[i + 1])
            elif random.random() < 2 / 3:
                winners.append(pairs[i])
                losers.append(pairs[i + 1])
            else:
                winners.append(pairs[i + 1])
                losers.append(pairs[i])

        # On transforme les listes de paires en listes de joueurs
        winners = [w for winner in winners for w in winner]
        losers = [l for loser in losers for l in loser]
        nulls = [n for null in nulls for n in null]

        # On prépare les informations des joueurs pour le prochain tour
        self.prepare_players_infos(winners, losers, nulls)

    def prepare_players_infos(self, winners, losers, nulls):
        player = {}

        # Les gagnants ont un score de 1, les perdants sont éliminés et ont un score de 0,  les nulls ont un score de 0,5
        for winner in winners:
            player[winner] = {"score": 1}
        for loser in losers:
            player[loser] = {"score": 0, "eliminated": True}
        for null in nulls:
            player[null] = {"score": 0.5}

        # On met à jour les informations des joueurs avec les résultats du tour
        self.update_player_infos(player)

        print(self.player_inf)


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
turneu.pairs_generation()
