##!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from codi.atributs.dades import Dades
from codi.atributs.pat import pat

so = sys.platform
if so == 'win32' or so == "win64":
    os.system('cls')
else:
    os.system('clear')

n = 0
taules = []
dict = {}
keyValue = []
menu = []

pat = pat("db")


def sencer(resposta):
    try:
        int(resposta)
        return resposta
    except:
        return 0

for file in os.listdir("codi/dades_pdb"):
    if file.endswith(".pdb"):
        n += 1
        keyValue = []
        keyValue.append(n)
        keyValue.append(file)
        d = Dades(file)
        nresidus = d.get_nresidus()
        dict[keyValue[0]] = keyValue[1]
        titol = d.get_title()
        menu.append("%d .- %s   - %s  .- Residus: %s "  % (n, file, d.get_title(), nresidus))

cap = "Escollir un fitxer"
print (cap)
print('-' * len(cap))
n = len(menu)


for i in range(n):
    print menu[i]
resposta = ""
while resposta == "":
    resposta = raw_input('\nOpcio : ').lower()
    if sencer(resposta) != 0 and 0 < int(resposta) <= n:
        f = open("taula.idx","w")
        text = dict[int(resposta)]
        f.write(text)
        f.close()
        break
    else:
        resposta = ""

