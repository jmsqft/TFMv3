#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib

import matplotlib.pyplot as plt

from codi.atributs.atributs import Atributs
from codi.atributs.atributs import Colors
from codi.atributs.estructura import Entitat

importlib.import_module('mpl_toolkits.mplot3d').__path__



class Plots(object):

    def __init__(self, tipus, tipus2 = None):
        f = open("taula.idx")
        taula = f.readline()
        f.close()
        self.fitxer = taula
        e = Entitat(self.fitxer)
        dadestotals = e.crear_entitat()
        self.capcalera = dadestotals[0]
        self.molecules = dadestotals[2]
        self.residus = dadestotals[3]
        self.atoms = dadestotals[4]
        self.nom_taula = dadestotals[5]
        self.tipus = tipus
        self.frase = ""

    def plot_atoms(self):
        xs = []
        ys = []
        zs = []
        cs = []
        watoms = []
        if self.tipus == 1:
            watoms = [atom for atom in self.atoms if atom[Atributs.atomt("idTAtom")] == True]
        if self.tipus == 2:
            watoms = [residu for residu in self.residus if residu[Atributs.residut("idTResidu")] == True]
        self.tipus2 = 1
        for linia in watoms:
            if self.tipus == 1:
                x = linia[Atributs.atomt("xcoor")]
                y = linia[Atributs.atomt("ycoor")]
                z = linia[Atributs.atomt("zcoor")]
            if self.tipus == 2:
                x = linia[Atributs.residut("xcoor")]
                y = linia[Atributs.residut("ycoor")]
                z = linia[Atributs.residut("zcoor")]

            # Get color
            chain = linia[Atributs.atomt("idChain")]
            colors = Colors(chain,1)
            col = colors.color_molecula()

            xs.append(x)
            ys.append(y)
            zs.append(z)
            cs.append(col)

        fig = plt.figure(figsize=(10, 5))
        ax = fig.add_subplot(111, projection='3d')
        ax.set_facecolor([0.98, 0.92, 0.84])  # blanc antic
        ax.text2D(-0.10, 0.95,  self.capcalera,
                  horizontalalignment='left',
                  verticalalignment='top',
                  family='Serif',
                  size= 9,
                  transform=ax.transAxes)
        ax.scatter(xs, ys, zs, c=cs, marker='o',alpha=0.35)
        ax.set_xlabel('Eix X')
        ax.set_ylabel('Eix Y')
        ax.set_zlabel('Eix Z')
        plt.show()

    ########################################################333

    def plot_linies(self):
        # Coordenades
        tx = 0.0
        ty = 0.0
        tz = 0.0
        txp = 0.0
        typ = 0.0
        tzp = 0.0
        self.tipus2 = 2
        fig = plt.figure(figsize=(11, 5))
        ax = fig.add_subplot(111, projection='3d')
        ax.set_facecolor([0.98,0.92,0.84])  # blanc antic

        ax.text2D(-0.10, 0.95,  self.capcalera,
                  horizontalalignment='left',
                  verticalalignment='top',
                  family='Serif',
                  size= 9,
                  transform=ax.transAxes)

        # ax.text2D(0.05, 0.95, self.capcalera, transform=ax.transAxes)

        # Posicions en el refistre de residus
        chain = Atributs.residut("idChain")
        s = Atributs.residut("idResidu")
        amin = Atributs.residut("nomResidu")
        x = Atributs.residut("xcoor")
        y = Atributs.residut("ycoor")
        z = Atributs.residut("zcoor")
        prot = Atributs.residut("idTResidu")

        # Vectors plot
        punt_inici_x = []
        punt_inici_y = []
        punt_inici_z = []
        punt_final_x = []
        punt_final_y = []
        punt_final_z = []

        colamin = []

        # Nomes aminoacids de la proteina residu[prot] == True

        cadena = [residu for residu in self.residus if residu[prot] == True]

        residus_net = cadena
        n = len(residus_net) - 1
        for i in range(n):
            linia = residus_net[i]
            chain1 = linia[chain]
            amino = linia[amin]
            tx = linia[x]
            ty = linia[y]
            tz = linia[z]
            res1 = [chain1 + str(linia[s])]
            if i < n:
                liniapost = residus_net[i + 1]
                chain2 = liniapost[chain]
                txp = liniapost[x]
                typ = liniapost[y]
                tzp = liniapost[z]
                res2 = [chain2 + str(liniapost[s])]
            else:
                pass

            # Get color
            if self.tipus == 1:
                colors = Colors(chain1,1)
                cl = colors.color_molecula()
            elif self.tipus == 2:
                aminos = ('ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'PHE', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE',
                                   'LEU', 'LYS', 'PRO', 'MET', 'SER', 'THR', 'TYR', 'TRP', 'VAL')
                if amino in aminos:
                    ccolors = Colors(amino,2)
                    cl = ccolors.color_tipus()
                else:
                    cl = ('k')
            else:
                cl = ('c')

            punt_inici_x.append(tx)
            punt_inici_y.append(ty)
            punt_inici_z.append(tz)
            colamin.append(cl)

            if i < n and chain1 == chain2:
                punt_final_x.append(txp)
                punt_final_y.append(typ)
                punt_final_z.append(tzp)
            else:
                punt_final_x.append(tx)
                punt_final_y.append(ty)
                punt_final_z.append(tz)

        for i in range(n):
            xs = [punt_inici_x[i], punt_final_x[i]]
            ys = [punt_inici_y[i], punt_final_y[i]]
            zs = [punt_inici_z[i], punt_final_z[i]]
            col = colamin[i]
            ax.plot(xs, ys, zs, linewidth=2, color=col )
            # linea = []
            # linea = [x for x in punt_inici_x if x == 0]

        # ax.set_xlabel('Eix X')
        # ax.set_ylabel('Eix Y')
        # ax.set_zlabel('Eix Z')
        plt.show()

    #########################################

    def plot2d_3d(self):
        fig = plt.figure(figsize=(11, 5))
        ax = fig.add_subplot(111, projection='3d')
        ax.text2D(-0.10, -0.10,  self.capcalera,
                  horizontalalignment='left',
                  verticalalignment='top',
                  family='Serif',
                  size= 8,
                  transform=ax.transAxes)
        self.tipus2 = 1
        ax_xy = fig.add_subplot(331)
        ax_xy.set_title('X/Y')
        ax_xz = fig.add_subplot(333)
        ax_xz.set_title('X/Z')
        ax_zy = fig.add_subplot(334)
        ax_zy.set_title('Z/Y')
        ax.set_facecolor([0.98,0.92,0.84])  # blanc antic
        zx, zy, zz = [], [], []

        idchains = Atributs.residut("idChain")
        idresidus = Atributs.residut("idResidu")
        idresatom = Atributs.atomt("idResidu")
        aprot = Atributs.atomt("idTAtom")

        idx = Atributs.atomt("xcoor")
        idy = Atributs.atomt("ycoor")
        idz = Atributs.atomt("zcoor")

        vella_mol = ""
        for chain_id in self.molecules:
            if chain_id != vella_mol:
                atr = Colors(chain_id)
                nom = atr.color_molecula()
                vella_mol = chain_id
            xs = []
            ys = []
            zs = []
            wresidus = [res for res in self.residus if res[idchains] == chain_id]
            for residu in wresidus:
                watoms = []
                watoms = [atom for atom in self.atoms if atom[idresatom] == residu[idresidus] and
                          atom[idchains] == chain_id and atom[aprot] == True]
                for atom in watoms:
                    x = atom[idx]
                    y = atom[idy]
                    z = atom[idz]
                    xs.append(x)
                    ys.append(y)
                    zs.append(z)
                    atr = Colors(chain_id,1)
                    nom = atr.color_molecula()
            ax.scatter(xs, ys, zs, marker='*', color=nom, alpha=0.35)
            ax_xy.scatter(xs, ys, marker='.', color=nom,  alpha=0.15)
            ax_xz.scatter(xs, zs, marker='.', color=nom, alpha=0.15)
            ax_zy.scatter(zs, ys, marker='.', color=nom, alpha=0.15)
            # ax.text2D(0.05, 0.95, self.capcalera, transform=ax.transAxes)
            # ax.text(9, 0, 0,self.capcalera , color='red')
        plt.show()
