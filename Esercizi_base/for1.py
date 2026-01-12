#ci sono tanti modi di fare il for in python 

#vediamo il primo modo, detto C-style

for i in range(4):
    print(i)  #stampa 0, 1, 2, 3

#i corre da 0 a 4 escluso
#oppure:
for i in range(0, 4):
    print(i)  #stampa 0, 1, 2, 3

#si può dare il gap:
for i in range(0, 4, 2):
    print(i)  #stampa 0, 2

#RANGE([start], STOP, [GAP])
for i in range(8, 1, -2):
    print(i)