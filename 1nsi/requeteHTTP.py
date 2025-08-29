# 1) Tester le programme ci-dessous et verifier qu'il fonctionne
#    Chercher sur internet la signification des differentes lignes de code
#
# 2) Analyse de la reponse envoyee par le serveur :
#    Ligne HTTP: que signifie le 200 ? et le OK ?
#    Ligne Date: la date est celle de quel ordinateur : du client ou du serveur ?
#    Ligne Content-Length: de quelle longueur s'agit-il ?
#    Comment le corps de la reponse est-il separe de l'entete ?

import ssl, socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(("tfontanet.github.io", 443))
context = ssl.create_default_context()
mySocket = context.wrap_socket(mySocket, server_hostname='tfontanet.github.io')

requete = \
"""
GET / HTTP/1.1
Host: tfontanet.github.io
Connection: close

"""
mySocket.sendall(requete.encode())

reponse = b""
data = mySocket.recv(4096)
while len(data) != 0:
    reponse += data
    data = mySocket.recv(4096)
mySocket.close()
print(reponse.decode())
