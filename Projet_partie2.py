# 3 blocs de condition complets (if)
# 3 entrées utilisateurs 
# 1 opérateur logique
# imprimer un résultat

#Note : ceci n'est que le démo et contient seulement le tutoriel

#Mise en situation du jeu et première variable globale qui influencera les états du jeu
print("You are currently in a locked room from which you are trying tp escape.")
print("The last thing you saw was a switch being flipped")
lumière = False
print("(Type the word help for a list of valid commands)")
commande = str(input("What do you do? "))

#Commandes valides lorsque le lumière est fermée
def valid_sans_lumière(x):
    #Ceci devrait être valide et accèssible en tout temps
    if x == "help":
        print("help : shows valid commands")
        print("look : tells you what you see in the romm with which you can interact")
        print("inventory : lists all the relevent object on your person")
        print("examine X : gives you a description of X, an interactable that you can see")
        print("get X : add the object X to the inventory, if possible")
        print("activate X : interact with X with the intension of changing it's state")
        print("use X on Y : interact with Y by using item X from your inventory")
    #Ceci bloque les commandes de base lors du tutoriel
    elif x == "look" or x == "inventory":
        print("It is too dark to see anything.")
    #Intéractions avec 1 objet
    elif x == "examine switch":
        print("You cannot see it anymore, but you feel the switch is still where you last saw it")
    elif x == "get switch":
        print("The switch cannot be removed from the wall")
    #Solution du tutoriel
    elif x == "activate switch":
        print("You flip the light switch and can now see the room and yourself")
        global lumière
        lumière = True
        return x
    else:
        print("invalid command, please try again ")
    commande = str(input("What do you do? "))
    valid_sans_lumière(commande)

#Boucle du tutoriel.
while lumière != True:
    valid_sans_lumière(commande)

#Partie 2 commence ici

#Variable globale qui décrit cette phase du jeu
found_cube = False

#Commandes valides dès que la lumière est ouverte
def valid_avec_lumimière(x):
    lumière = True
    while lumière == True:
            #Ceci devrait être valide et accèssible en tout temps
        if x == "help":
            print("help : shows valid commands")
            print("look : tells you what you see in the romm with which you can interact")
            print("inventory : lists all the relevent object on your person")
            print("examine X : gives you a description of X, an interactable that you can see")
            print("get X : add the object X to the inventory, if possible")
            print("activate X : interact with X with the intension of changing it's state")
            print("use X on Y : interact with Y by using item X from your inventory")
        #condition qui va arrêter la boucle et passer à son else
        elif x == "activate switch":
            lumière = False
        #Besoin de faire cette commande pour continuer continuer
        elif x == "inventory":
            print("You find some sort of cube in your pocket")
            global found_cube
            found_cube == True
            break
        elif x == "look":
            print("You see the following : ")
            print("- The switch you just flipped")
            print("- A door")
            print("- A wall pannel")
        elif x == "activate door":
            print("The door is locked")
        elif x == "examine door":
            print("It's a door with a keyhole above the handle")
        elif x == "examine switch":
            print("It's a standard lightswitch")
        elif x == "examine pannel":
            print("The pannel look like it might be able to be turned into the wall")
            print("It has two square holes, one red and one blue")
        elif x == "activate pannel":
            print("The pannel resists your push as you try to turn it.")
        elif x == "activate cube" or "examine cube":
            print("What cube are you talking about?")
        else:
            print("invalid command, please try again ")
        commande = str(input("What do you do? "))
        valid_avec_lumimière(commande)
    #Si la boucle pert la condition de la lumière, elle passe à ceci
    else:
        commande = str(input("You turn off the light. What do you do after?"))
        lumière = False
        valid_sans_lumière(commande)

#Boucle pour la phase avant de trouver le cube
commande = str(input("What do you do? "))
while found_cube == False:
    #Boucle pour inséré des messages si le joueur prend trop de temps
    for i in range(15):
        commande = str(input("What do you do? "))
        valid_avec_lumimière(commande)
        if i < 4:
            continue
        print("(Don't forget about the help command)")
    print("Maybe this game isn't for you")
    commande = str(input("What do you do? "))
    valid_avec_lumimière(commande)

#Variable globale qui décrit cette phase du jeu
cube_split = False
#Fonction à rouler lorsque l'on active le cube
def activate_cube(x):
    if found_cube == True and x == "activate cube":
        #Doit tourner le cube 3 fois pour l'ouvrir
        for i in range(3):
            if x == "activate cube":
                print("You turn the top part of the cube one turn clockwise")
                if i == 2:
                    print("The cube separates into two halves")
                    print("You place the red-half and the blue-half in you inventory")
                    #Variables globals qui changent l'état du jeu
                    global found_cube 
                    found_cube = False
                    global cube_split
                    cube_split = True
            elif x == "examine cube":
                #Joueur perd du progrès
                print("You watch as the cube somehow thightens itself one turn counterclockwise")
                i += -2
                #Message spécial si l'on examine le cube beaucoup de fois
                if i < 0:
                    print("The impossibility of that doesn't phase you.")
            else:
                #Empêche de terminer la boucle prématurément
                print("You feel that you should keep unscrewing the cube instead of that")
                i += -1
            x = str(input("What do you do? "))

#Boucle de la phase où l'on doit ouvrir le cube
commande = str(input("What do you do? "))
while cube_split == False:
    if commande == "activate cube":
        activate_cube(commande)
    elif commande == "examine cube":
        print("It's a generic cube with two halves (one blue one red) that linked via treading")
    elif commande == "use cube on door":
        print("The cube doesn't fit in the keyhole")
    elif commande == "use cube on switch":
        print("Using the cube, you turn the light off")
        commande = str(input("What do you do? "))
        lumière = False
        valid_sans_lumière(commande)
    elif commande == "use cube on pannel":
        print("None of the faces of the cube do anything when placed into either hole")
    else:
        valid_avec_lumimière(commande)

#Fin du jeu
print("Unfortunately, the demo currently ends here")
print("Thank you for playing the second demo!")

    


