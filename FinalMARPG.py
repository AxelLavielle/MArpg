import os
from Tkinter import * #On aura besoin de Tkinter pour un affichage plus joli
from random import *  #Et egalement de la fonction random pour les combats
from IAP4 import *
from P4 import *
from MDP import *
from fight import *
#Initialisation de la sauvegarde
#On cherche si un fichier de sauvegarde est deja existant, sinon, on le cree et on lui donne une valeur "0" correspondant
#Creation des deux premiers boutons Tkinter ainsi que de la premiere fenetre Tkinter.
def Choix_Save0():
    global Fenetre_Save
    global Choix_Save
    Fenetre_Save.destroy()
    Choix_Save = 0

def Choix_Save1():
    global Fenetre_Save
    global Choix_Save
    Fenetre_Save.destroy()
    Choix_Save = 1

Choix_Save = 0
Fenetre_Save = Tk()
Fenetre_Save.title = ("Debut Du Jeu")
Scenar_Save = Label(Fenetre_Save, text = "Voulez vous commencer une nouvelle partie ou bien continuer une sauvegarde ?\n")
Button_0 = Button(Fenetre_Save, text = "Commencer", command = Choix_Save0)
Button_1 = Button(Fenetre_Save, text = "Continuer", command = Choix_Save1)
Scenar_Save.pack(), Button_0.pack(side=LEFT, padx = 98), Button_1.pack(side=LEFT)
Fenetre_Save.mainloop()

if Choix_Save == 1:
    SaveR = "a"
    while type(SaveR) != int:
        try:
            SaveO = open("./RPGSave.txt", "r")
            SaveR = SaveO.read()
            SaveR = int(SaveR)
            SaveO.close()
        except:
                SaveO = open("./RPGSave.txt", "w")
                SaveO.write("0")
                SaveO.close()

if Choix_Save == 0:
    SaveO = open("./RPGSave.txt", "w")
    SaveO.write("0")
    SaveO.close()
    SaveO = open("./RPGSave.txt", "r")
    SaveR = SaveO.read()
    SaveR = int(SaveR)
    SaveO.close()

#Initialisation des variables
epee = 0
Choix_ = 0
Choix_2 = 0
Choix_f = 0
Choix_Monstre = 0
viejoueur = 0
stop = 0
fight = 0
x = 1

#Intro du scenario
if SaveR == 0:
    print("Bonjour jeune princesse, comme vous avez refuse la proposition de mariage du roi sorcier Saralzar,\n\
il vous a enferme dans sa tour, la grande tour galamadryabuyak.\nVous devez essayer de vous echapper car vous\
 etes trop laide pour qu'un chevalier vienne vous secourir.\nVous avez 10 points de vie.\n")
    SaveO = open("./RPGSave.txt", "w")
    SaveR = 1
    SaveO.write("1")
    SaveO.close()

if SaveR == 1:
    MDP_Binaire()
    SaveO = open("./RPGSave.txt", "w")
    SaveR = 2
    SaveO.write("2")
    SaveO.close()

if SaveR == 2:
    MDP_shadok("")
    SaveO = open("./RPGSave.txt", "w")
    SaveR = 3
    SaveO.write("3")
    SaveO.close()

while stop == 0 and SaveR < 6: #Debut de la fonction principale du programme.

#Ici je definis a l'avance chacun des boutons qui vont etre utilises dans Tkinter

    def Choix_8():
        global Fenetre
        global Choix_
        Fenetre.destroy()
        Choix_ = 8

    def Choix_6():
        global Choix_
        global Fenetre
        Fenetre.destroy()
        Choix_ = 6

    def Choix_2_2():
        global Choix_2
        global Fenetre_2
        Fenetre_2.destroy()
        Choix_2 = 2

    def Choix_2_5():
        global Choix_2
        global Fenetre_2
        Fenetre_2.destroy()
        Choix_2 = 5

    def Choix_2_8():
        global Choix_2
        global Fenetre_2
        Fenetre_2.destroy()
        Choix_2 = 8

    if SaveR == 3 or SaveR == 4: #Point de sauvegarde, 0, soit aucune sauvegarde precedente
        if SaveR == 4:  #Point de sauvegarde, 1, L'epee a ete prise
            epee = 1
