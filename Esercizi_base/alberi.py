class Nodo:
    """Nodo autoreferenziale per albero binario."""

    def _init_(self, valore, sx=None, dx=None): #classe che crea un nodo dell'alabero, 
                                                #più il suo nodo di destra e di sinistra
        self.valore = valore
        self.sx = sx
        self.dx = dx

    def inserisci(self, valore): 
        if valore > self.valore:
            if self.dx == None:
                self.dx = Nodo(valore)
            else:
                self.dx.inserisci(valore)
        elif valore < self.valore:
            if self.sx == None:
                self.sx = Nodo(valore)
            else:
                self.sx.inserisci(valore)
        
        return None

    def cerca(self, valore):
        if valore == self.valore:
            return True
        elif valore < self.valore:
            if self.sx != None:
                return self.sx.cerca(valore)
            else:
                return False
        elif valore > self.valore:
            if self.dx != None:
                return self.dx.cerca(valore)
            else:
                return False

    def _str_(self):
        return f"Nodo({self.valore}, sx={self.sx}, dx={self.dx})"



def main():
    radice = Nodo(5)
    for v in [3, 7, 1, 4, 6, 8]:
        radice.inserisci(v)
    
    print(radice)

    print(radice.cerca(4))            # True
    print(radice.cerca(9))            # False

if __name__ == "__main__":
    main()