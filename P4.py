from Tkinter import *
from IAP4 import *
from GameOver import *
import os
def Couleur_P4(lP):
    global x
    #Definiton des 7 boutons pour les 7 colonnes
    def ButtonP4F1():
        global x
        x = 0
        Fenetre_P4.destroy()

    def ButtonP4F2():
        global x
        x = 1
        Fenetre_P4.destroy()

    def ButtonP4F3():
        global x
        x = 2
        Fenetre_P4.destroy()

    def ButtonP4F4():
        global x
        x = 3
        Fenetre_P4.destroy()

    def ButtonP4F5():
        global x
        x = 4
        Fenetre_P4.destroy()

    def ButtonP4F6():
        global x
        x = 5
        Fenetre_P4.destroy()

    def ButtonP4F7():
        global x
        x = 6
        Fenetre_P4.destroy()
    ListeColor = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]#Cette liste sert a savoir quelle couleur nous allons mettre a quelle case
    XColor=0
    YColor=5
    Fenetre_P4=Tk()
    Scenar=Label(Fenetre_P4, text="C'est a vous,\nPrincesse, de jouer.\nChoisissez dans quelle colonne\nmettre votre pion. \n").grid(row=1,column=0, columnspan=7)
    buttonP4_1=Button(Fenetre_P4, text="1", command = ButtonP4F1).grid(row=8,column=0)
    buttonP4_2=Button(Fenetre_P4, text="2", command = ButtonP4F2).grid(row=8,column=1)
    buttonP4_3=Button(Fenetre_P4, text="3", command = ButtonP4F3).grid(row=8,column=2)
    buttonP4_4=Button(Fenetre_P4, text="4", command = ButtonP4F4).grid(row=8,column=3)
    buttonP4_5=Button(Fenetre_P4, text="5", command = ButtonP4F5).grid(row=8,column=4)
    buttonP4_6=Button(Fenetre_P4, text="6", command = ButtonP4F6).grid(row=8,column=5)
    buttonP4_7=Button(Fenetre_P4, text="7", command = ButtonP4F7).grid(row=8,column=6)
    #Les lignes au dessus servent a placer les boutons et le scenario
    for i in range (0,42): #Pour chaque cellules,
        if XColor == 7:    #Si on arrive a la fin de la ligne, on passe a la ligne d'en dessous
            XColor = 0
            YColor = YColor - 1

        if lP[YColor][XColor] == 0:
            ListeColor[YColor][XColor]=Label(Fenetre_P4, text=".",fg="#000000").grid(row=5-YColor+2,column=XColor)#On remplace les cellules par un "." si personne n'a joue dedans

        if lP[YColor][XColor] == 1:
            ListeColor[YColor][XColor]=Label(Fenetre_P4, text="0",fg="#00FF00").grid(row=5-YColor+2,column=XColor)#On remplace les cellules par un "0" de couleur verte si le joueur a jouer dedans

        if lP[YColor][XColor] == 2:
            ListeColor[YColor][XColor]=Label(Fenetre_P4, text="0",fg="#FF0000").grid(row=5-YColor+2,column=XColor)#Om remplace les cellules par un "0" de couleur rouge si l'ordinateur a jouer dedans

        XColor = XColor + 1
    Fenetre_P4.mainloop()

def Puissance4(viejoueur): #Debut de la fonction puissance 4
    # Code tkinter pour generer la fenetre et les boutons
    global SaveR
    SaveO = open("./RPGSave.txt", "w")
    SaveR = 7
    SaveO.write("7")
    SaveO.close()
    global x
    global epee
    global stop
    viejoueur = 11
    stop = 1
    epee = 0
    lP=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    Fenetre_f = Tk()
    Fenetre_f.title = ("Debloquage de la serrure")
    Scenar_P4 = Label(Fenetre_f, text = "Vous vous apercevez que la serrure est un puissance 4.\nVous vous approchez pour pouvoir la debloquer, un mecanisme semble repondre a la partie.")
    button_Ok = Button(Fenetre_f, text = "Ok", command = Fenetre_f.destroy)
    Scenar_P4.pack()
    button_Ok.pack(side=LEFT, padx = 250)
    Fenetre_f.mainloop() # tkinter : lancement
    y=0
    x=0
    j = 1

    def verif(j,x,y):
        if j!=0:
            for a in range(0,4):#horizontale
                if lP[y][a]==j and lP[y][a+1]==j and lP[y][a+2]==j and lP[y][a+3]==j:
                    if j == 2:
                        Game_Over()
                        os.startfile("processing.html")
                        j = 0
                        break
                    if j == 1:
                        os.startfile("processing.html")
                        j = 0
                        break

        if j!=0:
            for y in range(0,3):#verticale
                if lP[y][x]==j and lP[y+1][x]==j and lP[y+2][x]==j and lP[y+3][x]==j:
                    if j == 2:
                        Game_Over()
                        os.startfile("processing.html")
                        j = 0
                        break
                    if j == 1:
                        os.startfile("processing.html")
                        j = 0
                        break

        if j!=0:#diagonale haut droite
                for y in range(0,3):
                    if j==0:
                        return j
                    for a in range(0,4):
                        if lP[y][a]==j and lP[y+1][a+1]==j and  lP[y+2][a+2]==j and lP[y+3][a+3]==j:
                            if j == 2:
                                Game_Over()
                                os.startfile("processing.html")
                                j = 0
                                break
                            if j == 1:
                                os.startfile("processing.html")
                                j = 0
                                break

        if j!=0:#diagonale haut gauche
                for y in range(0,3):
                    if j==0:
                        return j
                    for a in range(3,7):
                        if lP[y][a]==j and lP[y+1][a-1]==j and  lP[y+2][a-2]==j and lP[y+3][a-3]==j:

                            if j == 2:
                                Game_Over()
                                os.startfile("processing.html")
                                j = 0
                                break
                            if j == 1:
                                os.startfile("processing.html")
                                j = 0
                                break

        return j
    if j==1 or j==2:
        while j!=0:
            if j==1:
                y=0
                x = 0
                Couleur_P4(lP)
                while lP[5][x] != 0:
                    Couleur_P4(lP)
                while lP[y][x]!=0:
                    y=y+1
                lP[y][x]=1
                j=verif(j,x,y)
                if j!=0:
                    j=2
            if j==2:
                y=0
                x=tour_IA(lP)
                while lP[y][x]!=0:
                    y=y+1
                lP[y][x]=2
                j=verif(j,x,y)
                if j!=0:
                    j=1