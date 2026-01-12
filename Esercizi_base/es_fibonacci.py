n = int(input("Quanti numeri di fibonacci vuoi? ->"))
a, b = 1, 1 #inizializzazione, non dichiarazione
if n > 2:
    for i in range(n):
        print(a, end="-") #end fa si che non vada a capo
        a, b = b, a+b #si potrebbe scrivere anche "a = b", ma mi perderei il valore di a
elif n==0:
    print("Nessun numero stampato")
elif n==2:
    print(a, end="-")
    print(b)
elif n==1:
    print (a)