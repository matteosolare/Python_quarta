def add0s(ip):
    """
    prende in input una stringa di max. 4 caratteri e aggiunge degli zeri a sinistra fino a ottenere 4 caratteri
    """

    ip_groups = ip.split(":")
    print(f"ip_groups = {ip_groups}")
    ip_groups = ip.split(":")
    ip_groups = [('0' * (4 - len(group))) + group for group in ip_groups]
    print(f"ip_groups completed = {ip_groups}")
    ip_final = ":".join(ip_groups)
    print(f"ip final = {ip_final}")
    return ip_final

def shortToExtended(ip):
    ip_list = ip.split(":")
    n_groups = len(ip_list)
    print(n_groups)
    print(ip_list)
    if n_groups == 8: #caso facile
        ip_final = add0s(ip)
        #aggiiungere 0 a sinistra nei gruppi
    elif n_groups > 8 or n_groups < 3:
        print("ERRORE: numero di gruppi errato")
        return None
    else:
        n_missing = 8 - n_groups
        missing_0s = ["0" for _ in range(n_missing + 1)]
        missing_groups = ":".join(missing_0s)
        # join() concatena gli elementi della lista mettendo il carattere in mezzo
        print(missing_groups)
        
        ip1, ip2, = ip.split("::")
        print(ip1)
        print(ip2)
        ip_complete = ip1 + ":" + missing_groups + ":" + ip2
    return ip_final

def main():
    ipv6_short = "FDEC:74::B0FF:0:FFF0"
    ipv6_extended = shortToExtended(ipv6_short) # finchè non restituisce niente, ipv6_extended = none
    print(f"IPv6 final extended form = {ipv6_extended}")
    
if __name__=="__main__":
    main()