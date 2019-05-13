import sys
from tkinter import filedialog as tkf
from tkinter import Tk
from math import *
from datetime import datetime

Tk().withdraw() # Wir wollen kein Tk-Fenster haben, sondern nur den filedialog

''' Verwendete Variablen

t = der zu durchsuchende Text
p = der zu findende Pattern
m = Laenge des Textes
sigma = Liste der Character im uebergebenen Text
'''


def main(*args, **kwargs):
    """
    Die main() stellt die Schnittstelle zum Benutzer. Hier werden alle benoetigten Eingaben abgefragt und die
    gewuenschten Algorithmen mit den entsprechenden Parametern aufgerufen. Wenn es zu einem Eingabefehler kommt,
    startet das Programm neu.
    """

    action1 = input("Woher soll der zu prüfende Text stammen?\n"
                        "0: Aus Datei einlesen\n"
                        "1: String eingeben\n"
                        "Mit 'help' lässt sich ein Hilfetext ausgeben.\n")
    if action1 == "0":
        print("Bitte eine Datei im Explorer auswählen...")
        path = tkf.askopenfilename(filetypes=[('Alle Dateien', '*')], title="Quelle für Text auswählen")
        t = open(path, 'r').read().replace('\n', '')
    elif action1 == "1":
        t = input("Text:\n")
    elif action1 == "help":
        help()
    else:
        print("Eingabe konnte nicht gelesen werden. Programm wird neugestartet.\n")
        main()

    action2 = input("Ok! Woher soll das gesuchte Pattern stammen?\n"
                        "0: Aus Datei einlesen\n"
                        "1: String eingeben\n"
                        "Mit 'help' lässt sich ein Hilfetext ausgeben.\n")
    if action2 == "0":
        print("Bitte eine Datei im Explorer auswählen...")
        path = tkf.askopenfilename(filetypes=[('Alle Dateien', '*')], title="Quelle für Muster auswählen")
        p = open(path, 'r').read().replace('\n', '')
    elif action2 == "1":
        p = input("Muster:\n")
    elif action2 == "help":
        help()
    else:
        print("Eingabe konnte nicht gelesen werden. Programm wird neugestartet.\n")
        main()

    action3 = input("Ok! Welcher Algorithmus soll für die Suche verwendet werden?\n"
                        "0: Naiver Algorithmus\n"
                        "1: Rabin-Karp-Algorithmus\n"
                        "2: Knuth-Morris-Pratt-Algorithmus\n"
                        "3: Boyer-Moore-Algorithmus\n"
                        "4: Alle 4 Algorithmen\n"
                        "Mit 'help' lässt sich ein Hilfetext ausgeben.\n")
    if action3 == "0":
        naiv(t, p)
    elif action3 == "1":
        rabin_karp(t, p, len(generate_sigma(t)))
    elif action3 == "2":
        knuth_morris_pratt(t, p)
    elif action3 == "3":
        boyer_moore(t, p, generate_sigma(t))
    elif action3 == "4":
        naiv(t, p)
        rabin_karp(t, p, len(generate_sigma(t)))
        knuth_morris_pratt(t, p)
        boyer_moore(t, p, generate_sigma(t))
    elif action3 == "help":
        help()
    else:
        print("Eingabe konnte nicht gelesen werden. Programm wird neugestartet.\n")
        main()


def help():
    print(
        "*** AMBI-Praktikum Aufgabe 1 - Bediedungsanleitung ***\n\n"
        "\tMit diesem Programm können zwei Zeichenketten mit verschiedenen\n"
        "\tAlgorithmen verglichen werden\n"
        "\tZeichenketten können entweder als String oder Datei übergeben werden.\n"
        "\tReihenfolge der Eingaben:\n"
        "\t\t1. Wählen Sie eine Eingabemethode für den zu überprüfenden Text\n"
        "\t\t(String oder .fasta Datei) mit den Ziffern 0, 1\n"
        "\t\t2. Wählen Sie eine .fasta Datei oder geben Sie einen String ein\n"
        "\t\t3. Wählen Sie eine Eingabemethode für das gesuchte Pattern\n"
        "\t\t(String oder Pattern) mit den Ziffern 0, 1\n"
        "\t\t4. Wählen Sie einen Algorithmus für die Auswertung.\n"
        "\t\tDafür stehen zur Verfügung:\n"
        "\t\t\t0: Naiver Algorithmus\n"
        "\t\t\t1: Rabin-Karp-Algorithmus\n"
        "\t\t\t2: Knuth-Morris-Pratt-Algorithmus\n"
        "\t\t\t3: Boyer-Moore-Algorithmus\n"
        "\t\t\t4: Alle 4 Algorithmen\n\n"
        "Das Programm wird neugestartet.\n"
    )


