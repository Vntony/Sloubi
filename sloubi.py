# -*-coding:utf-8 -*

import time, sys, os
from random import randrange

os.system('clear')

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
            print("Solde de votre porte-monnaie: %s $" %(pm))
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
            print("Voici votre adversaire pour cette manche...")
            time.sleep(2)
            #boucle pour afficher un message ou photo précis en fonction de l'adversaire
            if adv == options[0]():
                os.system("gvfs-open 'https://www.demotivateur.fr/images-buzz/4771/7d70499bb048568c5dzd6d12d5b89aafbb6.jpg'")
                time.sleep(1)
                os.system('clear')
                print("Bah... ouais, c'est pas faux !")
            elif adv == options[1]():
                os.system("gvfs-open 'http://shared.frenys.com/assets/160917536988/6036879-C-est-pas-si-simple-Leodagan.jpg'")    
                time.sleep(1)
                os.system('clear')
                print("Vous avez intérêt à marcher droit ou vous j'vous promets que vous allez voir du pays !")
            elif adv == options[2]():
                os.system("gvfs-open 'http://www.geek-powa.fr/wp-content/uploads/2015/12/ob_096604_gdwe51vl.jpg'")    
                time.sleep(1)
                os.system('clear')
                print("Moi j'réponds 'Merde'. En principe, ça colle avec tout.")
            elif adv == options[3]():
                os.system("gvfs-open 'http://img0.gtsstatic.com/serie/karadoc_174552_w620.jpg'")    
                time.sleep(1)
                os.system('clear')
                print("Y'a rien à développer, c'est d'la merde !")
            elif adv == options[4]():
                os.system("gvfs-open 'https://78.media.tumblr.com/2bd7a1da4fdcb83b0ea614f941bf50f7/tumblr_mtwd7pKwzB1sjm11ro1_250.gif'")    
                time.sleep(1)
                os.system('clear')
                print("En garde, ma mignonne !")
            elif adv == options[5]():
                os.system("gvfs-open 'http://www.moyenagepassion.com/wp-content/uploads/2017/01/kaamelott_merlin_enchanteur_humour_medieval_serie_televisee_culte_legende_arthur_graal_alexandrin1.jpg'")    
                time.sleep(1)
                os.system('clear')
                print("Qu'est-ce qui est petit et marron ?")
            elif adv == options[6]():
                os.system("gvfs-open 'https://s1-ssl.dmcdn.net/gJ8gv/1280x720-E9S.jpg'")
                time.sleep(1)
                os.system('clear')
                print("Qu'est-ce à dire que ceci ?!")
            time.sleep(5)
            for i in range(1,4):
                os.system('clear')
                print("Vous priez le Graal")
                time.sleep(0.5)    
                os.system('clear')
                print("Vous priez le Graal.")
                time.sleep(0.5)
                os.system('clear')
                print("Vous priez le Graal..")
                time.sleep(0.5)
                os.system('clear')
                print("Vous priez le Graal...")
                time.sleep(1.5)

            #début de la partie
            print("Vous avez sorti un %s," %(dj) + " et votre adversaire, %s" %(adv) + ", va lancer son dé.")
            time.sleep(2.5) #mettre 5
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