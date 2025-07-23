class Date:
    def __init__(self, jour, mois, année):
        """Constructeur qui génère une erreur si l'année n'est pas un entier,
        ou le mois n'est pas un entier entre 1 et 12,
        ou le jour n'est pas un entier entre 1 et 28, 30 ou 31 selon les mois.
        On fait comme si il n'y avait pas d'année bissectiles !!"""
        pass
        
    def nom_du_mois(self):
        """Renvoie le nom du mois en toutes lettres (janvier, février,...)"""
        pass
        
    def __repr__(self):
        """Permet à Thonny et à Python de savoir comment représenter la date par exemple : 5 janvier 2023"""
        pass

    def combientième_jour_de_année(self):
        """Renvoie un entier donnant le numéro du jour dans l'année"""
        pass
    
    def __lt__(self, other):
        """Permet à Thonny et à Python de savoir comparer deux objets date avec le signe <"""
        pass
        
aujourdhui = Date(17,9,2023)    
print(f"Aujourdhui, nous sommes le {aujourdhui}")
print(f"Déjà {aujourdhui.combientième_jour_de_année()} jours que l'année a commencé !")
demain = Date(18,9,2023)
print(aujourdhui < demain)
