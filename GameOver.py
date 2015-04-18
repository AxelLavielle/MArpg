from Tkinter import *
def Game_Over(): #Debut de la fonction fin de la partie.
    Fenetre_Game_Over = Tk()
    Fenetre_Game_Over.title = ("GAME OVER")
    Scenar_Game_Over = Label(Fenetre_Game_Over, text = "Vous n'avez pas reussi a vaincre le mecanisme, il se bloque.\nVous croupissez dans la cellule et mourrez de faim.\n\nGAME OVER")
    Button_Quitter = Button(Fenetre_Game_Over, text = "Quitter", command = Fenetre_Game_Over.destroy)
    Scenar_Game_Over.pack()
    Button_Quitter.pack(side=LEFT, padx = 250)
    Fenetre_Game_Over.mainloop() # tkinter : lancement

    global epee#On reinitialise toutes les variables pour pouvoir quitter la boucle
    epee = 0
    global stop
    stop = 1
    global viejoueur
    viejoueur = 11