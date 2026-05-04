class Libro:
    def __init__(self, titolo, autore, anno, pagine, letto = False):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.pagine = pagine
        self.letto = letto

    def eta(self, anno_corrente):
        return anno_corrente - self.anno
        # eta_libro = anno_corrente - self.anno
        # return eta_libro
    
    def e_classico(self, anno_corrente):
        return self.eta(anno_corrente) >= 50
        #     return True
        # else:
        #     return False
    
    def __str__(self):
        return f"{self.autore} - {self.titolo} ({self.anno}), {self.pagine}pp. [{'letto' if self.letto else 'non letto'}]"
    
def get_libri_letti(lista_libri):
    return [libro.titolo for libro in lista_libri if libro.letto]

def get_pubblicati_dopo(lista_libri, anno_soglia):
    return [libro for libro in lista_libri if anno_soglia < libro.anno]

def main():
    biblioteca = [
    Libro("Le città invisibili", "Italo Calvino", 1972, 164, True),
    Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 1178, False),
    Libro("Harry Potter e la pietra filosofale", "J.K. Rowling", 1997, 223, True),
    Libro("1984", "George Orwell", 1949, 328, False),
    Libro("L'amica geniale", "Elena Ferrante", 2011, 336, False),
    Libro("La Divina Commedia", "Dante Alighieri", 1320, 798, True),
    Libro("I Promessi Sposi", "Alessandro Manzoni", 1840, 724, True),
    Libro("Moby Dick", "Herman Melville", 1851, 635, False),
    Libro("Il grande Gatsby", "F. Scott Fitzgerald", 1925, 218, True),
    Libro("Frankenstein", "Mary Shelley", 1818, 280, True),
    Libro("Cent'anni di solitudine", "Gabriel García Márquez", 1967, 417, False),
    Libro("Orgoglio e pregiudizio", "Jane Austen", 1813, 432, True),
    Libro("Fondazione", "Isaac Asimov", 1951, 255, True),
    Libro("Ma gli androidi sognano pecore elettriche?", "Philip K. Dick", 1968, 256, False),
    Libro("Il nome della rosa", "Umberto Eco", 1980, 503, True),
    Libro("Il buio oltre la siepe", "Harper Lee", 1960, 281, False),
    Libro("Uno, nessuno e centomila", "Luigi Pirandello", 1926, 172, True),
    Libro("Il giovane Holden", "J.D. Salinger", 1951, 277, False),
    Libro("Gita al faro", "Virginia Woolf", 1927, 209, True),
    Libro("Don Chisciotte della Mancia", "Miguel de Cervantes", 1605, 1072, False)
    ]
    
    l = Libro("ciao", "lui", 2007, 200)
    print(l.eta(2026))
    print(l.e_classico(2026))
    print(l.__str__())
    print("---------------------------------------------------------------------------")
    lista_libri_letti = get_libri_letti(biblioteca)
    print(lista_libri_letti)
    print("---------------------------------------------------------------------------")
    lista_anno_soglia = get_pubblicati_dopo(biblioteca, 1800)
    # for libro in lista_anno_soglia:
    #     print(libro.__str__())
    [print(libro.__str__()) for libro in lista_anno_soglia]
    print("---------------------------------------------------------------------------")
    libri_letti_dopo = [libro for libro in get_pubblicati_dopo(biblioteca, 1950) if libro.letto]
    # for libro in libri_letti_dopo:
    #     print(libro.__str__())
    [print(libro.__str__()) for libro in libri_letti_dopo]

if __name__ == "__main__":
    main()