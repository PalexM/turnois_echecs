from colorama import Fore, Style
import datetime


class Vues:
    """TEST"""

    def __init__(self):
        self.reset = Style.RESET_ALL
        self.switch = {
            "info": Fore.BLUE,
            "danger": Fore.YELLOW,
            "error": Fore.RED,
            "validation": Fore.GREEN,
        }

    def get_color(self, type):
        if type in self.switch:
            return self.switch[type]

    def header(self):
        now = datetime.datetime.now()
        print(
            Fore.BLUE
            + """
                                                               .::.
                                            _()_       _::_
                                  _O      _/____\_   _/____\_
           _  _  _     ^^__      / //\    \      /   \      /
          | || || |   /  - \_   {     }    \____/     \____/
          |_______| <|    __<    \___/     (____)     (____)
    _     \__ ___ / <|    \      (___)      |  |       |  |
   (_)     |___|_|  <|     \      |_|       |__|       |__|
  (___)    |_|___|  <|______\    /   \     /    \     /    \\
  _|_|_    |___|_|   _|____|_   (_____)   (______)   (______)
 (_____)  (_______) (________) (_______) (________) (________)
 /_____\  /_______\ /________\ /_______\ /________\ /________\\
                                             
                                             __Centre échecs """
            + Fore.YELLOW
            + str(now.date())
            + self.reset,
            Fore.BLUE + "__\n" + self.reset,
        )

    def select_menu(self, menu: dict):
        menu_text = "      ".join(
            [
                self.color_danger(key + ")") + " " + self.color_info(value)
                for key, value in menu.items()
            ]
        )
        return "\n" + menu_text + "\n\n"

    def color_info(self, str):
        return Fore.BLUE + str + self.reset

    def color_danger(self, str):
        return Fore.YELLOW + str + self.reset

    def color_error(self, str):
        return Fore.RED + str + self.reset

    def color_validation(self, str):
        return Fore.GREEN + str + self.reset


# v = Vues()
# v.header()
# print(
#     v.select_menu(
#         {
#             "1": "Creer un Tournois",
#             "2": "Ajouter un Joueur",
#             "3": "Generer un Rapport",
#         }
#     )
# )
