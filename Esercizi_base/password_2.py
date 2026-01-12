password = input("Inserisci una password: ")
password_blanked = password[0] + "*"*(len(password) - 1)
print(f"Hai inserito la password: {password_blanked}")

password = input("Inserisci una password: ")
password_blanked = password[0] + "*"*(len(password) - 2) + password[-1]
print(f"Hai inserito la password: {password_blanked}")
