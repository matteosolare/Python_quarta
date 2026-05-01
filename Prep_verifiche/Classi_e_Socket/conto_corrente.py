class ContoCorrente():
    def __init__(self, intestatario, iban, saldo = 0.0):
        self.intestatario = intestatario
        self.iban = iban
        self.saldo = saldo

    def versa(self, importo):
        if importo > 0:
            self.saldo = self.saldo + importo
            return True
        else:
            print("L'importo deve essere maggiore di 0")
            return False

    def preleva(self, importo):
        if importo > 0 and importo <= self.saldo:
            self.saldo = self.saldo - importo
            return True
        else:
            print("Saldo insufficente")
            return False

    def bonifico(self, altro_conto, importo):
        if self.preleva(importo) == False:
            return False
        else:
            altro_conto.versa(importo)
            return True

    def __str__(self):
        return f"{self.intestatario} ({self.iban}): saldo {self.saldo}€"

def main():

    conto1 = ContoCorrente("mario", "IT60 X054 2811 1010 0000 0123 456")
    conto2 = ContoCorrente("luigi", "IT60 X054 2811 1010 0000 0123 457")
    print(conto1.versa(2000))
    print(conto1.preleva(500))
    print(conto1.bonifico(conto2, 500))
    print(conto1.__str__())
    print(conto2.__str__())

if __name__ == "__main__":
    main()
        

