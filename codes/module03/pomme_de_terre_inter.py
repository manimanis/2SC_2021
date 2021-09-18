titre = "Les bienfaits de la pomme de terre"
par1 = """La pomme de terre est un fruit qui apporte une grande satiété, 
se transporte facilement et peut se consommer partout."""
par2 = """Aussi, une pomme de terre est particulièrement intéressante : 
- avant l'effort elle apporte de l'énergie, 
- pendant l'effort, elle apporte des minéraux des minéraux et des vitamines qui rechargent l'organisme 
- et après l'effort, elle réhydrate !"""

ltit = len(titre)
print("Le titre contient " + str(ltit) + " caractères")
lpar1 = len(par1)
print("Le 1er paragrpahe contient " + str(lpar1) + " caractères")
lpar2 = len(par2)
print("Le 2ème paragrpahe contient " + str(lpar2) + " caractères")

# Utiliser l'indexation positive
print("Le 1er caractère du titre est :", titre[0])
print("Le 1er caractère du 3ème mot du titre est :", titre[14])

# Utiliser l'indexation négative
print("Le 1er caractère du titre est :", titre[-34])
print("Le 1er caractère du 3ème mot du titre est :", titre[-20])

# Utiliser l'indexation positive
print("Le 2ème mot du titre est :", titre[4:13])

# Utiliser l'indexation négative
print("Le 2ème mot du titre est :", titre[-30:-21])

mot = "apporte"
ex_titre = True # à compléter
ex_par1 = True # à compléter
ex_par2 = False # à compléter
print("Le mot", mot, "existe dans le titre :", ex_titre)
print("Le mot", mot, "existe dans le 1er paragrpahe :", ex_par1)
print("Le mot", mot, "existe dans le 2ème paragraphe :", ex_par2)

mot = "pomme"
p_tit = -1 # à compléter
p_p1 = -1 # à compléter
p_p2 = -1 # à compléter
print("Le mot", mot, "est à la position", p_tit, "dans le titre")
print("Le mot", mot, "est à la position", p_p1, "dans le 1er paragraphe")
print("Le mot", mot, "est à la position", p_p2, "dans le 2nd paragraphe")

mot = " de terre"
l_mot = 0 # à compléter
# Todo 1 : supprimer l'expression " de terre" du titre
p_mot = -1 # à compléter
titre = titre # à compléter

# Todo 2 : supprimer l'expression " de terre" du par1

# Todo 3 : supprimer l'expression " de terre" du par2

# Todo 4 : supprimer l'expression " des minéraux" du par2

# Todo 5 : Insérer le mot "succulent" dans par1

# Todo 6 : Insérer l'expression "pour les sportifs"

print('\n'*2)
print(titre)
print()
print(par1)
print()
print(par2)
