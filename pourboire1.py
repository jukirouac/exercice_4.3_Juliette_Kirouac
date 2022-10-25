#  Exercice 4.3
#  Auteur : fait par JK 2022
#  Date création : 2022-09-30 à 11 h
#  Algorithme / Description
#  Cet algorithme permet de calculer le pourboire selon le montant de la facture.
#  Limites
#

#  IMPORTS
from typing import Final
import locale

#  CONSTANTES
# PMC pas besoin d'autant de constantes pour les match-case ! c'est le seul cas ou ce n'est pas obligatoire JK
MONTANT_MAX_POUR_POURBOIRE_FIXE: Final = 10
MONTANT_MAX_POUR_POURBOIRE_PETIT: Final = 100
MONTANT_MAX_POUR_POURBOIRE_MOYEN: Final = 200
POURBOIRE_INITIAL_MONTANT_FIXE: Final = 1.50
POURBOIRE_INITIAL_TAUX: Final = 0
POURBOIRE_PETIT_MONTANT_FIXE: Final = 0
POURBOIRE_PETIT_TAUX: Final = 0.15
POURBOIRE_MOYEN_MONTANT_FIXE: Final = 15
POURBOIRE_MOYEN_TAUX: Final = 0.05
POURBOIRE_GRAND_MONTANT_FIXE: Final = 0
POURBOIRE_GRAND_TAUX: Final = 0

#  VARIABLES
# TODO mettre quelques commentaires JK
montant_facture: float  # montant de la facture avant le pourboire
montant_avec_pourboire: float  # montant de la facture avec le pourboire
taux_pourboire: float  # taux du pourboire pas en pourcentage
montant_fixe: float  # montant fixe à ajouter au pourboire

#  LOGIQUE
locale.setlocale(locale.LC_ALL, '')
montant_facture = float(input("Quel est le montant de la facture ?"))
# PMC ok un match case c'est bien, une série de if-elif-elif-else aurait fait l'affaire aussi JK
match montant_facture:
    case montant_facture if montant_facture < MONTANT_MAX_POUR_POURBOIRE_FIXE:
        montant_fixe = POURBOIRE_INITIAL_MONTANT_FIXE
        taux_pourboire = POURBOIRE_INITIAL_TAUX
    case montant_facture if montant_facture < MONTANT_MAX_POUR_POURBOIRE_PETIT:
        montant_fixe = POURBOIRE_PETIT_MONTANT_FIXE
        taux_pourboire = POURBOIRE_PETIT_TAUX
    case montant_facture if montant_facture < MONTANT_MAX_POUR_POURBOIRE_MOYEN:
        montant_fixe = POURBOIRE_MOYEN_MONTANT_FIXE
        taux_pourboire = POURBOIRE_MOYEN_TAUX
    case _:
        taux_pourboire = POURBOIRE_GRAND_MONTANT_FIXE
        montant_fixe = POURBOIRE_GRAND_TAUX

montant_avec_pourboire = montant_facture * (1 + taux_pourboire) + montant_fixe

print(f"Le prix total de votre facture est de {locale.currency(montant_avec_pourboire)} et le montant du pourboire est"
      f" de {locale.currency(montant_avec_pourboire - montant_facture)}.")
