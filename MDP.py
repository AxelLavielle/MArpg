def MDP_Binaire():
    #Scenario du mot de passe Binaire
    print("Bonjour princesse, je suis le maitre des cles, et j'en ai une a vous donner.\n\
Bien sur, vous vous en doutez, vous devrez trouver reponse a mes deux enigmes.\n\
La premiere est la suivante:\nQuelle est la representation binaire de mon nom ?\n\n\
On utilisera pour cela la table suivante:\na = 01\nb = 02\nc = 03,\nect..\n\n\
Je m'apelle Axel et les leviers sont tous a 0 (desactives)\n\
Choisissez le levier 1, 2, 3, 4 ou 5 pour l'activer ou le desactiver. Commencons par la lettre A:")
    lettre = [0,0,0,0,0]#Initialisation de la lettre sous forme binaire

    while lettre[0] != 0 or lettre[1] != 0 or lettre[2] != 0 or lettre[3] != 0 or lettre[4] != 1: #Tant que la personne n'a pas trouve la bonne lettre,

        print(lettre[0],lettre[1],lettre[2],lettre[3],lettre[4]) #On lui affiche a ou il en est
        Levier_Choisi = int(input("Quel levier voulez vous activer/desactiver ? (tapez 1, 2, 3, 4 ou 5)")-1)#On demande quel levier veut etre active ou desactive et on le change de sens
        if lettre[Levier_Choisi] == 0:
            lettre[Levier_Choisi] = 1
        else : lettre[Levier_Choisi] = 0

    print("Bravo vous avez trouver la lettre A, c'est bien 00001 passons a la lettre X:") #Si la personne a trouve le bon code
    lettre = [0,0,0,0,0]#on reinitialise la lettre
    while lettre[0] != 1 or lettre[1] != 1 or lettre[2] != 0 or lettre[3] != 0 or lettre[4] != 0: #Et on recommence avec la lettre suivante

        print(lettre[0],lettre[1],lettre[2],lettre[3],lettre[4])
        Levier_Choisi = int(input("Quel levier voulez vous activer/desactiver ? (tapez 1, 2, 3, 4 ou 5)")-1)
        if lettre[Levier_Choisi] == 0:
            lettre[Levier_Choisi] = 1
        else : lettre[Levier_Choisi] = 0

    print("Bravo vous avez trouver la lettre X, c'est bien 11000 passons a la lettre E:")
    lettre = [0,0,0,0,0]
    while lettre[0] != 0 or lettre[1] != 0 or lettre[2] != 1 or lettre[3] != 0 or lettre[4] != 1:

        print(lettre[0],lettre[1],lettre[2],lettre[3],lettre[4])
        Levier_Choisi = int(input("Quel levier voulez vous activer/desactiver ? (tapez 1, 2, 3, 4 ou 5)")-1)
        if lettre[Levier_Choisi] == 0:
            lettre[Levier_Choisi] = 1
        else : lettre[Levier_Choisi] = 0

    print("Bravo vous avez trouver la lettre E, c'est bien 00101 passons a la lettre L:")
    lettre = [0,0,0,0,0]
    while lettre[0] != 0 or lettre[1] != 1 or lettre[2] != 1 or lettre[3] != 0 or lettre[4] != 0:

        print(lettre[0],lettre[1],lettre[2],lettre[3],lettre[4])
        Levier_Choisi = int(input("Quel levier voulez vous activer/desactiver ? (tapez 1, 2, 3, 4 ou 5)")-1)
        if lettre[Levier_Choisi] == 0:
            lettre[Levier_Choisi] = 1
        else : lettre[Levier_Choisi] = 0

    print("Bravo vous avez trouver la lettre L, c'est bien 01100, le code complet est donc:\n00001\n11000\n00101\n01100")
    print("Vous avez retranscris mon nom en binaire, voici votre cle.")

def MDP_shadok(a):
    #Scenario du mot de passe Shadok
    print("Bravo princesse, vous avez resolu ma premiere enigme et j'en ai une deuxieme a vous donner.\n\
Bien sur, vous vous en doutez, vous devrez trouver reponse a celle ci.\n\
La seconde est la suivante:\nQuel est mon deuxieme nom en Shadok ?\n\n\
On utilisera pour cela la table suivante:\na = 00\nb = 01\nc = 02,\nect..\n\n\
Voici mon nom en Shadok: MEGA GAGA ZOME MEZO\n\
0 = GA\n1 = BU\n2 = ZO\n3 = ME")
    while a != "malo": #Tant que la personne n'a pas rentre le nom "malo",
        a=raw_input("entrez le mot de passe :")#On redemande le mot de passe