##!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from codi.atributs.atributs import Atributs

so =sys.platform
if so == 'win32' or  so=="win64":
    os.system('cls')
else:
    os.system('clear')


a = Atributs()
nom, lletra,  sig, volum, tipus1, tipus2, escala = a.llista_aminoacids()
frase = "Aminoàcid".ljust(15, " ") + " SIG "+"Lletra  " + "Tipologia" +"  " +"Masa relativa(*) "
print(frase)
print "--------------- ----- ---- ---------  ------------"
for i in range(len(sig)):
    frase= nom[i].ljust(15, " ") +" "+ sig[i].ljust(3, " ")+"    "+lletra[i] +"       " + str(tipus2[i])+ "     "+ str(escala[i])
    print(frase)
print(" ")
print (" * massa relativa a la massa de la Glicina = 1 ")
print(" ")
tipologia = ( 'Tipologia   Descripció',
'----------------------',
'      1	Hidrofòbics',
'      2	Hidrofílics',
'      3	Àcids',
'      4	Bàsics' )

for i in tipologia:
    print i


