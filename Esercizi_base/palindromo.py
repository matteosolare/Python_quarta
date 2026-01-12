a = input("inserire una stringa: ")
a = a.lower()
print(a)
if a == a[::-1]:
    print("la stringa è palindroma")
else:
    print("la stringa non è palindroma")