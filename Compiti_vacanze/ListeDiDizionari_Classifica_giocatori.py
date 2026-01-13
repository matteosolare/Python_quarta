# Una lista contiene dizionari con chiavi nome, punteggio. Scrivere una funzione che
# stampi la classifica ordinata per punteggio decrescente, numerando le posizioni.

def stampa_classifica_ordinata_decrescente(giocatori):

    giocatori.sort(key = prendiPunteggio, reverse = True)

    for i in range(len(giocatori)):
        conta = i+1
        informazioni = str(conta)
        for chiave in giocatori[i]:
            informazioni += " " + str(giocatori[i][chiave])
        print(informazioni)

def prendiPunteggio(dizionario):

    return dizionario["punteggio"]

def main():

    giocatori = [
    {"nome": "Player1", "punteggio": 4500},
    {"nome": "Player2", "punteggio": 7200},
    {"nome": "Player3", "punteggio": 3100},
    {"nome": "Player4", "punteggio": 8900},
    {"nome": "Player5", "punteggio": 5600}
    ]

    stampa_classifica_ordinata_decrescente(giocatori)

if __name__ == "__main__":
    main()
