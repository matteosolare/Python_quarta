def addZeros(ip):
    """
    La funzione prende in input una stringa di max 4 caratteri e aggiunge zeri a sinistra
    fino ad ottenere 4 caratteri
    """

    ip_groups = ip.split(":")
    print(f"ip_groups = {ip_groups}")
    ip_groups = [('0' * (4 - len(group))) + group for group in ip_groups]
    print(f"ip_groups completed = {ip_groups}")
    ip_final = ":".join(ip_groups)
    print(f"ip final = {ip_final}")
    return ip_final


def shortToExtended(ip):
    ip_list = ip.split(":")
    n_groups = len(ip_list)
    print(ip_list)
    print(n_groups)

    if n_groups == 8: #caso facile
        ip_final = addZeros(ip)
        #bisogna aggiungere zeri a sinistra nei gruppi che non li hanno
    elif n_groups > 8 or n_groups < 3:
        print("Errore. Numero gruppi errato.")
        return None
    else:
        n_missing = 8 - n_groups
        missing_zeros = ["0" for _ in range(n_missing + 1)]
        missing_groups = ":".join(missing_zeros)
        print(missing_groups)

        ip1, ip2 = ip.split("::")
        print(ip1)
        print(ip2)
        ip_complete = ip1 + ":" + missing_groups + ":" + ip2
        #print(ip_complete)
        ip_final = addZeros(ip_complete)
    
    return ip_final


def removeZeros(string):
    """
    La funzione prende in input una stringa di 4 caratteri e rimuove zeri a sinistra
    """
    count = 0
    for c in string:
        if c == "0":
            count += 1
        else:
            break
    if count == 4:
        return "0"
    return string[count:]
    

def extendedToShort(ip):
    """
    Cerca il gruppo di zeri consecutivi più lungo e lo sostituisce con '::'
    """
    ip_final = ""
    ip_groups = ip.split(":")
    print(f"ip_groups = {ip_groups}")

    # Rimuovo gli zeri a sinistra da ogni gruppo
    ip_groups = [removeZeros(group) for group in ip_groups]
    print(f"ip_groups senza zeri = {ip_groups}")

    sequence_start = -1
    sequence_len = 0
    best_start = -1
    best_len = 0

    for i, group in enumerate(ip_groups):
        if group == "0":
            if sequence_len == 0:
                sequence_start = i
            sequence_len += 1
            if sequence_len > best_len:
                best_start = sequence_start
                best_len = sequence_len
        else:
            sequence_len = 0


    if best_len >= 2:
        ip1 = ip_groups[:best_start]
        ip2 = ip_groups[best_start+best_len:]
        print(f"ip1 = {ip1}, ip2 = {ip2}")
        ip_final = ":".join(ip1) + "::" + ":".join(ip2)
    else:
        ip_final = ":".join(ip_groups)

    return ip_final

def main():
    ipv6_short= "FDEC:74::B0FF:0:FFF0" 
    ipv6_extended = shortToExtended(ipv6_short)
    print(f"IPv6 final extended form = {ipv6_extended}")
    ipv6_extended= "FDEC:0074:0000:0000:0000:B0FF:0000:FFF0" 
    ipv6_short = extendedToShort(ipv6_extended)
    print(f"IPv6 extended form = {ipv6_extended}")
    print(f"IPv6 final short form = {ipv6_short}")
if __name__ == "__main__":
    main()