#Debut du scenario
        Fenetre = Tk()
        bouton=Button(Fenetre, text="Quitter le jeu", command = Fenetre.destroy)
        bouton2=Button(Fenetre, text="Aller a droite", command = Choix_6)
        bouton3=Button(Fenetre, text="Aller tout droit", command = Choix_8)
        Scenar_1 = Label(Fenetre, text="Vous etes dans le hall de la tour, voulez vous :\n\n")
        Scenar_1.pack()
        bouton.pack(side=LEFT, padx=15), bouton3.pack(side=LEFT, padx=15), bouton2.pack(side=LEFT, padx=15)
        Fenetre.mainloop() # tkinter : lancement

        if Choix_ == 8: #Si le joueur a choisi d'aller tout droit, on le fais rentrer dans la salle d'en face et
            Choix_ = 0  #On reinitialise son choix (Pour eviter les boucles infinies)

            if epee == 0: # Si le joueur n'a pas pris l'epee:
                Fenetre_2 = Tk()
                bouton_2=Button(Fenetre_2, text="Quitter le jeu", command = Fenetre_2.destroy)
                bouton_2_1=Button(Fenetre_2, text="Revenir en arriere", command = Choix_2_2)
                bouton_2_2=Button(Fenetre_2, text="Prendre l'epee", command = Choix_2_5) # On lui propose de la prendre
                Scenar_2 = Label(Fenetre_2, text="Vous avancez.\nAnduril, l'epee legendaire ayant servi a trancher le doigt de Sauron,\nse trouve devant vous, voulez vous:\n\n")
                Scenar_2.pack()
                bouton_2.pack(side=LEFT, padx=15), bouton_2_1.pack(side=LEFT, padx=15), bouton_2_2.pack(side=LEFT, padx=15)
                Fenetre_2.mainloop() # tkinter : lancement

                if Choix_2 == 5:#Si le joueur la prend, on lui demande de revenir en arriere et on sauvegarde
                    Fenetre_2 = Tk()
                    bouton_2_1=Button(Fenetre_2, text="Revenir en arriere", command = Choix_2_2)
                    Scenar_Sword = Label(Fenetre_2, text="Vous avez maintenant Anduril.\n\n")
                    Scenar_Sword.pack()
                    bouton_2_1.pack(side=LEFT, padx=25)
                    Fenetre_2.mainloop() # tkinter : lancement
                    epee = 1
                    SaveO = open("./RPGSave.txt", "w")
                    SaveR = 4
                    SaveO.write("4")
                    SaveO.close()
                    continue

                if Choix_2 == 2: #Sinon, le  joueur retourne dans la salle precedente
                    continue

                else:
                    stop = 1

            if epee == 1: # Si le joueur a deja pris l'epee: on lui propose uniquement de revenir en arriere.
                Fenetre_2 = Tk()
                Scenar_sword_1 = Label(Fenetre_2, text="Vous avancez, vous avez deja pris Anduril, il n'y a plus rien dans cette salle, voulez vous:")
                bouton_2_2=Button(Fenetre_2, text="Revenir en arriere", command = Choix_2_2)
                Scenar_sword_1.pack()
                bouton_2_2.pack(side=LEFT, padx=250)
                Fenetre_2.mainloop() # tkinter : lancement

                if Choix_2 == 2:
                    continue

                else:
                    stop = 1

        if Choix_ == 6: #Le joueur a choisi d'aller a droite, il se retrouve donc face au sorcier. On lui demande si il veut passer la porte pour arriver jusqu'au sorcier ou reculer.
            Choix_ = 0
            Fenetre_2 = Tk()
            Scenar_Monstre = Label(Fenetre_2, text="Une porte se trouve devant vous.\nVoulez vous :\n")
            bouton_2_3=Button(Fenetre_2, text="Avancer", command = Choix_2_8)
            bouton_2_1=Button(Fenetre_2, text="Reculer", command = Choix_2_2)
            bouton_2=Button(Fenetre_2, text="Quitter le jeu", command = Fenetre_2.destroy)
            Scenar_Monstre.pack()
            bouton_2.pack(side=LEFT, padx=5), bouton_2_3.pack(side=LEFT, padx=5), bouton_2_1.pack(side=LEFT, padx=5)
            Fenetre_2.mainloop() # tkinter : lancement

            if Choix_2 == 8: #Si le joueur choisi le combat, on verifie si le joueur a bien pris l'epee
                Choix_2 = 0

                if epee == 0: #Si il ne l'a pas:
                    Fenetre_2 = Tk()
                    Scenar_S0 = Label(Fenetre_2, text="La porte est verouillee.\n")
                    bouton_2_1=Button(Fenetre_2, text="Revenir en arriere", command = Choix_2_2) #On lui propose de revenir en arriere
                    bouton_2=Button(Fenetre_2, text="Quitter le jeu", command = Fenetre_2.destroy)
                    Scenar_S0.pack()
                    bouton_2.pack(side=LEFT, padx=37), bouton_2_1.pack(side=LEFT, padx=5)
                    Fenetre_2.mainloop() # tkinter : lancement

                if Choix_2 == 2:
                        continue
                else:
                    stop = 1
    if SaveR == 5:
        epee = 1
    while epee == 1: #Si il l'a:
        if x == 1:
            Fenetre_porte = Tk()
            Scenar_S0 = Label(Fenetre_porte, text="Vous explosez le cadenas de la porte avec Anduril et vous appercevez le roi sorcier.\n")
            bouton_2_1=Button(Fenetre_porte, text="Courir vers Saralzar l'epee brandie", command = Fenetre_porte.destroy) #Le joueur cours vers le roi sorcier
            Scenar_S0.pack(), bouton_2_1.pack(side=LEFT, padx=125)
            Fenetre_porte.mainloop() # tkinter : lancement
            SaveO = open("./RPGSave.txt", "w")
            SaveR = 5
            SaveO.write("5")
            SaveO.close()
            fighting()
            x = 0

    else:
        stop = 1 #Fin de la boucle principale du programme.

