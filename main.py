# from Model.Joueurs import Joueurs

# print(Joueurs.get_players())


import itertools
from tqdm import tqdm
import time


def brute_force(actions, budget):
    best_profit = 0
    best_combination = []

    # Générer toutes les combinaisons possibles d'actions
    for r in range(1, len(actions) + 1):
        if actions[r][1] > 0 or actions[r][2] > 0:
            combinations = itertools.combinations(actions, r)
            # Parcourir chaque combinaison
            for combination in combinations:
                total_cost = sum(
                    action[1]
                    for action in combination
                    if action[1] > 0 or action[2] > 0
                )

                # Vérifier si le coût total est inférieur ou égal au budget
                if total_cost <= budget:
                    total_profit = sum(
                        action[1] * action[2]
                        for action in combination
                        if action[1] > 0 or action[2] > 0
                    )
                    # Vérifier si le profit total est supérieur au meilleur profit actuel
                    if total_profit > best_profit:
                        best_profit = total_profit
                        best_combination = combination
                        cost = total_cost
                        print(best_profit)
    with open("combinations.txt", "a") as f:
        f.write(
            " Meilleures combinations : "
            + str(best_combination)
            + " \n Meilleur profit : "
            + str(best_profit)
            + "\n Cost :"
            + str(cost)
        )
    return best_combination, best_profit, cost


# [('Action-20', 114, 0.18, 20.52), ('Action-6', 80, 0.25, 20.0), ('Action-4', 70, 0.2, 14.0), ('Action-5', 60, 0.17, 10.200000000000001), ('Action-12', 110, 0.09, 9.9), ('Action-10', 34, 0.27, 9.18), ('Action-19', 24, 0.21, 5.04), ('Action-16', 8, 0.08, 0.64)]
# def calculator(actions, budget):
#     rent = [(action, cost, profit, cost * profit) for action, cost, profit in actions]
#     rent_sorted = sorted(rent, key=lambda x: x[2], reverse=True)
#     best_combination = []
#     budget_limit = 0
#     for action_1, cost_1, profit_1, rentability_1 in rent_sorted:
#         combinations = []
#         for action_2, cost_2, profit_2, rentability_2 in rent_sort:

#     return best_combination


# Liste des actions avec leur coût et leur bénéfice
# actions = [
#     ("Action-1",20,0.05),
# ("Action-2",30,0.1),
# ("Action-3",50,0.15),
# ("Action-4",70,0.2),
# ("Action-5",60,0.17),
# ("Action-6",80,0.25),
# ("Action-7",22,0.07),
# ("Action-8",26,0.11),
# ("Action-9",48,0.13),
# ("Action-10",34,0.27),
# ("Action-11",42,0.17),
# ("Action-12",110,0.09),
# ("Action-13",38,0.23),
# ("Action-14",14,0.01),
# ("Action-15",18,0.03),
# ("Action-16",8,0.08),
# ("Action-17",4,0.12),
# ("Action-18",10,0.14),
# ("Action-19",24,0.21),
# ("Action-20",114,0.18)
# ]


# resultat = []

# for action in actions:
#      nom = action[0]
#      prix = action[1]
#      prc = action[2]
#      profit = prix * prc
#      resultat.append(f"{nom},{prix},{prc},{profit}")

# print(resultat)


# acts = calculator(actions,budget)
# total_cost = 0  # Variabilă pentru a acumula suma costurilor
# t_profit = 0
# t_rent = 0
# for action, cost, profit, rent in acts:
#     total_cost += cost
#     t_profit += profit
#     t_rent += rent


# print("Numar de element " + str(len(acts)))
# print("Suma totală a costurilor:", total_cost)
# print("Suma totală a profituluir:", t_profit)
# print("Suma totală a rentabilitatir:", t_profit)

# print(acts)
actions = []
with open("data.txt", "r") as f:
    for linie in f:
        linie = linie.strip()
        elemente = linie.split(",")
        # Convertiți elementele numerice în numere
        for i in range(1, len(elemente)):
            elemente[i] = float(elemente[i])
        # Verifică dacă toate elementele sunt mai mari sau egale cu 0
        if all(el >= 0 for el in elemente[1:]):
            actions.append(tuple(elemente))


budget = 500.0


print(len(actions))


best_combination, best_profit, cost = brute_force(actions, budget)

print("Meilleure combinaison d'actions :", len(best_combination))
print("Profit total :", best_profit)
print("Cost total :", cost)
print(best_combination)
