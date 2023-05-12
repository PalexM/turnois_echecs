
from ..Model.Joueurs import Joueurs
from ..Model.Tournois import Tournois
from ..Vue.Vues import Vues


# RAPPORTS
# Nous aimerions pouvoir afficher les rapports suivants dans le programme :
# ● liste de tous les joueurs par ordre alphabétique ;
# ● liste de tous les tournois ;
# ● nom et dates d’un tournoi donné ;
# ● liste des joueurs du tournoi par ordre alphabétique ;
# ● liste de tous les tours du tournoi et de tous les matchs du tour.


class Rapports():

    def __init__(self, rapport_name):
        self.rapport_name = rapport_name
    

    def get_players(self):
        pass

    def get_tournaments(self):
        pass

    def get_tournament_by_name(self, tournament_name):
        pass

    def get_players_from_tournament(self, tournament_name):
        pass

    def get_toutnament_infos(self, tournament_name):
        pass


