nom1 = input("Nom de la 1ère personne ? ")
age1 = input("Âge de " + nom1 + " ? ")

nom2 = input("Nom de la 2ème personne ? ")
age2 = input("Âge de " + nom2 + " ? ")

c1 = age1 > age2

print(nom1, "est plus âgé que", nom2, "?", c1)