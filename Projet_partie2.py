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
commande = str(input("What do you do? "))
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
        elif x == "activate switch":
            lumière = False
        elif x == "inventory":
            print("You find some sort of cube in your pocket")
            global found_cube
            found_cube == True
            break
        elif x == "look":
            pass #à faire plus tard
        else:
            print("invalid command, please try again ")
        commande = str(input("What do you do? "))
        valid_avec_lumimière(commande)
    else:
        commande = str(input("You turn off the light. What do you do after?"))
        valid_sans_lumière(commande)

valid_avec_lumimière(commande)

commande = str(input("What do you do? "))
def activate_cube(x):
    if found_cube == True and x == "activate cube":
        for i in range(3):
            if x == "activate cube":
                print("You turn the top part of the cube one turn clockwise")
                if i == 2:
                    print("The cube separates into two halves")
            elif x == "examine cube":
                print("You watch as the cube somehow thightens itself one turn counterclockwise")
                i += -2
                if i < 0:
                    print("The impossibility of that doesn't phase you.")
            else:
                print("You feel that you should keep unscrewing the cube instead of that")
                i += -1
            x = str(input("What do you do? "))
if commande == "activate cube":
    activate_cube(commande)



#Fin du jeu
print("Thank you for playing the demo!")

    


