from tkinter import filedialog as tkf
from tkinter import Tk
from math import *
from datetime import datetime

Tk().withdraw() #Wir wollen kein Tk-Fenster haben, sondern nur den filedialog

def main():
    action1 = int(input("Woher soll der zu prüfende Text stammen?\n0: Aus \
Datei einlesen\n1: String eingeben\n"))
    if action1 == 0:
        print("Bitte Datei im Explorer auswählen...")
        path = tkf.askopenfilename(filetypes=[('Alle Dateien','*')],
                                   title = "Quelle für Text auswählen")
        t = open(path, 'r').read().replace('\n', '')
    else:
        t = input("Text:\n")
    action2 = int(input("Ok! Woher soll das zu suchende Muster stammen?\n0: Aus \
Datei einlesen\n1: String eingeben\n"))
    if action2 == 0:
        print("Bitte Datei im Explorer auswählen...")
        path = tkf.askopenfilename(filetypes=[('Alle Dateien','*')],
                                   title = "Quelle für Muster auswählen")
        p = open(path, 'r').read().replace('\n', '')
    else:
        p = input("Muster:\n")
    action3 = int(input("Ok! Welcher Algorithmus soll für die Suche verwendet \
werden?\n0: Naiver Algorithmus\n1: Rabin-Karp-Algorithmus\n2: Knuth-Morris-\
Pratt-Algorithmus\n3: Boyer-Moore-Algorithmus\n"))
    if action3 == 0:
        naiv(t, p)
    elif action3 == 1:
        rabin_karp(t, p, 10)
    elif action3 == 2:
        knuth_morris_pratt(t, p)
    else:
        boyer_moore(t, p)

def naiv(t, p):
    n = len(t)
    m = len(p)
    c = 0
    for s in range(0, n-m+1):
        if p==t[s:s+m]:
            print("Das Muster taucht mit Verschiebung", s, "auf.")
            c+=1
    print("Gesamt:", c, "Fund(e)." )
    

def rabin_karp(text, pattern, d):
    # Start der Zeitmessung
    startTime = datetime.now()

    # Initialisierung
    cSchritte = 1
    cFunde = 0
    q = 13
    n = len(text)
    m = len(pattern)
    h = pow(d, m - 1) % q
    p = 0
    t = 0

    # Preprocessing
    for i in range(1, m + 1):
        p = ((d * p) + pattern[i - 1]) % q
        t = ((d * t) + text[i - 1]) % q

        # Matching
        for s in range(n - m + 1):
            if p == t:
                if pattern == text[s:s + m]:
                    cFunde+=1
                    print("Das Muster taucht mit Verschiebung", s, "auf")
        if s < (n - m):
            t = (text[s + m] + d * (t - text[s] * h)) % q
        cSchritte+=1

        # Messungd er verbrauchten Zeit
        runtime = datetime.now() - startTime

        # nachdem der gesamte Text nach dem Pattern durchsucht wurde,
        # wird die Anzahl der Suchschritte ausgegeben
        print("Gesamt:", cFunde, "Fund(e)")
        print("Anzahl der Suchschritte:", cSchritte)
        print("benoetigte Laufzeit:", time, "s")


def knuth_morris_pratt(t, p):
    n = len(t)
    m = len(p)
    c = 0

def boyer_moore(t, p):
    print()

main()
