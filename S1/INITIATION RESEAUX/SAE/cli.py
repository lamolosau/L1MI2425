import sys
import socket

def manage_cli():
    """ 
    Permet de changer l'IP et le port du serveur
    à l'aide de la ligne de commande.
    Si on ne donne pas une adresse IP de machine,
    on utilise localhost et les connexions depuis 
    une autre machine ne sont pas possibles.
    """
    # attention : le premier argument est le nom du programme !
    # len(sys.argv)>=1
    if len(sys.argv)==3:
        ip = sys.argv[1]
        port = int(sys.argv[2])
    else:
        ip = '127.0.0.1'
        if len(sys.argv)==2:
            port = int(sys.argv[1])
        else:
            port = 12345
    return (ip,port)

