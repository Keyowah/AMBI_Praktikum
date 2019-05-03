from tkinter import filedialog as tkf
from tkinter import Tk

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
        rabin_karp(t, p)
    elif action3 == 2:
        knuth_morris_pratt(t, p)
    else:
        boyer_moore(t, p)

def naiv(t, p):
    n = len(t)
    m = len(p)
    c = 0
    for s in range(0, n-m+1):
        if p[0:m]==t[s:s+m]:
            print("Das Muster taucht mit Verschiebung", s, "auf.")
            c+=1
    print("Gesamt:", c, "Fund(e)." )

def rabin_karp(t, p):
    print()

def knuth_morris_pratt(t, p):
    n = len(t)
    m = len(p)
    c = 0

def boyer_moore(t, p):
    print()

main()
