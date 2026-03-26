# Attention : pour bien évaluer la complexité des algorithmes ci-dessous,
# on ne s'autorisera pas à comparer des chaînes de caractères entières (même si Python le permet)
# on les comparera caractère par caractère.

# 1) Commencer par compléter la fonction ci-dessous
# qui effectue la recherche naïve évoquée dans la vidéo
def recherche_naive(texte, motif):
    pass

phrase = "bonjour josianne comment ça va ?"
adn = "CAAGCGCACAAGACGCGGCAGACCTTCGTTATAGGCGATGATTTCGAACCTACTAGTGGGTCTCTTAGGCCGAGCGGTTCCGAGAGATAGTGAAAGATGGCTGGGCTGTGAAGGGAAGGAGTCGTGAAAGCGCGAACACGAGTGTGCGCAAGCGCAGCGCCTTAGTATGCTCCAGTGTAGAAGCTCCGGCGTCCCGTCTAACCGTACGCTGTCCCCGGTACATGGAGCTAATAGGCTTTACTGCCCAATATGACCCCGCGCCGCGACAAAACAATAACAGTTTGCTGTATGTTCCATGGTGGCCAATCCGTCTCTTTTCGACAGCACGGCCAATTCTCCTAGGAAGCCAGCTCAATTTCAACGAAGTCGGCTGTTGAACAGCGAGGTATGGCGTCGGTGGCTCTATTAGTGGTGAGCGAATTGAAATTCGGTGGCCTTACTTGTACCACAGCGATCCCTTCCCACCATTCTTATGCGTCGTCTGTTACCTGGCTTGGCAT"

assert recherche_naive(phrase, "comment") == 17
assert recherche_naive(phrase, "coucou") == -1
assert recherche_naive(adn, "CAAGCGCACAAG") == 0
assert recherche_naive(adn, "A") == 1
assert recherche_naive(adn, "AGACGCGGCAGACCT") == 10
assert recherche_naive(adn, "AGGAAGCCAGC") == 340

# 2) Compléter maintenant la fonction ci-dessous qui retourne un dictionnaire
# contenant les décalages à faire comme expliqué dans la vidéo
def décalages(motif):
    pass
        
assert décalages("comment") == {'c': 6, 'o': 5, 'm': 3, 'e': 2, 'n': 1}
assert décalages("") == {} 
assert décalages("a") == {}
assert décalages("papapa") == {'p': 1, 'a': 2}
assert décalages("quinquennal") == {'q': 6, 'u': 5, 'i': 8, 'n': 2, 'e': 4, 'a': 1}

# 3) Compléter la fonction ci-dessous qui appelle la fonction "décalages"
# et utilise l'algorithme de Boyer-Moore-Horspool expliqué dans la vidéo
def recherche_boyer_moore(texte, motif):
    pass

        
assert recherche_boyer_moore(phrase, "comment") == 17
assert recherche_boyer_moore(phrase, "coucou") == -1
assert recherche_boyer_moore(adn, "CAAGCGCACAAG") == 0
assert recherche_boyer_moore(adn, "A") == 1
assert recherche_boyer_moore(adn, "AGACGCGGCAGACCT") == 10
assert recherche_boyer_moore(adn, "AGGAAGCCAGC") == 340

