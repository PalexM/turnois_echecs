from datetime import datetime
import sys

sys.path.append("..")
from Model.Joueurs import Joueurs
from Model.Tournois import Tournois as Tournois_Model
from Matchs import Match
from Vue.Vues import Vues

# def __init__(self, name, place, players, rounds=4, start_tournament=False):
#     self.name = name
#     self.place = place
#     self.rounds = rounds
#     self.players = players
#     self.start_tournament = start_tournament


class Tournois:
    def __init__(self):
        self.vue = Vues()

    def create_new_tournament(self):
        name = self.get_input("Nom Tournoi : ")
        place = self.get_input("Emplacement Tournoi : ")
        all_players = Joueurs.get_players()
        while True:
            rounds = int(input("Nombre de Tours  (min 4): "))
            if rounds >= 4:
                break

        selected_players = self.select_players_for_tournament(all_players)
        while True:
            start_tournament = input(
                "Voulez-vous commencer le tournoi maintenant ? Oui / Non   : "
            )
            if (
                start_tournament.lower().strip() == "oui"
                or start_tournament.lower().strip() == "non"
            ):
                break

        try:
            new_tournament = Tournois_Model(
                name, place, selected_players, rounds, start_tournament
            )
            new_tournament.add_tournament()
            print(self.vue.color_green("\n   Le tournoi a été crée avec succès   \n"))
            if start_tournament == "oui":
                print(
                    self.vue.color_green(
                        f"\n   Le tournoi  {name} vient de commencer!   \n"
                    )
                )
                start_tournament = Match(
                    name,
                    selected_players,
                    rounds,
                )
                self.tournament_results(start_tournament.play_tournament())
        except ValueError as e:
            print("Erreur:", self.vue.color_red(str(e)))

    def start_tournament(self):
        tournaments = Tournois_Model.get_tournaments()
        non_started_tournaments = [
            tournament["Nom"]
            for tournament in tournaments
            if tournament["Debut"] == "non"
        ]
        if len(non_started_tournaments) <= 0:
            pass
        else:
            while True:
                self.list_options(
                    "Sélectionnez un tournoi pour commencer", non_started_tournaments
                )
                start_tournament = int(input())
                if 0 <= start_tournament < len(non_started_tournaments):
                    break
        tournament_data = Tournois_Model.get_tournament(
            non_started_tournaments[start_tournament]
        )
        start_tournament = Match(
            tournament_data.get("Nom"),
            tournament_data.get("Joueurs"),
            tournament_data.get("Tours depart"),
        )

        self.tournament_results(start_tournament.play_tournament())

    def tournament_results(self, results):
        players = dict(player for player in results.get("infos").items())
        for player in players.items():
            if player[1].get("winner"):
                winner = player[0]
                Joueurs.update_player(player[0], 1, results["tournament_name"])
            else:
                Joueurs.update_player(player[0], 0, results["tournament_name"])
        tournament_name = results['tournament_name']
        data = {
            'winner': results['winner'],
            'rounds' : results['tournament_rounds'],
            'infos' : results["infos"],
            'start_date' : results['start_time'],
            'end_date' : results['end_time'],
        }
        Tournois_Model.update_tournament(tournament_name, data)

        # print(
        #     self.vue.color_blue("Le Tournoi "),
        #     self.vue.color_green(results["tournament_name"]),
        #     self.vue.color_blue(" vient d'etre remportee par "),
        #     self.vue.color_green(winner),
        # )

    def select_players_for_tournament(self, player_data):
        selected_players = []
        all_players = [
            f" {player.get('Nom')} {player.get('Prenom')} ID :{player.get('ID')}"
            for player in player_data
        ]
        while True:
            self.list_options("Choisissez les joueurs", all_players)
            selected = input(
                "Veuillez sélectionner un joueur, pour quitter sélectionner x : "
            )
            if selected == "x" or len(all_players) < 1:
                break
            else:
                try:
                    selected = int(selected)
                    selected_players.append(all_players[selected])
                    all_players.pop(selected)
                    self.list_options(
                        "Joueurs sélectionnés jusqu'à présent :", selected_players
                    )
                except IndexError:
                    print(
                        "Erreur, le joueur n'existe pas, veuillez en sélectionner un autre."
                    )
                except ValueError:
                    print("Erreur, veuillez entrer un nombre valide ou x pour quitter.")
        return [player.split(":")[1] for player in selected_players]

    def get_input(self, text):
        while True:
            var = input(text)
            if len(var) > 0:
                return var

    def list_options(self, title, options):
        print(f"\n\n \t\t\t {self.vue.color_yellow(title)}       \n\n ")
        option = ""
        for index, element in enumerate(options):
            while (
                len(element) <= 20
            ):  #  égalisation des longueurs de texte pour l'esthétique et la mise en page
                element += " "

            if index % 5 == 4:  # creer 5 colones pour la mise en page
                option += f" {self.vue.color_yellow(str(index))}) {self.vue.color_blue(element)}      "
            else:
                option += f" {self.vue.color_yellow(str(index))}) {self.vue.color_blue(element)}      "
        option += " \n\n"
        print(option)


# turneu = Tournois(
#     "paris_2023",
#     [
#         "Alice",
#         "Bob",
#         "Charlie",
#         "Dave",
# "Eve",
# "Frank",
# "Grace",
# "Heidi",
# "Ivan",
# "Judy",
# "Kevin",
# "Linda",
# "Mike",
# "Nancy",
# "Oscar",
# "Patty",
# "Quentin",
# "Randy",
# "Sarah",
# "Tom",
# "Dan",
#     ],
# )
# turneu.play_tournament()
# print(f"date debut : {turneu.start_time}\n")
# print(f"date fin : {turneu.end_time} \n")
# print(f"Tours: {turneu.rounds} \n")
# print(turneu.player_inf)
# turneu.list_players_for_tournament()
