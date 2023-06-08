import os
import json
import os

# from ..Vue.Vues import Vues
# # nom dossir , nom de fichier, nom de la classe


class Joueurs:
    """Class Joueurs, Methodes principales: Ajouter un nouveau joueur, Récupérer les informations d'un joueur, Mettre à jour les informations d'un joueur"""

    # Obtention du chemin relatif vers le répertoire "Data"
    data_folder = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, "Data")
    )
    file_path = os.path.join(data_folder, "Joueurs.json")

    def __init__(self, first_name, last_name, birth_date, id):
        """Initialisation des attributs de l'objet Joueurs"""
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.id = id

    @classmethod
    def _get_json_file(cls):
        """Recuperation du contenu du fichier json"""
        # Vérification si le fichier n'est pas vide
        if os.path.getsize(cls.file_path) > 0:
            with open(cls.file_path, "r") as json_data:
                # Charger les données existantes
                return json.load(json_data)
        else:
            return []

    @classmethod
    def _write_json_file(cls, data):
        """Ecrire les donnees dans le fichier JSON"""
        with open(cls.file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    def add_player(self):
        """Ajouter un nouveau joueur ou returne une expetion ValueError"""
        joueur = {
            "Nom": self.last_name,
            "Prenom": self.first_name,
            "Date naissance": self.birth_date,
            "ID": self.id,
            "Tournois Gagnee": 0,
            "Liste Tournois Gagnee": [],
            "Liste Tournois Participe": [],
        }

        data = Joueurs._get_json_file()

        # Vérification des doublons
        if any(el.get("ID") == joueur["ID"] for el in data):
            raise ValueError("Un joueur avec cet ID existe déjà.")
        else:
            data.append(joueur)

        # Écrire les données dans le fichier JSON
        Joueurs._write_json_file(data)

    def get_player(self, id):
        """Récupérer les informations d'un joueur, returne le joueur ou KeyError exception"""
        data = Joueurs._get_json_file()
        for el in data:
            # Parcourir la liste des éléments et vérifier si l'ID correspond
            if el["ID"] == id:
                return el
            else:
                raise KeyError("Ce Joueur n'est pas enregistré")

    @staticmethod
    def get_players():
        data = Joueurs._get_json_file()
        return data

    @staticmethod
    def update_player(id, score, tournmanent_name):
        """Mettre à jour les informations d'un joueur ou returne une exception KeyError"""
        data = Joueurs._get_json_file()
        for element in data:
            # Parcourir la liste des éléments et vérifier si l'ID correspond
            if element["ID"] == id:
                # Si l'ID correspond, supprimer l'élément correspondant
                if score < 1:
                    element["Tournois Gagnee"] += score
                    element["Liste Tournois Participe"].append(tournmanent_name)
                else:
                    element["Tournois Gagnee"] += score
                    element["Liste Tournois Gagnee"].append(tournmanent_name)
                    element["Liste Tournois Participe"].append(tournmanent_name)
                # Ajouter l'élément mis à jour
                break

        # Écrire les données dans le fichier JSON
        Joueurs._write_json_file(data)


# if __name__ == "__main__":
#     # Exemple d'utilisation de la classe Joueurs
#     player = Joueurs("Pop", "Alexandru", "08/11/1991", "AB5454ada")

#     update_inf = {
#         "Nom": "Alexandru",
#         "Prenom": "Pop",
#         "Date naissance": "08/11/1991",
#         "ID": "AB5454a",
#     }
#     player.get_players()
