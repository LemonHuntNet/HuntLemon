from pathlib import Path

#introduzione

print("---HuntLemon---")
print("Benvenuto in HuntLemon, qui puoi cercare le tue cartelle.")
print("Come ti chiami?")
nome = input(": ")
print(f"Benvenuto {nome}")
print("per chiudere lo script premere 'b'.")

attivo = True

#inizio

while attivo:
    
    scelta = input(f"In quale cartella vuoi andare, {nome}? ")
   
    if scelta.strip().lower() == 'b':
        break
    
    if scelta.strip().lower() == "downloads":
        print("Ecco i file Downloads")

        percorso = Path("C:/Users/User/Downloads")

        for file in percorso.iterdir():
            print(file.name)

    elif scelta.strip().lower() == "desktop":
        print("ecco i file desktop".title())

        percorso = Path("C:/Users/User/Desktop")

        for file in percorso.iterdir():
            print(file.name)
    
    elif scelta.strip().lower() == 'onedrive':
        print("Ecco i file OneDrive")

        percorso = Path("C:/Users/User/OneDrive")

        for file in percorso.iterdir():
            print(file.name)

    elif scelta.strip().lower() == "appdata":
        print("Ecco le cartelle di AppData")

    percorso = Path("C:/Users/user/AppData")

    if percorso.exists():
        for file in percorso.iterdir():
            print(file.name)
    else:
        print("Cartella AppData non trovata!")

