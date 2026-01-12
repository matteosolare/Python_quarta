a = input("Inserisci una stringa: ")
n = int(input("Inserisci un numero intero: "))
if(n<=len(a)):
    str = a[0:-2] + "*"*2
    print(f"La frase è {str}")

#ciai