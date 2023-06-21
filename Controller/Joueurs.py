from Model.Joueurs import Joueurs as Joueurs_Model
from Vue.Vues import Vues
import sys
import re

sys.path.append("..")


class Joueurs:
    """Class Joueurs, gestion des joueurs"""

    def __init__(self) -> None:
        self.vue = Vues()

    def list_players(self):
        players = Joueurs_Model.get_players()
        players = [
            f"{player.get('Nom')} {player.get('Prenom')} ID:{player.get('ID')}"
            for player in players
        ]
        return players

    def add_player(self):
        last_name = self.get_input("Nom : ")
        first_name = self.get_input("Prenom : ")
        while True:
            birth_date = input("Date naissance , format dd/mm/yyyy : ").strip()
            pattern = r"\d{2}/\d{2}/\d{4}"
            if re.match(pattern, birth_date):
                break

        while True:
            id = input("Identifiant national d'échecs : ").strip()
            pattern = r"^[A-Za-z]{2}\d{5}$"

            if re.match(pattern, id):
                break

        try:
            new_player = Joueurs_Model(first_name, last_name, birth_date, id)
            new_player.add_player()
            print(self.vue.color_green("\nLe joueur a été ajouté avec succès"))
        except ValueError as e:
            print("Erreur:", self.vue.color_red(str(e)))

    def update_player(self, id):
        pass

    def update_players(self):
        pass

    def get_input(self, text):
        while True:
            var = input(text).strip()
            if len(var) > 0:
                return var
