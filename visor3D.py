##!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from codi.plot3D.proteina3D import Proteines
from codi.atributs.dades import Dades

f = open("taula.idx")
taula = f.readline()
f.close()
fitxer = taula
d = Dades(fitxer)
nresidus = d.get_nresidus()


taules = []


''' 
Tipus de representació
-----------------------------

1. Representació 3D del complex protèic seguns color aminoacids
5. Representació del complex per molècules
7. Representació per tipus aminoàcid
2. Representació dels elements externs a la proteina 
4. Representació ubicació d'un aminoacid concret dins la proteina 
3. Representació dels carbonis alfa units per les linees que representen els aminoacids
6. Representació en backbone
7. Representació del complex per tipus d'aminoàcids
'''

sws = 0

if len(sys.argv[1:]) < 2:
    raise SystemExit("S'han d'entrar un minim de 2 parametres")
tipus = str(sys.argv[1])
tipus2 = str(sys.argv[2])
try:
    tipus3 = str(sys.argv[3])
    sws = 1
except:
    tipus3 = ""
    sws = 0

# tipus = "c"
# tipus2 = "alfa"
# tipus = "atoms"
# tipus2 = "amino"
# tipus3 = "GLY"

""" Comprovacions """

param1 = ["a", "c"]
param2 = ["residu", "extern", "amino", "molecula", "alfa", "tipus"]
aminos = ('ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'PHE', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS', 'PRO', 'MET',
          'SER', 'THR', 'TYR', 'TRP', 'VAL')

if tipus not in param1:
    print("El primer paràmentre ha de ser: %s" % (str(param1)))
if tipus2 not in param2:
    print("El segon  paràmentre ha de ser: %s" % (str(param2)))
if sws == 1 and tipus3 not in aminos:
    print("El segon  paràmentre ha de ser: %s" % (str(aminos)))

if tipus == "a":
    tipus = "atoms"
if tipus == "c":
    tipus = "cadenes"

fet = 0
fet2 = 0

""" Representació dels ball & stick"""
if tipus == "cadenes" and tipus2 == "alfa":
    proteines = Proteines(3, fitxer)
    fet = 1

"""Representació en backbone"""
if tipus == "cadenes" and tipus2 == "tipus":
    proteines = Proteines(6, fitxer)
    fet = 1

if tipus == "atoms" and nresidus < 1300:
    """ Representació del complex proteic seguns color aminoàcids"""
    if tipus == "atoms" and tipus2 == "residu":
            proteines = Proteines(1, fitxer)
            fet = 1
    """ Representació dels elements externs a la proteina"""
    if tipus == "atoms" and tipus2 == "extern":
            proteines = Proteines(2, fitxer)
            fet = 1
    """7. Representació per tipus aminoàcid"""
    if tipus == "atoms" and tipus2 == "tipus":
            proteines = Proteines(7, fitxer)
            fet = 1
    """ Representació ubicació d'un aminoacid concret"""
    if tipus == "atoms" and tipus2 == "amino" and tipus3 != "":
            proteines = Proteines(4, fitxer, tipus3)
            fet = 1
    """ Representació del complex per molècules """
    if tipus == "atoms" and tipus2 == "molecula":
            proteines = Proteines(5, fitxer)
            fet = 1
elif tipus == "atoms":
    fet = 0
    fet2 = 1
    print("No es poden representar proteines amb forma atomica de mes de 1300 residus ")

if fet == 1:
    base.run()
else:
    if fet == 0 and fet2 ==0:
        print("La combinacio %s i %s %s no esta prevista" % (tipus, tipus2, tipus3))