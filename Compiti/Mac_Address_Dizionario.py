def main():
    file = open("mac-vendors-export.csv", "r", encoding = 'utf-8')
    elenco = file.readlines()
    file.close()

    vendor = elenco[1:]

    print(vendor)

    

if __name__=="__main__": 
    main()
