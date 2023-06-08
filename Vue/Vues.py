from colorama import Fore, Style
import datetime
import os


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
            Fore.GREEN
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

    def menu(self, menu: dict):
        menu_text = "      ".join(
            [
                self.color_yellow(key + ")") + " " + self.color_blue(value)
                for key, value in menu.items()
            ]
        )
        print("\n" + menu_text + "\n\n")

    def color_blue(self, str):
        return Fore.BLUE + str + self.reset

    def color_yellow(self, str):
        return Fore.YELLOW + str + self.reset

    def color_red(self, str):
        return Fore.RED + str + self.reset

    def color_green(self, str):
        return Fore.GREEN + str + self.reset

    def clear_console(self):
        os.system("cls")


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
