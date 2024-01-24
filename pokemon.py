from inventaire import Inventaire
import random

class Personnage(Inventaire):

    def __init__(self, nom, pv, defense, vit, xp, lvl, inventaire, types, atk_base, effet="normal"):
        super().__init__()
        self.nom = nom
        self.pv = pv
        self.defense = defense
        self.vit = vit
        self.xp = xp
        self.lvl = lvl
        self.inventaire = ['potion'] * 3 + ['superpotion'] * 1
        self.types = types
        self.atk_base = atk_base
        self.effet = effet
        
        self.paralyser = False
        self.empoisonner = False
        self.bruler = False
        self.soigner = False
        self.tour = 0



      

    def evololution(self):
        xp_necessaire = 100 
        while self.xp >= xp_necessaire:
            self.lvl += 1
            self.xp -= xp_necessaire
            xp_necessaire += 50 
            self.item_evolution()
            print(f"{self.nom} est passé au niveau {self.lvl}!")
            
    def item_evolution(self):
        nouveau_item = 'lvlup'
        self.inventaire.append(nouveau_item)       
        
    def calculer_degats(self, attaqueur, defenseur):
        multiplicateurs_type = {
            "eau": {"feu": 2.0, "terre": 0.5, "plante": 0.5, "eau": 1.0},
            "feu": {"eau": 0.5, "plante": 2.0, "terre": 0.5, "feu": 1.0},
            "terre": {"eau": 2.0, "feu": 0.5, "terre": 1.0, "terre": 1.0},
            "normal": {"eau": 0.75, "feu": 0.75, "terre": 0.75, "normal": 0.75},
        }


        if attaqueur.types in multiplicateurs_type and defenseur.types in multiplicateurs_type[attaqueur.types]:
            multiplicateur = multiplicateurs_type[attaqueur.types][defenseur.types]

        pourcentage_ratage = 0.20
        if random.random() <= pourcentage_ratage:
            print(f"\n{attaqueur.nom} a raté son attaque!")
            return 0    

        
        degats = attaqueur.atk_base * multiplicateur

        return degats

    def utiliser_attaque_speciale(self,autre):
            
            if self.types == "electrique":
                print(f"{self.nom} a utilisé ???? , {autre.nom} est paralysé")
                autre.paralyser = True
                autre.tour = 2

            elif self.types == "plante": 
                print(f"{self.nom} a utilisé ???? , {autre.nom} est empoisonné")
                autre.empoisonner = True
                autre.tour = 2

            elif self.types == "feu":
                print(f"{self.nom} a utilisé ???? , {autre.nom} est brulé")
                autre.bruler = True
                autre.tour = 2
            
            elif self.types == "eau":
                print(f"{self.nom} a utilisé ???? , il se soigne")
                autre.soigner = True
                autre.tour = 3

             
################################## LE JEU #######################################
    

    def choisir_action(self):
        print("\nActions disponibles:") 
        print("1. Attaquer")
        print("2. Attaque Special")
        print("3. Se défendre")
        print("4. Inventaire")

        choix = input("Choisissez une action (1/2/3/4) : ")

        if choix == "1":
            return "Attaquer"
        elif choix == "2":
            return "Attaque Special"
        elif choix == "3":
            return "Se défendre"
        elif choix == "4":
            return "Inventaire"    
        else:
            print("Action invalide. Veuillez choisir une action valide.")
            return self.choisir_action()

    def combat(self, ennemi):
        
        while self.pv > 0 and ennemi.pv > 0:
            action = self.choisir_action()

            if action == "Attaquer":
                print(f"\n{self.nom} attaque {ennemi.nom}!")
                
                if  ennemi.paralyser:
                    ennemi.pv -= self.calculer_degats(self, ennemi)
                    print(f"{self.nom} est paralysé et ne peut pas attaquer ce tour.")
                
                elif  ennemi.empoisonner:
                    ennemi.pv -= 2
                    print(f"{self.nom} est empoisonnée et perds 2 pv supplementaire dans ce tour.")
                
                elif ennemi.bruler:
                    ennemi.pv -= 3
                    print(f"{self.nom} est brulé et perds 2 pv supplementaire dans ce tour.")
                
                elif ennemi.soigner:
                    ennemi.pv += 5
                    print(f"{self.nom} ce soigne est gagne 5 pv supplementaire dans ce tour.")

                print(f"{ennemi.nom} a maintenant {ennemi.pv} points de vie.")
                
                if ennemi.paralyser:
                    ennemi.tour -=1
                    if ennemi.tour == 0:
                        ennemi.paralyser = False
                elif ennemi.empoisonner:
                    ennemi.tour-= 1
                    if ennemi.empoisonner == 0:
                        ennemi.empoisonner = False  
                elif ennemi.bruler:
                    ennemi.tour-= 1
                    if ennemi.empoisonner == 0:
                        ennemi.bruler = False  
                elif ennemi.soigner:
                    ennemi.tour-= 1
                    if ennemi.soigner == 0:
                        ennemi.soigner = False  
                        

            elif action == "Attaque Special":
                self.utiliser_attaque_speciale(ennemi)
            
            elif action == "Se défendre":
                print(f"\n{self.nom} se défend contre l'attaque de {ennemi.nom}.")
                self.pv -= ennemi.calculer_degats(ennemi, self) / 2  # Réduit les dégâts en se défendant
                print(f"{self.nom} a maintenant {self.pv} points de vie.")
           
            elif action == "Inventaire":
                self.utiliser_inventaire()
            else:
                print("Action invalide. Veuillez choisir une action valide.")
    

            if ennemi.pv <= 0:
                print(f"{ennemi.nom} a été vaincu ! Vous avez gagné !")
                self.xp += 50
                print(f"Vous avez gagné 50 xp. Votre xp total : {self.xp}")
                self.evololution()
                break

            print(f"\n{ennemi.nom} attaque {self.nom}!")
            self.pv -= ennemi.calculer_degats(ennemi, self)
            print(f"{self.nom} a maintenant {self.pv} points de vie.")

            if self.pv <= 0:
                print(f"{self.nom} a été vaincu ! Vous avez perdu.")
                break


        
        rejouer = input("Voulez vous continuez ?")
        if rejouer  == "oui":
            main()
        elif rejouer == "non":
            quit   




def main():
    
    attaqueur = Personnage("Salameche", 100, 10, 10, 0, 4, 0, "feu", 10, )  
    ennemi = Personnage("Caninos", 100, 10, 10, 0, 5, 0, "feu", 10, )
    

  

    if attaqueur is not None and ennemi is not None:
        attaqueur.combat(ennemi)
        attaqueur.evololution()

# Appel de la fonction principale
if __name__ == "__main__":
    main()