from Tkinter import *
from random import *
from P4 import *
def fighting():
    #initialisation des variables et des boutons
    viejoueur = 10
    stop = 0
    epee = 1
    global fight
    viemonstre = 15
    def Choix_f_9():
        Fenetre_f.destroy()
        global fight
        fight = 9

    def Choix_f_2():
        Fenetre_f.destroy()
        global fight
        fight = 2

    while viejoueur != 11:
        fight = 0
        if viejoueur < 1: #Si la vie du joueur est inferieure a 1:
            Fenetre_f = Tk()
            Scenar_Monstre_Mort = Label(Fenetre_f, text="Saralzar vous emmene dans une cage et pars mourir en paix des blessures que vous lui avez infligees\n")
            button_Ok = Button(Fenetre_f, text = "Ok", command = Fenetre_f.destroy)
            Scenar_Monstre_Mort.pack()
            button_Ok.pack(side=LEFT, padx=250)
            Fenetre_f.mainloop() # tkinter : lancement
            Puissance4(viejoueur) #Lancement du puissance 4
            viejoueur = 11
            if viejoueur == 11: #Si la vie du joueur est egale a 11, on arrete toute la boucle.
                stop = 1
                epee = 0
                break

        if viemonstre < 1: #Si la vie du joueur est superieure a 1, le joueur a reussi a tuer le monstre, les variables sont reinitialisees
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
            epee = 0
            stop = 1
            viejoueur = 11
            Puissance4(viejoueur)
            break

        if viejoueur == 11: #Si la vie du joueur est egale a 11, on arrete toute la boucle.
            stop = 1
            epee = 0
            break

        Fenetre_f = Tk() #On demande au joueur si il veut attaquer ou defendre, en precisant sa vie et la vie qu'il reste au monstre.
        Scenar_fight = Label(Fenetre_f, text="Preparez vous a combattre !!.\nVous avez "+str(viejoueur)+" points de vie et Saralzar en a "+str(viemonstre)+"\n")
        bouton_f_2=Button(Fenetre_f, text="Attaquer", command = Choix_f_9)
        bouton_f_3=Button(Fenetre_f, text="Defendre", command = Choix_f_2)
        Scenar_fight.pack()
        bouton_f_2.pack(side=LEFT, padx=35), bouton_f_3.pack(side=LEFT, padx=5)
        Fenetre_f.mainloop() # tkinter : lancement

        if fight == 0:
            viejoueur = 11
            epee = 0
            stop = 1

        if fight == 2: #Si le joueur choisit la defense:
            degatmonstre = randint(0,1)
            viejoueur = viejoueur - degatmonstre
            Fenetre_f = Tk()
            button_Ok = Button(Fenetre_f, text = "Ok", command = Fenetre_f.destroy)
            Scenar_Def = Label(Fenetre_f, text="Vous vous defendez et ne subissez que "+str(degatmonstre)+" de dommages.")
            Scenar_Def.pack()
            button_Ok.pack(side=LEFT, padx=300)
            Fenetre_f.mainloop() # tkinter : lancement
            fight = 0

        if fight == 9: #Si le joueur choisi l'attaque:
            degatmonstre = randint(0,10) #Les degats infliges par le monstre et le joueur son definis aleatoirement
            degatperso = randint(0,10)   #entre 0 et 10
            Fenetre_f = Tk()
            Button_Ok = Button(Fenetre_f, text = "Ok", command = Fenetre_f.destroy)
            Scenar_Att = Label(Fenetre_f, text="Saralzar vous a fais "+str(degatmonstre)+" de dommages, vous avez fait "+str(degatperso)+" de dommages.")
            Scenar_Att.pack()
            Button_Ok.pack(side=LEFT, padx=300)
            Fenetre_f.mainloop() # tkinter : lancement, on y affiche les degats infliges
            viemonstre = viemonstre - degatperso #On fais le calcul de la vie restante (vie - degats)
            viejoueur = viejoueur - degatmonstre #Pour le monstre et le joueur.
            fight = 0