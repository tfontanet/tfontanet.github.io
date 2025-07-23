class CompteBancaire:
    def __init__(self, titulaire):
        """le solde et le montant placé dans le livret A sont initialisés à 0"""
        pass

    def retrait(self, somme):
        """vérifier que la somme à retirer est inférieure au solde"""
        pass

    def dépot(self, somme):
        pass

    def placesurlivretA(self, somme):
        """la somme placée n'est plus dans le solde.
        vérifier qu'elle n'est pas supérieure au solde"""
        pass

    def retiredulivretA(self, somme):
        """la somme retirée est remise dans le solde.
        vérifier qu'elle n'est pas supérieure à ce qui est placé"""
        pass

    def __repr__(self):
        """affiche le titulaire, suivi du solde, suivi de ce qui est sur le livret A"""


crédit_lyonnais = CompteBancaire("Thibaud")
print(crédit_lyonnais)
crédit_lyonnais.dépot(500)
print(crédit_lyonnais)
crédit_lyonnais.retrait(50)
print(crédit_lyonnais)
crédit_lyonnais.retrait(50000)
print(crédit_lyonnais)
crédit_lyonnais.placesurlivretA(100)
print(crédit_lyonnais)
crédit_lyonnais.retiredulivretA(50)
print(crédit_lyonnais)

