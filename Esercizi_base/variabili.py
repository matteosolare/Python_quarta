# il carattere # serve per i commenti
# in questo programma useremo l'assegnazione
# in python non ci sono dichiarazioni, python fa
# dynamic type cheking (controllo dinamico dei tipi)
# sulla base dei valori assegnati alle variabili 

a = 1
print(a)    # stampa il valore di a
print(type(a))  # stampa il tipo di a

b = input("Scrivi qualcosa -> ") # simile a scanf
# input restituisce sempre stringhe
# facciamo una print con una f-string
print(f"Hai inserito {b} che è di tipo {type(b)}") # la f ti permette di mettere in 
# automatico le variabili dentro le print

