import os
import sys

sys.path.append("..")
from Model.Joueurs import Joueurs
from Model.Tournois import Tournois
from Vue.Vues import Vues

from Model.Joueurs import Joueurs


# RAPPORTS
# Nous aimerions pouvoir afficher les rapports suivants dans le programme :
# ● liste de tous les joueurs par ordre alphabétique ;
# ● liste de tous les tournois ;
# ● nom et dates d’un tournoi donné ;
# ● liste des joueurs du tournoi par ordre alphabétique ;
# ● liste de tous les tours du tournoi et de tous les matchs du tour.


class Rapports:
    def __init__(self):
        self.vue = Vues()
        # Obtention du chemin relatif vers le répertoire "Repports"
        self.data_folder = os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.pardir, "Data")
        )

    def main(self, error=""):
        self.list_options(
            "Rapports",
            [
                "Liste de tous les joueurs par ordre alphabétique",
                "Liste de tous les tournois",
                "Nom et dates d’un tournoi",
                "Liste des joueurs du tournoi par ordre alphabétique",
                "Liste de tous les tours du tournoi et de tous les matchs du tour",
            ],
        )
        choice = input(
            error
            if error != ""
            else "Veuillez sélectionner l'une des options ci-dessus : "
        )

        match choice:
            case "0":
                Rapports().get_players()
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case _:
                self.main("L'option que vous avez saisie n'existe pas, réessayez: ")

    def get_players(self):
        players = Joueurs.get_players()
        players.sort(key=lambda x: x["Nom"])
        data = ""
        for player in players:
            data += "\n ---------------------- \n"
            data += f"Nom : {player['Nom']}, Prenom : {player['Prenom']}"

        self.save_rapport("players_list", data)

    def get_tournaments(self):
        pass

    def get_tournament_by_name(self, tournament_name):
        pass

    def get_players_from_tournament(self, tournament_name):
        pass

    def get_toutnament_infos(self, tournament_name):
        pass

    def save_rapport(self, name, data):
        file_path = os.path.join(self.data_folder, name + ".txt")
        with open(file_path, "w") as f:
            f.write(data)

    def list_options(self, title, options):
        print(f"\n\n \t\t\t {self.vue.color_yellow(title)}       \n\n ")
        option = ""
        for index, element in enumerate(options):
            while (
                len(element) <= 20
            ):  #  égalisation des longueurs de texte pour l'esthétique et la mise en page
                element += " "

            if index % 5 == 4:  # creer 5 colones pour la mise en page
                option += f" {self.vue.color_yellow(str(index))}){self.vue.color_blue(element)}      "
            else:
                option += f" {self.vue.color_yellow(str(index))}){self.vue.color_blue(element)}      "
        option += " \n\n"
        print(option)
