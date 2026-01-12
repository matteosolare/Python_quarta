# Scrivere una funzione che trovi il secondo valore più 
# grande in una lista di numeri (senza usare sort o sorted).

def Trova_secondo_val_max(valori):

    massimo = -1
    secondo_massimo = -1
    
    for valore in valori:
        if valore > massimo:
            secondo_massimo = massimo
            massimo = valore
        elif valore > secondo_massimo and valore != massimo:
            secondo_massimo = valore
            
    print(f"All'interno della lista {valori} Il secondo valore massimo è: {secondo_massimo}")

def main():

    valori = [45, 12, 78, 34, 67, 23, 89, 56]
    Trova_secondo_val_max(valori)

if __name__ == "__main__":
    main()