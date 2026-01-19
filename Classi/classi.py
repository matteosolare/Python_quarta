# in python tutto è un oggetto, anche int o float sono oggetti
# anche le funzioni sono oggetti
# creare classi ci permette di creare nuovi oggetti
class Punto():
    # costruttore, viene chiamato da Punto()
    def __init__(self, x, y): # self è come this in java
        #attributi (in python tutto è pubblico) --> no get e set
        self.x = x
        self.y = y
    
    def __str__(self):
        # deve ritornare una stringa
        return f"({self.x}, {self.y})"

def main():

    a = Punto(1, 2) #istanza di punto in coordinate 1, 2
    print(a)

if __name__ == "__main__":
    main()