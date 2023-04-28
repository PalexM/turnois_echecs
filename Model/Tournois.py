import os
import json
import re


class Tournois:
    """Class Tournois, Methodes principales: Creer un tournois, Récupérer les informations d'un tournois, Mettre à jour les informations d'un tournois"""

    # Obtention du chemin relatif vers le répertoire "Data"
    data_folder = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, "Data/Tournois")
    )

    @classmethod
    def _create_json_file(cls, name, data):
        file_path = os.path.join(cls.data_folder, name + ".json")
        # Verifier si un turnois existe deja
        if os.path.exists(file_path):
            raise ValueError("Un tournois existe deja avec ce nom")
        # Creer le fichier et ecrire les donnees
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    @classmethod
    def _get_json_file(cls, file_name):
        """Recuperation du contenu du fichier json"""
        file_path = os.path.join(cls.data_folder, file_name + ".json")
        # Vérification si le fichier n'est pas vide
        if os.path.getsize(file_path) > 0:
            with open(file_path, "r", encoding="utf-8") as json_data:
                # Charger les données existantes
                return json.load(json_data)
        else:
            return []

    @classmethod
    def _write_json_file(cls, file_name, data):
        """Ecrire les donnees dans le fichier JSON"""
        file_path = os.path.join(cls.data_folder, file_name + ".json")
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    def __init__(
        self,
        name,
        place,
        start_date,
        end_date,
        players,
        infos_turnament,
        rounds=4,
    ):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.players = players
        self.infos_turnament = infos_turnament

    def add_turnament(self):
        """Ajouter un nouveau tournois ou returne une expetion ValueError"""
        actual_round = 0
        turnois = {
            "Nom": self.name,
            "Lieu": self.place,
            "Date debut": self.start_date,
            "Date fin": self.end_date,
            "Tours depart": self.rounds,
            "Tour Actuel": actual_round,
            "Joueurs": self.players,
            "Informations turnois": self.infos_turnament,
        }

        data_file_name = re.sub(r"[^a-zA-Z0-9]", "", self.name)
        Tournois._create_json_file(data_file_name, turnois)

    def get_turnament(self, turnament_name):
        """Récupérer les informations d'un tournois, returne le turnois ou KeyError exception"""
        data = Tournois._get_json_file(turnament_name)

        for el in data:
            # Parcourir la liste des éléments et vérifier si l'ID correspond
            if re.sub(r"[^a-zA-Z0-9]", "", el.get("Nom").lower()) == re.sub(
                r"[^a-zA-Z0-9]", "", turnament_name.lower()
            ):
                return el
            else:
                raise KeyError("Ce Tournois n'est pas enregistré")

    def update_turnament(self, turnament_name, turnament_data):
        """Mettre à jour les informations d'un joueur ou returne une exception KeyError"""
        data = Tournois._get_json_file(turnament_name)

        for i, element in enumerate(data):
            # Parcourir la liste des éléments et vérifier si l'ID correspond
            if re.sub(r"[^a-zA-Z0-9]", "", element["Nom"]) == turnament_name:
                data.pop(i)
                # Si l'ID correspond, supprimer l'élément correspondant
                data.append(turnament_data)
                # Ajouter l'élément mis à jour
                break
            else:
                raise KeyError("Ce Tournois n'est pas enregistré")

        # Écrire les données dans le fichier JSON
        Tournois._write_json_file(data)


my_tournament = Tournois(
    name="Paris 2023",
    place="Paris",
    start_date="2023-05-01",
    end_date="2023-05-08",
    rounds=6,
    players=["toto", "tata"],
    infos_turnament={
        "Lorem": "Lorem ipsum dolor sit amet.",
        "Integer": "Integer accumsan dui.",
        "Pellentesque": "Pellentesque eget enim ut nibh.",
        "Vestibulum": "Vestibulum sagittis tellus.",
        "Fusce": "Fusce eu lectus id ante.",
        "Cras": "Cras semper enim a ex venenatis.",
        "Aliquam": "Aliquam erat volutpat.",
        "Maecenas": "Maecenas auctor turpis.",
        "Morbi": "Morbi euismod nisl.",
        "Nulla": "Nulla eu tellus efficitur.",
    },
)
my_tournament.add_turnament()
# my_tournament.add_turnament()

# print(my_tournament.get_turnament("tournois1"))

# my_tournament.update_turnament(
#     "tournois1",
#     {
#         "Nom": "tournois1",
#         "Lieu": "Paris",
#         "Date debut": "2023-05-01",
#         "Date fin": "2023-05-08",
#         "Tours depart": 6,
#         "Tour Actuel": 1,
#         "Joueurs": ["toto", "tata"],
#         "Informations turnois": {
#             "Lorem": "Lorem ipsum dolor sit amet.",
#             "Integer": "Integer accumsan dui.",
#             "Pellentesque": "Pellentesque eget enim ut nibh.",
#             "Vestibulum": "Vestibulum sagittis tellus.",
#             "Fusce": "Fusce eu lectus id ante.",
#             "Cras": "Cras semper enim a ex venenatis.",
#             "Aliquam": "Aliquam erat volutpat.",
#             "Maecenas": "Maecenas auctor turpis.",
#             "Morbi": "Morbi euismod nisl.",
#             "Nulla": "Nulla eu tellus efficitur.",
#         },
#     },
# )
