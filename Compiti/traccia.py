def leggi_registro(nome_file):
    """Restituisce un dizionario {nome: [voti]}."""
    
    nome_file = open("registro.txt", "r")
    righe = nome_file.readlines()
    nome_file.close()

    registroVoti = {}
    listaVoti = []

    for riga in righe:
        campi = riga[:-1].split(";")
        for campo in campi[1:]:
            campo = int(campo)
        listaVoti = campi[1:]
        nome = campi[0]
        registroVoti[nome] = listaVoti
    return registroVoti

def calcola_media(voti):
    """Restituisce la media di una lista di voti."""
    tot = 0
    for voto in voti:
        len_voti = len(voti)
        tot += voto
    media = tot/len_voti
    return media


def classifica(registro):
    """
    Restituisce una lista di tuple (nome, media) 
    ordinata per media decrescente.
    """
    lista_classifica = []
    for nome in registro:
        media = registro[nome]
        tupla = (media, nome)
        lista_classifica.append(tupla)
    lista_ordinata = sorted(lista_classifica, reverse=True)
    class_finale = []
    for tupla in lista_ordinata:
        class_finale.append((tupla[1], tupla[0]))

    return class_finale
        

def stampa_podio(classifica):
    """Stampa i primi 3 della classifica (usa slicing)."""
    print("Podio:")
    for i,tupla in enumerate(classifica[:3]):
        print(f"{i+1} - Nome: {tupla[0]}, media: {tupla[1]}")

def trova_insufficienti(classifica):
    """Restituisce la lista degli studenti con media < 6."""
    insuff = []
    for tupla in classifica:
        if tupla[1] < 6:
            insuff.append(tupla)
    return insuff

def main():
    file = "registro.txt"
    registro_voti = leggi_registro(file)
    #print(registro_voti)

    registro_medie = {}

    for nome in registro_voti:
        media = calcola_media(registro_voti[nome])
        registro_medie[nome] = media
    #print(registro_medie)

    lista_classifica = classifica(registro_medie)
    for i,tupla in enumerate(lista_classifica):
        print(f"{i+1} - Nome: {tupla[0]}, media: {tupla[1]}")
    stampa_podio(lista_classifica)
    lista_insufficienti = trova_insufficienti(lista_classifica)
    print(f"Insufficienti:")
    for tupla in lista_insufficienti:
        print(tupla)


if __name__ == "_main_":
    main()

# Scrivi un programma che: 
# Legga il file e costruisca un dizionario {nome: [lista_voti]}
# Calcoli la media di ogni studente
# Produca una classifica ordinata per media decrescente
# Mostri il "podio" (i primi 3) e gli studenti in difficoltà (media < 6)
