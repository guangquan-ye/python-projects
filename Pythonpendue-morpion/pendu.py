import random 
#level=input("choix du niveau : debutant, intermediaire, expert :")

#ouvrir le fichier texte avec l'encodage
with open ("/Users/shinz/Documents/Pythonpendue-morpion/dico_france.txt", "r", encoding="ISO-8859-15") as f :
    dico=f.read().split()
    liste=list(dico)
    r=random.choice(liste)

#print (mot)

lvl = (input("Choisir lvl facile intermediaire expert: ")) 
vie = 0

if lvl == "facile":
    vie = 10
elif lvl == "intermediaire":
    vie = 7
elif lvl == "expert":
    vie = 4
else : 
    print ("erreur")
    


historique = []
lettres = []

pendu = False
print ("nombre de lettre :", len(r))
while not pendu:
    pendu = True
    for i in r :
        if i in lettres:
            print (i,end = "")
            
        else: 
            pendu = False
            
            print ("_ ", end ="")
    if vie == 0: 
        print ("Perdu,le mot c'etait : "+r)
        break
    if pendu:
        print(" Winner ! ")
        break
    lettre = input(" choisir une lettre : ")
    lettres.append(lettre)
    if lettre not in r:
        
        vie = vie -1
        print ("nombre de vie restantes :", vie)
    if lvl != "expert" :
        historique.append(lettre)
        print(historique)
        
