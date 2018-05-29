# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 09:14:01 2018

@author: alexm
"""

from functools import reduce
import time
 
def gen_row(w, s):
    """Créer toutes les solutions pour chaque colonne et ligne possibles pour la run."""
    
    def gen_seg(o, sp):
        if not o:
            return [[2] * sp]
        return [[2] * x + o[0] + tail 
                for x in range(1, sp - len(o) + 2)
                for tail in gen_seg(o[1:], sp - x)]
 
    return [x[1:] for x in gen_seg([[1] * i for i in s], w + 1 - sum(s))]
 

def deduce(hr, vr):
    """On ajoute les cases obligatoirement noircies."""
    
    def allowable(row):
        return reduce(lambda a, b: [x | y for x, y in zip(a, b)], row)
 
    def fits(a, b):
        """Notre liste correspond t'elle à la solution possible ?"""
        return all(x & y for x, y in zip(a, b))
 
    def fix_col(n):
        """ On vérifie si une colonne a des valeurs fixes."""
        # print("----------------------------",n,"-------------------------")
        c = [x[n] for x in can_do]
        # Récupère toutes les combinaisons possibles pour la colonne n
        cols[n] = [x for x in cols[n] if fits(x, c)]
        # On vient ajouter une solution si elle est unique
        for i, x in enumerate(allowable(cols[n])):
            if x != can_do[i][n]:
                mod_rows.add(i)
                can_do[i][n] &= x
 
    def fix_row(n):
        """Pareil pour les lignes"""
        c = can_do[n]
        # Récupère toutes les combinaisons possibles pour la ligne n
        rows[n] = [x for x in rows[n] if fits(x, c)]
        # On vient ajouter une solution si elle est unique
        for i, x in enumerate(allowable(rows[n])):
            if x != can_do[n][i]:
                mod_cols.add(i)
                can_do[n][i] &= x
 
    def show_gram(m):
        # Un 'x' est une erreur.
        # Un '?' nécéssite plus de travail
        
        for x in m:
            file.write(" ".join("x#.?"[i] for i in x)+"\n") 
            print(" ".join("x#.?"[i] for i in x))
        file.write("\n")
        print()
 
    w, h = len(vr), len(hr)
    rows = [gen_row(w, x) for x in hr]
    cols = [gen_row(h, x) for x in vr]
    can_do = list(map(allowable, rows))
 
    # On init les lignes et colonnes.
    mod_rows, mod_cols = set(), set(range(w))
    while mod_cols:
        for i in mod_cols:
            fix_col(i)
        mod_cols = set()
        for i in mod_rows:
            fix_row(i)
        mod_rows = set()
 
    # S'il n'y a plus de 3 (inconnu), solution unique
    if all(can_do[i][j] in (1, 2) for j in range(w) for i in range(h)):
        print("Solution probablement unique")  # peut être incorrect!
    # Sinon solution multiple
    else:
        print("Solution probablement non unique, recherche suplémentaire:")
 

    out = [0] * h
 
    def try_all(n = 0):
        if n >= h:
            for j in range(w):
                if [x[j] for x in out] not in cols[j]:
                    return 0
            show_gram(out)
            return 1
        sol = 0
        for x in rows[n]:
            out[n] = x
            sol += try_all(n + 1)
        return sol
 
    n = try_all()
    if not n:
        print("Pas de solution.")
    elif n == 1:
        print("Solution unique.")
    else:
        print(n, "solutions.")
    print()


def solve(p, show_runs=True):
    s = [[[ord(c) - ord('A') + 1 for c in w] 
        for w in l.split()]
        for l in p.splitlines()]
    if show_runs:
        print("Horizontal:", s[0])
        print("Vertical:", s[1])
    deduce(s[0], s[1])


def main():
    
    # Read problems from file.
    
    fn = "pbs_python.txt"
    for p in (x for x in open(fn).read().split("\n\n") if x):
        start_time = time.time()
        solve(p, False)
        print("--- %s Mseconds ---" % str((time.time() - start_time) *1000))

file = open("result_python.txt","w") 
main()
file.close()