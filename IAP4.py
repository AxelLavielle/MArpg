def test_pion (x, y, lP) :
	"""fonction qui test toutes les cases autour de la position donnee en parametre et renvoie le resultat sous cette forme : [nombre de pion aligner a gauche] [puis son joueur] [nombre de pion aligner a droite] [puis son joueur] cela pour la ligne la colonne et les diagonales"""

	lenX= len(lP[1])
	lenY= len(lP)
	w= 0
	joueur= 0
	if x != 0 :
		xTest= x-1
		yTest= y
		joueur= lP[yTest][xTest]
		if joueur != 0 :
			while (xTest != -1) and (lP[yTest][xTest] == joueur):
				w= w+1
				xTest= xTest-1
	lPion= [w, joueur]

	w= 0
	if x != lenX-1 :
		xTest= x+1
		yTest= y
		joueur= lP[yTest][xTest]
		if joueur != 0 :
			while (xTest != lenX) and (lP[yTest][xTest] == joueur):
				w= w+1
				xTest= xTest+1
	lPion+= [w, joueur]

	w= 0
	if y != 0 :
		xTest= x
		yTest= y-1
		joueur= lP[yTest][xTest]
		if joueur != 0 :
			while (yTest != -1) and (lP[yTest][xTest] == joueur):
				w= w+1
				yTest= yTest-1
	lPion+= [w, joueur]

	lPion+= [0, 0]

	w= 0
	if (y != lenY-1) and (x != 0) :
		xTest= x-1
		yTest= y+1
		joueur= lP[yTest][xTest]
		if joueur != 0 :
			while (yTest != lenY) and (xTest != -1) and (lP[yTest][xTest] == joueur):
				w= w+1
				yTest= yTest+1
				xTest= xTest-1
	lPion+= [w, joueur]

	w= 0
	if (y != 0) and (x != lenX-1) :
		xTest= x+1
		yTest= y-1
		joueur= lP[yTest][xTest]
		if joueur != 0 :
			while (yTest != -1) and (xTest != lenX) and (lP[yTest][xTest] == joueur):
				w= w+1
				yTest= yTest-1
				xTest= xTest+1
	lPion+= [w, joueur]

	w= 0
	if (y != 0) and (x != 0) :
		xTest= x-1
		yTest= y-1
		joueur= lP[yTest][xTest]
		if joueur != 0 :
			while (yTest != -1) and (xTest != -1) and (lP[yTest][xTest] == joueur):
				w= w+1
				yTest= yTest-1
				xTest= xTest-1
	lPion+= [w, joueur]

	w= 0
	if (y != lenY-1) and (x != lenX-1) :
		xTest= x+1
		yTest= y+1
		joueur= lP[yTest][xTest]
		if joueur != 0 :
			while (yTest != lenY) and (xTest != lenX) and (lP[yTest][xTest] == joueur):
				w= w+1
				yTest= yTest+1
				xTest= xTest+1
	lPion+= [w, joueur]

	return lPion

def tour_IA (lP) :
	"""Cette fonction est une fonction qui simule une intelligence artificielle elle prend uniquement en parametre lP la matrice du puissance 4
	et elle renvoie la colonne entre 0 et 6 la plus avantageuse pour l'IA
	elle utilise le principe de notes pour chacune des 7 cases possiblent celles-ci calaculees a partir du nombre de pions allie et adverse autour de chaque positions ainsi que de calculs mathematiques pour interpeter ces resultats"""

	# boucle pour determiner les 7 cases possibles
	lYBas= [0,0,0,0,0,0,0]
	for x in range(len(lP[1])) :
		while (lYBas[x] != 6) and (lP[lYBas[x]][x] != 0) :
			lYBas[x]= lYBas[x]+1

	lNotes= [0,0,0,0,0,0,0]

	# boucle principale du calcule de chaques notes
	for x in range(len(lP[1])) :

		# -1000 a la note si on est en haut du tableau
		if lYBas[x] == 6 :
			lNotes[x]= -1000
			continue

		# On recupere tout les pions autour de la position
		lPion= test_pion(x, lYBas[x], lP)

		# Calcule de la note a partir de ces positions par la relation : [plus grand nombre de pions aligne +1] puissance [lui meme +1] multiplier par [le joueur a qui appartient ces pions (1 pour le joueur1 2 pour le joueur2) ]
		# pour la ligne
		if lPion[1] == lPion[3] :
			lNotes[x]= ((lPion[0]+lPion[2]+1)**(lPion[0]+lPion[2]+1))*lPion[1]
		elif lPion[0] > lPion[2] :
			lNotes[x]= ((lPion[0]+1)**(lPion[0]+1))*lPion[1]
		else :
			lNotes[x]= ((lPion[2]+1)**(lPion[2]+1))*lPion[3]

		# pour la colonne
		lNotes[x]+= ((lPion[4]+1)**(lPion[4]+1))*lPion[5]

		# pour les diagonales
		if lPion[9] == lPion[11] :
			lNotes[x]+= ((lPion[8]+lPion[10]+1)**(lPion[8]+lPion[10]+1))*lPion[9]
		elif lPion[8] > lPion[10] :
			lNotes[x]+= ((lPion[8]+1)**(lPion[8]+1))*lPion[9]
		else :
			lNotes[x]+= ((lPion[10]+1)**(lPion[10]+1))*lPion[11]

		if lPion[13] == lPion[15] :
			lNotes[x]+= ((lPion[12]+lPion[14]+1)**(lPion[12]+lPion[14]+1))*lPion[13]
		elif lPion[12] > lPion[14] :
			lNotes[x]+= ((lPion[12]+1)**(lPion[12]+1))*lPion[13]
		else :
			lNotes[x]+= ((lPion[14]+1)**(lPion[14]+1))*lPion[15]

		# petite condition pour eviter les pieges enleve 300 a la note si il y a un piege sur la case du dessu et ajoute 50 si c'est en notre faveur
		if lYBas[x] != 5 :
			lPion= test_pion(x, lYBas[x]+1, lP)
			for i in range(0,len(lPion),4) :
				if lPion[i+1] == lPion[i+3] :
					t= (lPion[i]+lPion[i+2])*lPion[i+1]
				elif lPion[i] > lPion[i+2] :
					t= lPion[i]*lPion[i+1]
				else :
					t= lPion[i+2]*lPion[i+3]
				if t == 3 :
					lNotes[x]-= 300
				if t == 6 :
					lNotes[x]+= 50

	# retourne la plus haute note de cette liste
	return lNotes.index(max(lNotes))