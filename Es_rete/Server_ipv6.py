# server udp che sta in ascolto sulla rete, e può fare 2 cose:
# abbreviare indirizzi IP, o scriverli in forma estesa
import socket
from IPv6 import shortToExtended, extendedToShort
# se ipv6.py è nella stessa cartella, funziona
# messaggio client = f"{comando}{indirizzo_ipv6}"
# comando = "SHORT o "EXTENDED" 