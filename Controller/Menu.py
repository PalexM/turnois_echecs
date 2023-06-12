import sys

sys.path.append("..")
from Vue.Vues import Vues
from Controller.Tournois import Tournois as Turnois_Controller
from Controller.Joueurs import Joueurs
from Controller.Rapports import Rapports


class Menu:
    def __init__(self) -> None:
        self.vue = Vues()
        self.main_menu = {
            "1": "Creer un Tournois",
            "2": "Demarrer un Tournois",
            "3": "Ajouter un Joueur",
            "4": "Generer un Rapport",
        }
        self.sub_menu_rapport = {
            "1": "Liste de tous les joueurs par ordre alphabétique",
            "2": "Liste de tous les tournois",
            "3": "nom et dates d’un tournoi",
            "4": "Liste des joueurs du tournoi par ordre alphabétique",
            "5": "Liste de tous les tours du tournoi et de tous les matchs du tour",
        }

    def display_menu(self):
        self.vue.header()
        self.vue.menu(self.main_menu)

    def main_menu_interaction(self, error=""):
        choice = input(
            error
            if error != ""
            else "Veuillez sélectionner l'une des options ci-dessus : "
        )
        match choice:
            case "1":
                tournois = Turnois_Controller()
                tournois.create_new_tournament()
            case "2":
                tournois = Turnois_Controller()
                tournois.start_tournament()
            case "3":
                Joueurs().add_player()
            case "4":
                Rapports().main()
            case _:
                self.main_menu_interaction(
                    "L'option que vous avez saisie n'existe pas, réessayez: "
                )

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


if __name__ == "__main__":
    # Exemple d'utilisation de la classe Joueurs
    menu = Menu()
    menu.display_menu()
    menu.main_menu_interaction()
