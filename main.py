def main():
    action1 = input("bla")

def naiv(t, p):
    n = len(t)
    m = len(p)
    c = 0
    for s in range(0, n-m+1):
        if p[0:m]==t[s:s+m]:
            print("Das Muster", p, "taucht mit Verschiebung", s, "auf.")
            c+=1
    print("Gesamt:", c, "Fund(e)" )

def rabin_karp(t, p):
    print()

def knuth_morris_pratt(t, p):
    print()

def boyer_moore(t, p):
    print()
