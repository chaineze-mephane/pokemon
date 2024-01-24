class Inventaire:
    def ajouter_item(self, item):
        self.inventaire.append(item)
        print(f"{self.nom} a obtenu un(e) {item}!")

    def utiliser_potion(self):
        if "potion" in self.inventaire:
            self.pv += 20  
            self.inventaire.remove("potion")
            print(f"{self.nom} a utilisé une potion et récupéré 20 points de vie.\n {self.nom} à {self.pv}")
        else:
            print(f"{self.nom} n'a pas cette item dans son inventaire.")
    
    def utiliser_superpotion(self):
        if "superpotion" in self.inventaire:
            self.pv += 40
            self.inventaire.remove("superpotion")
            print(f"{self.nom} a utilisé une Super Potion et récupéré 40 points de vie.")
        else:
            print(f"{self.nom} n'a pas cette item dans son inventaire.")
    
    def utiliser_antidote(self):
        if "antidote" in self.inventaire:
            effet = "normal"
            self.inventaire.remove("antidote")
            print(f"{self.nom} a utilisé un antidote, il est plus empoisonné.")
        else:
            print(f"{self.nom} n'a pas cette item dans son inventaire.")
    
    def utiliser_antipara(self):
        if "antipara" in self.inventaire:
            effet = "normal"
            self.inventaire.remove("antipara")
            print(f"{self.nom} a utilisé un antipara, il n'est plus paralysé.")
        else:
            print(f"{self.nom} n'a pas cette item dans son inventaire.")
    
    def utiliser_antibrulure(self):
        if "antibrulure" in self.inventaire:
            effet = "normal"
            self.inventaire.remove("antibrulure")
            print(f"{self.nom} a utilisé un antibrulure, il ne brûle plus.")
        else:
            print(f"{self.nom} n'a pas cette item dans son inventaire.")

    def utiliser_lvlup(self):
        if "lvlup" in self.inventaire:
            self.inventaire.remove("lvlup")
            print(f"{self.nom} a utilisé un lvlup. Votre pokemon a évolué.")
        else:
            print(f"{self.nom} n'a pas cette item dans son inventaire.")               
    
    def utiliser_inventaire(self):
        inventaire_counts = {item: self.inventaire.count(item) for item in set(self.inventaire)}
        print("\nObjets dans l'inventaire:")

        for item, count in inventaire_counts.items():
            print(f" {item} = ({count}x)")

        choix_item = input("Choisissez un objet à utiliser (potion, etc.), ou 0 pour revenir : ")

        if choix_item.lower() == "potion" and "potion" in inventaire_counts:
            self.utiliser_potion()
        elif choix_item.lower() == "superpotion" and "superpotion" in inventaire_counts:
             self.utiliser_superpotion()
        elif choix_item.lower() == "lvlup" and "lvlup" in inventaire_counts:
            self.utiliser_lvlup()
        elif choix_item == "0":
            print("Retour à la sélection d'action.")
