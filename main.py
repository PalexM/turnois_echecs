from Controller.Menu import Menu
import sys

sys.path.append("..")


if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()
    menu.main_menu_interaction()
