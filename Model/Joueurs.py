import os
import json


class Joueurs:
    # Obtention du chemin relatif vers le répertoire "Data"
    data_folder = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, "Data")
    )
    file_path = os.path.join(data_folder, "Joueurs.json")

    @classmethod
    def _get_json_file(cls):
        # Vérification si le fichier n'est pas vide
        if os.path.getsize(cls.file_path) > 0:
            with open(cls.file_path, "r") as json_data:
                # Charger les données existantes
                return json.load(json_data)
        else:
            return []

    @classmethod
    def _write_json_file(cls, data):
        with open(cls.file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    def __init__(self, first_name, last_name, birth_date, id):
        # Initialisation des attributs de l'objet Joueurs
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.id = id

    def add_player(self):
        """Ajouter un nouveau joueur"""
        joueur = {
            "Nom": self.last_name,
            "Prenom": self.first_name,
            "Date naissance": self.birth_date,
            "ID": self.id,
        }

        data = Joueurs._get_json_file()

        # Vérification des doublons
        if any(el.get("ID") == joueur["ID"] for el in data):
            print("ID déjà existant")
        else:
            data.append(joueur)

        # Écrire les données dans le fichier JSON
        Joueurs._write_json_file(data)

    def get_player(self, id):
        """Récupérer les informations d'un joueur"""
        data = Joueurs._get_json_file()
        for el in data:
            # Parcourir la liste des éléments et vérifier si l'ID correspond
            if el["ID"] == id:
                return el

    def update_player(self, id, player_data):
        """Mettre à jour les informations d'un joueur"""
        data = Joueurs._get_json_file()

        for i, element in enumerate(data):
            # Parcourir la liste des éléments et vérifier si l'ID correspond
            if element["ID"] == id:
                data.pop(i)
                # Si l'ID correspond, supprimer l'élément correspondant
                data.append(player_data)
                # Ajouter l'élément mis à jour
                break

        # Écrire les données dans le fichier JSON
        Joueurs._write_json_file(data)


# Exemple d'utilisation de la classe Joueurs
player = Joueurs("Pop", "Alexandru", "08/11/1991", "AB5454ada")

update_inf = {
    "Nom": "Alexandru",
    "Prenom": "Pop",
    "Date naissance": "08/11/1991",
    "Turnois gagnee": 1,
    "ID": "AB5454a",
}
player.update_player("AB5454a", update_inf)
