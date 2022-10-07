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
montant_facture: float
montant_avec_pourboire: float
taux_pourboire: float
montant_fixe: float

#  LOGIQUE
locale.setlocale(locale.LC_ALL, '')
montant_facture = float(input("Quel est le montant de la facture ?"))

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
