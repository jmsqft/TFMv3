##!/usr/bin/env python
# -*- coding: utf-8 -*-
from codi.plot2D.proteina2D import Plots
import sys
import os

if len(sys.argv[1:]) != 2:
    raise SystemExit("S'han d'entrar d'un minim de 2 parametres")

tipus1  = str(sys.argv[1])
tipus2  = str(sys.argv[2])

param1 = ["a", "c"]
param2 = ["molecula", "residu", "tipus", "vistes"]

if tipus1 not in param1:
    print("El primer paràmentre ha de ser: %s" % (str(param1)))

if tipus2 not in param2:
    print("El segon  paràmentre ha de ser: %s" % (str(param2)))

fet = 0

if tipus1 == "a":
    tipus1 = "atoms"
if tipus1 == "c":
    tipus1 = "cadenes"

if tipus1 == "atoms" and tipus2 == "molecula":
    plots = Plots(1)  # Proteina per atoms
    dades = plots.plot_atoms()
    fet = 1

"""Representació en pseudo-3d dels atoms """
if tipus1 == "atoms" and tipus2 == "residu":
    plots = Plots(2)  # Proteina per residus
    dades = plots.plot_atoms()
    fet = 1

"""Representació en linies dels residus en pseudo 3D """
if tipus1 == "cadenes" and tipus2 == "molecula":
    plots = Plots(1)
    dades = plots.plot_linies()
    fet = 1

"""Representació en linies dels residus en pseudo 3D segon naturalesa dels residus """
if tipus1 == "cadenes" and tipus2 == "tipus":
    plots = Plots(2)
    dades = plots.plot_linies()
    fet = 1

"""Representació en 2D i pseudo 3D"""
if tipus1 == "atoms" and tipus2 == "vistes":
    plots = Plots(1)
    dades = plots.plot2d_3d()
    fet = 1

if fet == 0:
    print("La combinació %s i %s no està prevista" % (tipus1, tipus2))