def naiv(text, pattern):
    """
    Der Algorithmus ueberprueft nacheinander jede Stelle zwischen 0 und n-m im Text als potenziellen Anfang des Patterns.
    Daher wird jede Stelle im Text bis zu m mal betrachtet.
    :param t: der zu ueberpruefende Text, string
    :param p: das gesuchte Pattern, string
    :Ausgabe: der Algorithmus gibt die Verschiebungen fuer alle gefunden Pattern im Text an.
    Ausserdem wird die Anzahl der Funde und die benoetigte Anzahl der Vergleiche von Text und Pattern
    gezaehlt und die Laufzeit gemessen und ausgegeben.
    """
    print("\n*** Naiv ***\n")

    start_time = datetime.now()  # Start der Zeitmessung

    n = len(text)
    m = len(pattern)
    c_funde = 0
    c_schritte = 0
    for s in range(0, n - m + 1):
        # Pruefe, ob pattern mit Verschiebung s im text auftaucht
        ident = 0
        for i in range(0, m):
            c_schritte += 1 # nachfolgenden Vergleich zählen
            if pattern[i] == text[s+i]:
                ident += 1
            else:
                break
        if ident == m:
            print("Das Muster taucht mit Verschiebung", s, "auf.")
            c_funde += 1

    # Messung der verbrauchten Zeit
    runtime = datetime.now() - start_time

    print("Gesamt:", c_funde, "Fund(e)")
    print("Anzahl der Suchschritte:", c_schritte)
    print("Benoetigte Laufzeit:", runtime)


def rabin_karp(text, pattern, d):
    """
    Der Algorithmus bestimmt fuer jeden Textabschnitt der Groesse m iterativ einen Hashwert mit Hilfe der Horners Rule. Die
    betrachteten Buchstaben werden in ihre ASCII Werte umgewandelt, damit mit ihnen gerechnet werden kann. Der in einem
    Schritt betrachtetete Textabschnitt kann nur dem Pattern entsprechen, wenn deren Hash-Werte gleich sind.
    :param text: zu ueberpruefender Text, string
    :param pattern: gesuchtes Pattern, string
    :param d: Groesse des Alphabets von Text
    :Ausgabe: der Algorithmus gibt die Verschiebungen fuer alle gefunden Pattern im Text an.
    Ausserdem wird die Anzahl der Funde und die benoetigte Anzahl der Vergleiche von Text und Pattern
    gezaehlt und die Laufzeit gemessen und ausgegeben.
    """
    print("\n*** Rabin-Karp ***\n")

    start_time = datetime.now()  # Start der Zeitmessung

    # Initialisierung
    c_schritte = 0
    c_funde = 0
    q = 61
    n = len(text)
    m = len(pattern)
    p = 0
    t = 0
    # Damit pow(d,m-1) keinen Overflow produzieren kann, verwenden wir
    # (x * y) mod q = (x mod q)*(y mod q) mod q zur Berechnung von h= pow(d,m-1) % q
    h = d % q
    for i in range (1, m - 1): # nur bis m-2 weil h=h^1 schon vorliegt
        h = (h * (d % q)) % q
        
    # Berechnung der Hash-Werte von pattern und den ersten m Stellen von text
    for i in range(0, m):
        p = ((d * p) + ord(pattern[i])) % q
        t = ((d * t) + ord(text[i])) % q

    # Suche nach einem gueltigen Matching. Die aktuelle Position im text muss
    # ueberprueft werden, wenn die Hash-Werte gleich sind. Anschliessend wird
    # der Hash-Wert fuer die Stellen s+1,...,s+m aktualisiert.
    for s in range(0, n - m + 1):
        if p == t:
            ident = 0
            for i in range(0, m):
                c_schritte += 1 # nachfolgenden Vergleich zählen
                if pattern[i] == text[s+i]:
                    ident += 1
                else:
                    break
            if ident == m:
                print("Das Muster taucht mit Verschiebung", s, "auf.")
                c_funde += 1
        if s < (n - m):
            t = (ord(text[s + m]) + d * (t - ord(text[s]) * h)) % q

        # Messung der verbrauchten Zeit
        runtime = datetime.now() - start_time

    # nachdem der gesamte Text nach dem Pattern durchsucht wurde,
    # wird die Anzahl der Suchschritte ausgegeben
    print("Gesamt:", c_funde, "Fund(e)")
    print("Anzahl der Suchschritte:", c_schritte)
    print("benoetigte Laufzeit:", runtime)

    
