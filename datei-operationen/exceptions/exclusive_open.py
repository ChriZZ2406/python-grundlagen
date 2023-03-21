import os
import math


try:
# datei öffnen zum schreiben
    datei = open("text.txt", "x")

# zu schreibender text definieren
    text = "hallo das ist ein text"

#t ext in datei schreiben
    datei.write(text)

# datei schließen
    datei.close()
except FileExistsError:
    eingabe = input("hey etwas ist schief gelaufen - delete? J/N? ")
    if eingabe.capitalize() == "J":
        os.remove("text.txt")# lösche datei


except:
    print("nope")