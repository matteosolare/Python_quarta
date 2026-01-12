#in python possiamo delimitare con "" oppure con ''

stringa = "ciao mondo!"
print(stringa)
print(f"Il penultimo carattere della stringa è {stringa[-2]}")

#esempio di slicing delle stringhe 
#slicing: modo di tagliare le stringhe 

print(stringa[2:5])

#2 è incluso, 5 invece no, il carattere 5 sarebbe la m di "mondo", ma dato che non è
#incluso prende il carattere dopo

print(f"La sottostringa 2-5 è {stringa[2:5]}.")

#assegnazione pultipla (vale per ogni tipo di dato)
nome, cognome = "Mario ", "Rossi "

#concatenazione tra stringhe
x = nome + cognome 
print(f"Il solito {x}")

#scrive il nome per quante volte scelgo io
y = nome*5
t = cognome*5
print(y)
print(t)