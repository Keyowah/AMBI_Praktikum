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
        print("benoetigte Laufzeit:", runtime, "s")

def compute_prefix_function(pattern):
    m = len(pattern)
    pi = []
    pi.append(0)
    k = 0
    for q in range(1,m):
        while (k>0 and pattern[k]!=pattern[q]):
            k = pi[k]
        if pattern[k]==pattern[q]:
            k = k+1
        pi.append(k)
    return pi

def knuth_morris_pratt(text, pattern):
    # Start der Zeitmessung
    startTime = datetime.now()

    #Initialisierung
    cSchritt = 0
    cFunde = 0
    n = len(text)
    m = len(pattern)
    pi = computePrefixFunc(pattern)
    q = 0

    #Matching
    for i in range(0,n):
        while(q>0 and pattern[q]!=text[i]):
            q = pi[q-1]
        if pattern[q] == text[i]:
            q = q+1
        if q == m:
            print("Das Muster taucht mit Verschiebung", i+1-m, "auf")
            q = pi[q-1]
            cFunde += 1
        cSchritt += 1

    # Messungd er verbrauchten Zeit
    runtime = datetime.now() - startTime

    # nachdem der gesamte Text nach dem Pattern durchsucht wurde,
    # wird die Anzahl der Suchschritte ausgegeben
    print("Gesamt:", cFunde, "Fund(e)")
    print("Anzahl der Suchschritte:", cSchritt)
    print("benoetigte Laufzeit:", runtime)

def compute_last_occurence_function(p, m, sigma):
    lam = {}
    for a in sigma:
        lam.update({a:0})
    for j in range(0, m):
        lam[p[j]]=j
    return lam

def compute_good_suffix_function(p, m):
    pi = compute_prefix_function(p)
    p2 = p[::-1]
    pi2 = compute_prefix_function(p2)
    gamma = []
    for j in range(0, m):
        gamma.append(m-1-pi[m-1])
    for l in range(0, m):
        j = m-1-pi2[l]
        if gamma[j] > l-pi2[l]:
            gamma[j] = l-pi2[l]
    return gamma

def boyer_moore(t, p, sigma):
    n = len(t)
    m = len(p)
    lam = compute_last_occurence_function(p, m, sigma)
    gamma = compute_good_suffix_function(p, m)
    s = 0
    while s <= n-m:
        j = m-1
        print(j, s, p[j], t[s+j])
        while j >= 0 and p[j] == t[s+j]:
            print(j, s)
            j-=1
        if j==-1:
            print("Muster taucht mit Verschiebung", s-1, "auf.")
            s += gamma[0]
        else:
            s += max(gamma[j], j-lam[t[s+j]])


