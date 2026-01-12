#Crea un programma in python che chiede all'utente il suo nome 
#e lo stampa sempre con l'iniziale maiuscola

nome = input("Inserisci il nome: ")
maiusc = nome[0].upper() + nome[1:]
print(f"Il tuo nome è {maiusc}")