if SaveR == 6:
    Fenetre_f = Tk()
    Scenar_Victory = Label(Fenetre_f, text="Vous avez enfin tuez le roi sorcier,\nvous pouvez sortir victorieux de ce donjon et aller rassurer les villageois,\nou bien aller a la taverne boire une bonne chope d'hydromel !\n\n")
    Button_Sortie=Button(Fenetre_f, text="Sortir rassurer", command = Fenetre_f.destroy)
    Button_Sortie_2=Button(Fenetre_f, text="Aller a la taverne", command = Fenetre_f.destroy)
    Scenar_Victory.pack()
    Button_Sortie.pack(side=LEFT, padx=75),Button_Sortie_2.pack(side=LEFT, padx=5)
    Fenetre_f.mainloop() # tkinter : lancement
    Fenetre_f = Tk()
    Scenar_Victory = Label(Fenetre_f, text="Mais.. La porte d'entree est bloquee !!!\nPfff.. Voyons voir ca de plus pres..\n")
    Button_Sortie=Button(Fenetre_f, text="S'avancer", command = Fenetre_f.destroy)
    Scenar_Victory.pack()
    Button_Sortie.pack(side=LEFT, padx=75)
    Fenetre_f.mainloop() # tkinter : lancement
    Puissance4(viejoueur)

SaveO = open("./RPGSave.txt", "w")
SaveR = 7
SaveO.write("7")
SaveO.close()

if SaveR == 7:
    os.startfile("processing.html")