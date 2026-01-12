#Crea un programma che chieda all'utente una frase e stampi 
#la stringa inserita un carattere si e uno no

frase = input("Inserisci una frase: ")
frase_alternata = frase[::2]    
print("Frase con un carattere sì e uno no: ")
print(frase_alternata)
