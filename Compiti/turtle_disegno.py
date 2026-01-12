import turtle
def main():
    file = open("disegno.txt", "r")
    righe = file.readlines()
    file.close()

    d = {}
    comando = campi[0]
    step = campi[1]
    
    for riga in righe:
        campi = riga.split(" ")
        d[campi[0]] = int(campi[1])

if __name__ == "__main__":
    main()