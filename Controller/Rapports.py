from Model.Joueurs import Joueurs
from Model.Tournois import Tournois as Turnois_Model
from Vue.Vues import Vues
import os
import sys

sys.path.append("..")


class Rapports:
    """Classe Rapports, gestion et creation des rapports"""

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
                self.get_players()
            case "1":
                self.get_tournaments()
            case "2":
                self.get_tournament_by_name()
            case "3":
                self.get_players_from_tournament()
            case "4":
                self.get_toutnament_infos()
            case _:
                self.main("L'option que vous avez saisie n'existe pas, réessayez: ")

    def get_players(self):
        players = Joueurs.get_players()
        players.sort(key=lambda x: x["Nom"])
        data = "Liste des Joueurs"
        for player in players:
            data += "\n ---------------------- \n"
            data += f"Nom    : {player['Nom']}\nPrenom : {player['Prenom']}"

        self.save_rapport("players_list", data)

    def get_tournaments(self):
        tournamens = Turnois_Model.get_tournaments()
        data = "Liste des Tournois"
        for turnament in tournamens:
            data += "\n ---------------------- \n"
            data += f"Nom : {turnament['Nom']}"
        self.save_rapport("tournaments_list", data)

    def get_tournament_by_name(self):
        selected = self.select_tournament()
        tournament = Turnois_Model.get_tournament(selected)
        data = f"""
----------------------------------------
Tournois {selected}
----------------------------------------
    
    Date Debut {tournament['Debut Tournoi']}
    Date Fin {tournament['Fin Tournoi']}
    """
        self.save_rapport(f"tournament_{selected}", data)

    def get_players_from_tournament(self):
        selected = self.select_tournament()
        tournament = Turnois_Model.get_tournament(selected)
        data = f"Liste Joueurs pour tournois {selected}\n\n"
        for player in tournament["Joueurs"]:
            data += f"    {player}\n"
        self.save_rapport(f"tournament_{selected}_players", data)

    def get_toutnament_infos(self):
        selected = self.select_tournament()
        tournament = Turnois_Model.get_tournament(selected)
        data = f"Informations Tournois {selected} \n\n"

        for round_number, round_info in tournament["Rounds"].items():
            data += f"    Tour : {round_number}\n"
            pairs = round_info["pairs"]
            for pair in pairs:
                data += f"        Paires : {pair[0]} et {pair[1]}\n"
            wait_list = round_info["wait_list"]
            if wait_list:
                data += f"        Liste d'attente : {wait_list}\n"

        for player, info in tournament["Infos"].items():
            data += f"\n    Joueur : {player}:\n"
            data += f"        Score : {info['score']}\n"
            data += f"        Adversaires : {info['adversary']}\n"
            data += f"        Elimine : {'oui' if info['eliminated'] else 'non'}\n"
            data += f"        Gagnant : {'oui' if info['winner'] else 'non'}\n"
            data += f"        Tours Joue : {info['rounds_played']}\n"
        self.save_rapport(f"tournament_{selected}_infos", data)

    def save_rapport(self, name, data):
        file_path = os.path.join(self.data_folder, name + ".txt")
        with open(file_path, "w") as f:
            f.write(data)
        print(self.vue.color_green(f"Le Rapport a ete genere dans : '{file_path}'"))

    def select_tournament(self):
        tournament_list = [
            tournament["Nom"] for tournament in Turnois_Model.get_tournaments()
        ]
        self.list_options("Veuillez sélectionner un tournoi", tournament_list)
        select = int(input(""))
        return tournament_list[select]

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
