chat_chien = 20
chat_mouton = 54
chien_mouton = 66

masse_anim = (chat_chien + chien_mouton + chat_mouton) / 2

mouton = masse_anim - chat_chien
chat = masse_anim - chien_mouton
chien = masse_anim - chat_mouton

print("La masse total est", masse_anim, "Kg")
print("Chat =", chat)
print("Chien =", chien)
print("Mouton =", mouton)
