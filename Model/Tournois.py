import os
import json
import re


class Tournois:
    """A Class Tournois, Methodes principales: Creer un tournois, Récupérer les informations d'un tournois, Mettre à jour les informations d'un tournois"""

    # Obtention du chemin relatif vers le répertoire "Data"
    data_folder = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, "Data")
    )
    file_path = os.path.join(data_folder, "Tournois.json")

    @classmethod
    def _get_json_file(cls):
        """Recuperation du contenu du fichier json"""
        # Vérification si le fichier n'est pas vide
        if os.path.getsize(cls.file_path) > 0:
            with open(cls.file_path, "r", encoding="utf-8") as json_data:
                # Charger les données existantes
                return json.load(json_data)
        else:
            return []

    @classmethod
    def _write_json_file(cls, data):
        """Ecrire les donnees dans le fichier JSON"""
        with open(cls.file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    def __init__(self, name, place, players, rounds=4, start_tournament=False):
        self.name = name
        self.place = place
        self.rounds = rounds
        self.players = players
        self.start_tournament = start_tournament

    def __str__(self):
        if self.start_tournament:
            return f"Le tournoi {self.name} vient de commencer"
        else:
            return f"Le tournoi {self.name} vient d'être créé"

    def add_tournament(self):
        """Ajouter un nouveau tournois ou returne une expetion ValueError"""
        turnois = {
            "Nom": self.name,
            "Lieu": self.place,
            "Tours depart": self.rounds,
            "Joueurs": self.players,
            "Debut": self.start_tournament,
        }

        data = Tournois._get_json_file()

        # Vérification des doublons
        if any(
            re.sub(r"[^a-zA-Z0-9]", "", el.get("Nom").lower())
            == re.sub(r"[^a-zA-Z0-9]", "", turnois["Nom"].lower())
            for el in data
        ):
            raise ValueError("Un Tournois existe deja avec ce nom!")
        else:
            data.append(turnois)

        Tournois._write_json_file(data)

    @staticmethod
    def get_tournament(tournament_name):
        """Récupérer les informations d'un tournois, returne le turnois ou KeyError exception"""
        data = Tournois._get_json_file()
        for element in data:
            if isinstance(element, dict):
                if "Nom" in element and element["Nom"] == tournament_name:
                    return element
            else:
                print("Le tournois n'existe pas")

    @staticmethod
    def get_tournaments():
        data = Tournois._get_json_file()
        return data

    @staticmethod
    def update_tournament(tournament_name, tournament_data):
        """Mettre à jour les informations d'un joueur ou returne une exception KeyError"""
        data = Tournois._get_json_file()

        for i, element in enumerate(data):
            if re.sub(r"[^a-zA-Z0-9]", "", element["Nom"]) == tournament_name:
                element["Gagnant"] = tournament_data["winner"]
                element["Rounds"] = tournament_data["rounds"]
                element["Infos"] = tournament_data["infos"]
                element["Debut Tournoi"] = tournament_data["start_date"]
                element["Fin Tournoi"] = tournament_data["end_date"]
                element["Debut"] = "oui"

                # Ajouter l'élément mis à jour
                break
        Tournois._write_json_file(data)
