# Esercizio 2 — la classe Studente e le list comprehension
# Contesto
# Si vuole rappresentare un gruppo di studenti e calcolare alcune statistiche.
# Parte 1 — la classe (60%)
# Definire una classe Studente con:
# • nome (str)
# • cognome (str)
# • voti (list[int], default lista vuota)
class Studente:
    def __init__(self, nome, cognome, voti = None):
        self.nome = nome
        self.cognome = cognome
        self.voti = voti if voti is not None else []

    # aggiungi_voto(v) — se v è compreso tra 1 e 10 estremi inclusi, lo aggiunge alla lista dei
    # voti e restituisce True. Altrimenti stampa un messaggio di errore e restituisce False senza
    # modificare la lista.
    def aggiungi_voto(self, v):
        if 1 <= v <= 10:
            self.voti.append(v)
            return True
        else:
            print("Il voto non è valido")
            return False

    #2 media() — restituisce la media dei voti come float. Se la lista è vuota restituisce 0.0.
    def media(self):
        if self.voti:
            return sum(self.voti) / len(self.voti)  # già float
        else:
            return 0.0
        
    #e_promosso() — restituisce True se la media è maggiore o uguale a 6.
    def e_promosso(self):
        if self.media() >= 6:
            print("Promosso")
            return True
        else:
            print("Non promosso")
    
    #__str__ — formato: Rossi Mario: media 7.25 [promosso] oppure [non promosso].
    def __str__(self):
        stato = "promosso" if self.e_promosso else "non promosso"
        return f"{self.nome} {self.cognome}: media {self.media()} [{stato}]"

#la lista dei cognomi degli studenti promossi.
def cognome_promossi(classe):
    return [s.cognome for s in classe if s.e_promosso()]

#la lista degli studenti (oggetti, non stringhe) con almeno tre voti registrati.
def almeno_tre_voti(classe):
    return [s for s in classe if len(s.voti) >= 3]

def main():
    s1 = Studente("Paolo", "Ruffini", [])
    print(s1.aggiungi_voto(11))
    print(s1.aggiungi_voto(8))
    print(s1.voti)
    print(s1.media())
    print(s1.e_promosso())
    print(s1.__str__())

    classe = [
    Studente("Mario", "Rossi", [7, 8, 6, 8]),
    Studente("Luigi", "Bianchi", [4, 3]),
    Studente("Anna", "Verdi", [9, 10, 8, 9]),
    Studente("Sara", "Neri", [5, 6,]),
    Studente("Luca", "Esposito", [6, 7, 8, 6]),
    ]
    print(cognome_promossi(classe))
    for s in almeno_tre_voti(classe):
        print(s)
if __name__ == "__main__":
    main()
