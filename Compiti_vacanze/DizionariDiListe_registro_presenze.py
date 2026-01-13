# Un dizionario associa nomi di studenti a liste di date (stringhe) in cui erano presenti. 
# Scrivere funzioni per: (a) contare le presenze di uno studente, (b) trovare chi ha più 
# presenze, (c) trovare chi era presente in una certa data.

def conta_presenze(presenze, nomeStudente):

    return len(presenze[nomeStudente])

def max_presenze(presenze):

    max = 0
    nome = ""
    for studente in presenze:
        if len(presenze[studente]) > max:
            max = len(presenze[studente])
            nome = studente
    return nome

def presenza_in_data(presenze, data_cercata):

    for studente in presenze:
        for data in presenze[studente]:
            if data == data_cercata:
                print(studente)

def main():

    presenze = {
    "Marco": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15"],
    "Sara": ["2024-01-10", "2024-01-12", "2024-01-15", "2024-01-16", "2024-01-17"],
    "Luca": ["2024-01-10", "2024-01-11"],
    "Elena": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15", "2024-01-16"]
    }

    print(conta_presenze(presenze, "Sara"))
    print(max_presenze(presenze))
    presenza_in_data(presenze, "2024-01-11")

if __name__=="__main__":
    main()
