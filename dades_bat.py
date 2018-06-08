##!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from codi.atributs.estructura import Entitat

if sys.platform == "win32" or sys.platform == "win64":
    os.system('cls')
else:
    os.system('clear')

from codi.atributs.dades import Dades
import numpy as np

f = open("taula.idx")
taula = f.readline()
f.close()

D = Dades(taula)
capcalera, molecules, nom_taula = D.entrades()
capca1 = D.get_header()
titol = D.get_title()
keywds = D.get_keywds()
descmol = D.get_compnd()
heterogenis = D.get_heterogenis()
models = D.get_models_dades()
latoms, latomsn, lhets, lhetsn = D.get_elements()
lresidus, lresidusn, lresiduts, lresidutsn, lreshets, lreshetsn = D.get_residus()
thelix = D.get_helix()
tsheet = D.get_sheet()
capca2 = "Taula: %s .- Nom complex:  %s" % (nom_taula, titol)
sub= np.repeat('-', len(capca1)+1)
s = ""
seq = s.join(sub)

print(capca1)
print(capca2)
print (seq)
print("Paraules clau: %s" % (keywds))
print
print("Nombre de models: %s" % (models))
print ("")
print("Descripcio de les molecules: ")
print("-----------------------------")
print("Nombre de molècules: %s" % (molecules))
print("")
for i in range(len(descmol)):
    print (descmol[i])
print("")
hets, cadenes, natoms, hetnams, hetsyn, formuls = D.get_heterogenis()
print("Els elements heterogenis del complex proteic ")
print ("--------------------------------------------")
for i in range(len(hets)):
    if hetnams[i].strip(" ") != "":
        print ("Molècula  " + (hets[i]) + " - " + (hetnams[i]) + " " + (hetsyn[i]) + " de la molècula " + (
        cadenes[i]) + "format per  " + (natoms[i]).strip(" ") + " àtoms " + " de formula " + (formuls[i]))
print ("")
print ("ESTRUCTURES SECUNDARIES")
print ("-----------------------")
print (thelix)
print(tsheet)
print ("")
text = ""
print ("ELEMENTS QUIMICS")
print ("-----------------")
print ("")
print ("Els elements quimics que formen part de la proteina exclosos els hidrogens")
print ("--------------------------------------------------------------------------")
numatoms = 0
for i in range(len(latoms)):
    numatoms = numatoms + int(latomsn[i])
    text = text + "( %s : %s ) " % (latoms[i], latomsn[i])
print (text)
print ("Total elements exclosos l'hidrogen: %d " % (numatoms))
print ("")
print ("Descripcio dels elements heterogens: ")
print ("-------------------------------------")
print ("Els elements quimics que no formen part de la proteina exclosos l' HOH")

text = ""
for i in range(len(lhets)):
    text = text + "( %s : %s )" % (lhets[i], lhetsn[i])
print(text)
text = ""
text2 = ""
print("")
numres = 0
numamino = 0
print ("RESIDUS")
print ("-------")
print ("")
print ("Els residus que formen part de la proteina que sòn aminoacids")
print ("-------------------------------------------------------------")
for i in range(len(lresidus)):
    numamino += 1
    numres = numres + int(lresidusn[i])
    if numamino <= 10:
        text = text + "( %s : %s ) " % (lresidus[i], lresidusn[i])
    else:
        text2 = text2 + "( %s : %s ) " % (lresidus[i], lresidusn[i])
print(text)
print(text2)

print ("Total tipus aminoacids: %d i total residus %d" % (numamino, numres))
print("")
text = ""
print ("Els residus que formen part de la proteina que no sòn aminoacids")
for i in range(len(lresiduts)):
    text = text + "( %s : %s ) " % (lresiduts[i], lresidutsn[i])
print(text)
print("")
text = ""
print ("Els residus hetrogenis que no formen  part de la proteina")
for i in range(len(lreshets)):
    text = text + "( %s : %s )" % (lreshets[i], lreshetsn[i])
print(text)
print(lresidus)