def compute_prefix_function(pattern):
    """
    Der Algorithmus ueberprueft den Pattern nach shifts in sich selbst.
    :param pattern: zu ueberpruefendes Pattern
    :return: __pi[i] ist die Laenge des laengsten Praefixes von pattern, der ein Suffix von pattern[1,..,i] ist
    """
    m = len(pattern)
    __pi = [0]
    k = 0
    k_alt = 0
    # Ermittlung der Eintraege 1 bis m-1 von __pi
    for q in range(1, m):        
        while k > 0 and pattern[k] != pattern[q]:
            k_alt = k
            k = __pi[k]
            # Verhinderung einer Endlosschleife, falls k = __pi[k] 
            if k == k_alt:
                k = 0
        if pattern[k] == pattern[q]:
            k = k + 1
        __pi.append(k)
    return __pi


def knuth_morris_pratt(text, pattern):
    """
    Funktioniert aehnlich wie der Ansatz mittels DFA. Nutzt Enthaltensein des Patterns in sich selbst aus, um bessere
    Erhoehungen des Shifts s zu erreichen. Liest dafuer den gesamten Text von links nach rechts.
    :param text: zu ueberpruefendes Pattern, string
    :param pattern: gesuchtes Pattern, string
    :Ausgabe: der Algorithmus gibt die Verschiebungen fuer alle gefunden Pattern im Text an.
    Ausserdem wird die Anzahl der Funde und die benoetigte Anzahl der Vergleiche von Text und Pattern
    gezaehlt und die Laufzeit gemessen und ausgegeben.
    """
    print("\n*** Knuth-Morris-Pratt ***\n")

    start_time = datetime.now()  # Start der Zeitmessung

    # Initialisierung
    c_schritte = 0
    c_funde = 0
    n = len(text)
    m = len(pattern)
    # Vorverarbeitung des Patterns fuer Werte fuer Enthaltensein in sich selbst
    __pi = compute_prefix_function(pattern)
    q = 0
    # q haelt fest, wie weit der pattern an der aktuellen Stelle im Text bisher gematcht wurde (wie bei DFA)
    # das Matching erfolgt beim Lesen des Texts Buchstabe fuer Buchstabe (wie bei DFA)
    for i in range(0, n):
        while q > 0 and pattern[q] != text[i]:
            # Wie weit muss q reduziert werden? Das steht an der entsprechenden Stelle in __pi
            q = __pi[q - 1]
        c_schritte += 1 # den nachfolgenden Vergleich zählen
        if pattern[q] == text[i]:
            # Ein weiteres Zeichen wurde gematcht
            q = q + 1
        if q == m:
            print("Das Muster taucht mit Verschiebung", i - m + 1, "auf.")
            # Aktualisieren von q wie oben
            q = __pi[q - 1]
            c_funde += 1

    # Messung der verbrauchten Zeit
    runtime = datetime.now() - start_time

    print("Gesamt:", c_funde, "Fund(e)")
    print("Anzahl der Suchschritte:", c_schritte)
    print("Benoetigte Laufzeit:", runtime)


