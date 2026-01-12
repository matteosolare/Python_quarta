def main():
    #un dizionario è una sequenza di coppie: valore
    #usati per fare ricerche
    elenco = {"A3-32-B4-FF-F4-32": "Luca", "65-A0-AA-11-F4-19": "Mario"}
    mac1 = "A3-32-B4-FF-F4-32"
    print(elenco[mac1]) 

    mac2 = "A3-32-B4-FF-F4-31" #MAC SBAGLIATO, ALLORA CONTROLLO CON L'IF
    if mac2 in elenco: 
        print(elenco[mac2])
    else:
        print("Mac non trovato!")
        
    #aggiungiamo un nuovo elemento al dizionario
    elenco["FF-FF-FF-FF-FF-FF"] = "broadcast" #per aggiungere elementi al dizionario
    print(elenco)

if __name__=="__main__":
    main()