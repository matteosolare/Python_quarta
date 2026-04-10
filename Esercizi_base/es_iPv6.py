def add0s(string):
    """
    prende in input una stringa di max. 4 caratteri e aggiunge degli zeri a sinistra fino a ottenere 4 caratteri
    """

def shortToExtended(ip):
    ip_list = ip.split(":")
    n_groups = len(ip_list)
    print(n_groups)
    print(ip_list)
    if n_groups == 8:
        #caso facile
        #aggiiungere 0 a sinistra nei gruppi
        pass
    elif n_groups > 8 or n_groups < 3:
        print("ERRORE: numero di gruppi errato")
    else:
        n_missing = 8 - n_groups
        missing_0s = ["0" for _ in range(n_missing + 1)]
        missing_groups = ":".join(missing_0s)
        # join() concatena gli elementi della lista mettendo il carattere in mezzo
        print(missing_groups)
        
        ip1, ip2, = ip.split("::")
        print(ip1)
        print(ip2)

def main():
    ipv6_short = "FDEC:74::B0FF:0:FFF0"
    ipv6_extended = shortToExtended(ipv6_short) # finchè non restituisce niente, ipv6_extended = none
    print(ipv6_extended)
if __name__=="__main__":
    main()