def compute_last_occurence_function(pattern, m, sigma):
    """
    Funktion zur Realisierung der bad-character Heuristik.
    Findet das letzte Auftreten fuer jeden Buchstaben im Alphabet im Pattern und gibt ein Dictionary
    mit den entsprechenden Paaren zurueck.
    :param pattern: zu ueberpruefendes Pattern, string
    :param m: Laenge von pattern
    :param sigma: Alphabet des Textes, in dem der Pattern gesucht wird
    :return: ein Dictionary der Form {Buchstabe: letzte Position im Pattern}
    """
    lam = {}
    for a in sigma:
        lam.update({a: 0})
    for j in range(0, m):
        lam[pattern[j]] = j
    return lam


def compute_good_suffix_function(pattern, m):
    """
    Funktion zur Realisierung der good-suffix Heuristik.
    Gibt fuer jede Position 0<=j<=m-1 an, wie weit der Pattern verschoben werden darf, ohne ein Mismatch
    des bisher gematchten 'good-suffix' im Text mit dem Pattern zu erzeugen oder ein Matching zu verpassen.
    :param pattern: zu ueberpruefendes Pattern, string
    :param m: Laenge von pattern
    :return: Eine Liste mit den obig beschriebenen Werten fuer jede Position 0<=j<=m-1 im Pattern
    """

    # Vorverarbeitung des Patterns
    __pi = compute_prefix_function(pattern)
    pattern2 = pattern[::-1] # umgekehrtes Pattern
    pi2 = compute_prefix_function(pattern2)
    # Initialisierung der Liste
    __gamma = []
    # Ermittle Einträge gemaess Rechnung aus der Vorlesung
    for j in range(0, m):
        __gamma.append(m - __pi[m-1])
    for l in range(0, m):
        j = m-1 - pi2[l]
        if __gamma[j] > l+1 - pi2[l]:
            __gamma[j] = l+1 - pi2[l]
    return __gamma


def boyer_moore(t, p, sigma):
    """
    Der Algorithmus funktioniert wie der naive Algorithmus, nur dass er das Muster jeweils
    von rechts nach links liest und bei Mismatches durch Anwendung von Heuristiken bessere
    Erhöhungen des Shifts s als 1 erzielt. Die Heuristiken heissen bad-character und good-suffix.
    :param t:
    :param p:
    :param sigma:
    :Ausgabe: der Algorithmus gibt die Verschiebungen fuer alle gefunden Pattern im Text an.
    Ausserdem wird die Anzahl der Funde und die benoetigte Anzahl der Vergleiche von Text und Pattern
    gezaehlt und die Laufzeit gemessen und ausgegeben.
    """
    print("\n*** Boyer-Moore ***\n")

    start_time = datetime.now()  # Start der Zeitmessung

    c_schritte = 0
    c_funde = 0
    n = len(t)
    m = len(p)
    # Woerterbuch fuer bad-character Heuristik
    lam = compute_last_occurence_function(p, m, sigma)
    # Liste fuer good-suffix Heuristik
    __gamma = compute_good_suffix_function(p, m)
    s = 0
    # es gibt n - m + 1 mögliche shifts
    while s <= n - m:
        # durchlaufe das Muster von hinten nach vorne
        j = m - 1
        c_schritte += 1 # nachfolgenden Vergleich zählen
        while j >= 0 and p[j] == t[s + j]:
            c_schritte += 1 # Vergleich für die Bed. des nächsten Durchlaufs
            j -= 1
        if j == -1:
            c_schritte -= 1 # While-Bed ist schon an j>=0 gescheitert
            print("Das Muster taucht mit Verschiebung", s, "auf.")
            # Anwendung der good-suffix Heuristik fuer j=0
            s += __gamma[0]
            c_funde += 1
        else:
            # Ermittlung, welche der beiden Heuristiken die größere Verschiebung liefert
            s += max(__gamma[j], j - lam[t[s + j]])

    # Messung der verbrauchten Zeit
    runtime = datetime.now() - start_time

    print("Gesamt:", c_funde, "Fund(e)")
    print("Anzahl der Suchschritte:", c_schritte)
    print("Benoetigte Laufzeit:", runtime)


def generate_sigma(text):
    """
    Generiert eine Liste von einzigartigen Buchstaben aus der Zeichenkette text,
    also das zugehoerige Alphabet.
    :return: Alphabet von text
    """
    return list(set(list(text)))


if __name__ == "__main__":
    main()
