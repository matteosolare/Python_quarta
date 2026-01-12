def main():
    file = open("mac-vendors-export.csv", "r", encoding = 'utf-8')
    righe = file.readlines()
    file.close()

    mac_address = []
    vendor = []
    data = []

    for riga in righe[1:]:
        campi = riga.split(",") #split divide i campi del csv
        mac_address.append(campi[0])
        vendor.append(campi[1])
        data.append(campi[-1])

    #exit() il programma arriva fino alla fine e poi finisce, per i test
    mac = input("inserisci il MAC address per intero->").upper()
    mac = mac.replace("-", ":")
    #gestire anche il carattere - come separatore dei byte del MAC 
    #usare il medoto replace delle stringhe 
    #usando l'IA: scrivere una funzione python che restituisce il macaddress della scheda di
    #rete wi-fi del proprio pc
    for m, v, d in zip(mac_address, vendor, data):
          if m[0:8]==mac[0:8]:
              print(f"Il MAC address è {m}")
              print(f"Il produttore è {v}")
              print(f"La data è {d}")

if __name__=="__main__": #dunder doppio underscore si usa per molti contesti
                         #in questo caso è una variabile
    main()