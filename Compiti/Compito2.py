#crea un programma in python che chiede all'utente un numero intero
#e stampa se il numero è divisibile per 2, per 3 o per 5. (Hint: usare 
#operatore % per il resto della divisione)

numero = int(input("inserisci un numero intero: "))
print(f"Hai inserito {numero}")
if numero % 2 == 0:
    print("Il numero è divisibile per 2")
if numero % 3 == 0:
    print("Il numero è divisibile per 3")
if numero % 5 == 0:
    print("Il numero è divisibile per 5")
else:
    print("Il numero non è divisibile per 2, 3 o 5")