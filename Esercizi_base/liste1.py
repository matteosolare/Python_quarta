#in python abbiamo le collezioni. tra le collezioni abbiamo: liste, tuple, dizionari, set.

#vediamo le liste
#creare le liste:
l = [3, 3.14, 10, "ciao", True]

#per accedere agli elementi vigono le stesse regole di INDICIZZAZIONE e SLICING delle stringhe

print(f"L'ultimo elemento della lista è {l[-1]}")
print(l)
print(f"Tutta la lista senza il primo e l'ultimo elemento è {l[1:-1]}")

#aggiunta di un elemento
l.append("NUOVO") #NON RESTITUISCE NULLA, MA MODIFICA l!
print(l)
l.pop() #RIMUOVE L'ULTIMO ELEMENTO DELLA LISTA
l.pop()
print(l)
