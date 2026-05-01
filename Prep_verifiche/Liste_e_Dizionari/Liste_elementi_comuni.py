# Date due liste, restituire una nuova lista con gli elementi presenti in entrambe.

def Liste_unite(lista_a, lista_b):
        
    liste_unite = []

    for numero in lista_a:
        liste_unite.append(numero)
    for elemento in lista_b:
        liste_unite.append(elemento)
    print(liste_unite)

def main():

    lista_a = [1, 5, 8, 12, 15, 20]
    lista_b = [3, 5, 10, 12, 18, 20, 25]
    Liste_unite(lista_a, lista_b)

if __name__ == "__main__":
    main()