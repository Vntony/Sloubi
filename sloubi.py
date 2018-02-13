# -*-coding:utf-8 -*

import time, sys
from random import randrange

print("Bienvenue dans la taverne, messire, et rejoignez-nous pour une partie de Sloubi !")
pm = 100
print("Dans votre bourse, vous avez %s $. Ne gaspillez pas tout (ou devenez riche. Ou bossez, mais faites un truc.)" %(pm))

while pm >= 1:
    tune = input("Combien voulez-vous miser ?" + "\n")
    try:
        tune == int(tune)
    except ValueError: 
        print("Vous foutez pas de moi, ou vous prenez toute la tartine dans la gueule !")
    else:
        if int(pm) < int(tune) or int(tune) < 1:
            print("Il faut jouer selon les règles, alors respectez, arrêtez de nous souffler dans les narines et misez une vraie somme ! ")
        else:
            pm = int(pm) - int(tune)
            print(int(pm))
            print("Super, maintenant vous devez lancer votre dé à 7 faces (bah ouais, on a trouvé un dé avec une face égale à 0, comme on n'avait plus de poutres de 8 pieds...)")
            dj = randrange(7)

            #partie adversaire
            def perceval():
                return "Perceval"
            def leodagan():
                return "Leodagan"
            def arthur():
                return "Arthur"
            def karadoc():
                return "Karadoc"
            def maitrearmes():
                return "Le maître d'armes"
            def merlin():
                return "Merlin"
            def burgonde():
                return "Le Roi Burgonde"
            options = {0 : perceval,
                       1 : leodagan,
                       2 : arthur,
                       3 : karadoc,
                       4 : maitrearmes,
                       5 : merlin,
                       6 : burgonde,
            }
            adv = options[randrange(7)]()
            print("Voici votre adversaire pour cette partie...")
            
            #boucle pour afficher un message ou photo précis en fonction de l'adversaire
            if adv == options[0]():
                print("")
            else:
                print("CACAAAAAAAAAAAAAAAAAA")

            #début de la partie
            print("Vous avez sorti un %s," %(dj) + " et votre adversaire, %s" %(adv) + ", va lancer son dé.")
            time.sleep(8.5)
            for i in range(1, 8):
                print("*roll roll roll roll*")
                time.sleep(0.4)
            dadv = randrange(7)
            rep = "caca"
            time.sleep(1.5)
            print(adv + " a sorti un %s," %(dadv) + " et vous regarde avec un air biaiseux.")
            time.sleep(1.5)

            #Si le joueur gagne
            if dj > dadv:
                print("Vous lui en avez collé une bonne dans sa tronche !")
                time.sleep(1.5)
                pm = int(pm) + int(tune) + int(tune)
                print("Compte de votre porte-monnaie : %s pièces d'or" %(pm))
                time.sleep(1.5)
                while str(rep) != "a" and str(rep) != "b":
                    rep = input("Souhaitez-vous continuer ?" + "\n" + "a- Mais tout à fait !" + "\n" + "b- Mais certainement pas, monsieur !" + "\n")
                    time.sleep(0.4)
                    if rep == "a":
                        print("Okay !")
                        time.sleep(0.4)
                        print("Tavernier, une mousse pour ce brave personnage, on continue la partie !")
                    elif rep == "b":
                        print("Parfait, allez plutôt nettoyer les cuvettes de la taverne et laissez les vrais jouer !")
                        sys.exit()
            #Si il y a égalité
            elif dj == dadv:
                print("Ah, égalité... Sloubi ?")
                time.sleep(1.5)
                pm = int(pm) + int(tune)
                print("Compte de votre porte-monnaie : %s pièces d'or" %(pm))
                time.sleep(1)
                while str(rep) != "a" and str(rep) != "b":
                    rep = input("Souhaitez-vous continuer ?" + "\n" + "a- Mais tout à fait !" + "\n" + "b- Mais certainement pas, monsieur !" + "\n")
                    time.sleep(0.4)
                    if rep == "a":
                        print("Okay !")
                        time.sleep(0.4)
                        print("Tavernier, une mousse pour ce brave personnage, on continue la partie !")
                    elif rep == "b":
                        print("Parfait, allez plutôt nettoyer les cuvettes de la taverne et laissez les vrais jouer !")
                        sys.exit()
            else:
                print("Vous vous êtes fait bouffer.")
                time.sleep(1.5)
                print("Compte de votre porte-monnaie : %s pièces d'or" %(pm))
                time.sleep(1.5)
                while str(rep) != "a" and str(rep) != "b":
                    rep = input("Souhaitez-vous continuer ?" + "\n" + "a- Mais tout à fait !" + "\n" + "b- Mais certainement pas, monsieur !" + "\n")
                    time.sleep(0.4)
                    if rep == "a":
                        print("Okay !")
                        time.sleep(0.4)
                        print("Tavernier, une mousse pour ce brave personnage, on continue la partie !")
                    elif rep == "b":
                        print("Parfait, allez plutôt nettoyer les cuvettes de la taverne et laissez les vrais jouer !")
                        sys.exit()
            
#Plus d'argent ? Fin de la partie !
else:
    print("Pécore, vous ne pouvez plus jouer et êtes éjecté(e) de la taverne !")
    time.sleep(1)