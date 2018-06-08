#!/usr/bin/env python
# -*- coding: utf-8 -*-
from codi.atributs.atributs import *

class Colors(object):

    def __init__(self, parametre=None, parametre2=None):
        self.parametre = parametre
        self.parametre2 = parametre2

        self.taula_colors = [[1, "Negre", "u'Negre'", u'#000000', [0.00, 0.00, 0.00,1]],
                             [2, "Verd fosc", "u'Verd fosc'", u'#006400', [0.00, 0.39, 0.00,1]],
                             [3, "Gris", "u'Gris'", u'#808080', [0.50, 0.50, 0.50,1]],
                             [4, "Vermell fosc", "u'Vermell fosc'", u'#8B0000', [0.55, 0.00, 0.00,1]],
                             [5, "Marró", "u'Marró'", u'#A52A2A', [0.65, 0.16, 0.16,1]],
                             [6, "Roig indi", "u'Roig indi'", u'#CD5C5C', [0.80, 0.36, 0.36,1]],
                             [7, "Carmesí", "u'Carmesí'", u'#DC143C', [0.86, 0.08, 0.24,1]],
                             [8, "Caqui fosc", "u'Caqui fosc'", u'#BDB76B', [0.74, 0.72, 0.42,1]],
                             [9, "Taronja fosc", "u'Taronja fosc'", u'#FF8C00', [1.00, 0.55, 0.00,1]],
                             [10, "Verd llima", "u'Verd llima'", u'#32CD32', [0.20, 0.80, 0.20,1]],
                             [11, "Groc verd", "u'Groc verd'", u'#9ACD32', [0.60, 0.80, 0.20,1]],
                             [12, "Or", "u'Or'", u'#FFD700', [1.00, 0.84, 0.00,1]],
                             [13, "Groc", "u'Groc'", u'#FFFF00', [1.00, 1.00, 0.00,1]],
                             [14, "Mig violeta vermell", "u'Mig violeta vermell'", u'#C71585', [0.78, 0.08, 0.52,1]],
                             [15, "Rosa profund", "u'Rosa profunda'", u'#FF1493', [1.00, 0.08, 0.58,1]],
                             [16, "Cian fosc", "u'Cian fosc'", u'#008B8B', [0.00, 0.55, 0.55,1]],
                             [17, "Llum verd mari", "u'Llum verd marí'", u'#20B2AA', [0.13, 0.70, 0.67,1]],
                             [18, "Mar verd fosc", "u'Mar verd fosc'", u'#8FBC8F', [0.56, 0.74, 0.56, 1]],
                             [19, "Marron Rosy ", "u'Marron Rosy '", u'#BC8F8F', [0.74, 0.56, 0.56,1]],
                             [20, "Plata", "u'Plata'", u'#C0C0C0', [0.75, 0.75, 0.75,1]],
                             [21, "Verd pàl·lid", "u'Verd pàl·lid'", u'#98FB98', [0.60, 0.98, 0.60,1]],
                             [22, "Blau", "u'Blau'", u'#0000FF', [0.00, 0.00, 1.00,1]],
                             [23, "Blau reial", "u'Blau reial'", u'#4169E1', [0.25, 0.41, 0.88,1]],
                             [24, "Violeta mitjà", "u'Violeta mitjà'", u'#9370DB', [0.58, 0.44, 0.86,1]],
                             [25, "Orquídia fosca", "u'Orquídia fosca'", u'#9932CC', [0.60, 0.20, 0.80, 1]],
                             [26, "Fucsia", "u'Fucsia'", u'#FF00FF', [1.00, 0.00, 1.00, 1]],
                             [27, "Blau profund marí", "u'Blau profund marí'", u'#00BFFF', [0.00, 0.75, 1.00, 1]],
                             [28, "Blau Dodger", "u'Blau Dodger'", u'#1E90FF', [0.12, 0.56, 1.00, 1]],
                             [29, "Prunera", "u'Prunera'", u'#DDA0DD', [0.87, 0.63, 0.87, 1]],
                             [30, "Rosa clar", "u'Rosa clar'", u'#FFB6C1', [1.00, 0.71, 0.76, 1]],
                             [31, "Pale Turquesa", "u'Pale Turquesa'", u'#AFEEEE', [0.69, 0.93, 0.93, 1]],
                             [32, "Lavanda", "u'Lavanda'", u'#E6E6FA', [0.90, 0.90, 0.98, 1]],
                             [33, "Blanc antic", "u'Blanc antic'", u'#FAEBD7', [0.98, 0.92, 0.84,1]],
                             [34, "Neu", "u'Neu'", u'#FFFAFA', [1.00, 0.98, 0.98, 1]]]

        self.molecules = {'A': 23, 'B': 17, 'C': 12, 'D': 18, 'E': 19, 'F': 8, 'G': 20, 'H': 2, 'I': 30, "J": 2, 'K': 29,
                          "L": 16, "M": 27, "N":23, "O":17, "P":12, "Q":18,"R":19, "S": 8, "T": 20, "U":2, "V": 30,
                            "W":29, "X":16,"Y":27,"Z":23}
        self.molecules2 = {'A': 'red', 'B': 'green', 'C': 'blue', 'D': 'darkorchid', 'E': 'darkviolet',
                           'F': 'chocolate', 'G': 'darksalmon', 'H': 'yellowgreen', 'I':  'deepskyblue'}

        self.tipus_aminoacid = {'ALA': 1, 'ARG': 4, 'ASN': 2, 'ASP': 3, 'CYS': 2, 'PHE': 2, 'GLN': 3, 'GLU': 2,
                                'GLY': 4, 'HIS': 1, 'ILE': 2, 'LEU': 4, 'LYS': 1, 'PRO': 1, 'MET': 1, 'SER': 2,
                                'THR': 2, 'TYR': 1, 'TRP': 2, 'VAL': 1}

        self.tipologia_amin = {1: "Hidrofobics", 2: "Hidrofilics", 3: "Acids", 4: "Basics", 5: "Altres"}

        self.tipologia_lcolor = {1: "r", 2: "g", 3: "b", 4: "y", 5: "k"}

        self.tipologia_color = {1: 2, 2: 12, 3: 24, 4: 30, 5: 26}

        self.color_aminoacids = {'ALA': 1, 'ARG': 2, 'ASN': 3, 'ASP': 4, 'CYS': 5, 'PHE': 6, 'GLN': 7, 'GLU': 8,
                                 'GLY': 9, 'HIS': 10, 'ILE': 11, 'LEU': 12, 'LYS': 13, 'PRO': 14, 'MET': 15, 'SER': 16,
                                 'THR': 17, 'TYR': 18, 'TRP': 19, 'VAL': 20, "C": 21, "G": 22, "A": 23, "U": 24,
                                 "I": 25, "DC": 27, "DG": 28, "DA": 29, "DU": 30, "DT": 31, "DI+": 32, "NNN": 33}





    # @staticmethod
    def color_molecula(self):
        cl=()
        if self.parametre2 == 1:
            num = self.molecules[self.parametre]
            num = num - 1
            linia = self.taula_colors[num]
            cl = linia[4]
        if self.parametre2 == 2:
            cl = self.molecules2[self.parametre]
        return cl

    def color_tipus(self):
        try :
            num = self.tipus_aminoacid[self.parametre]
        except:
            num = 5
        if self.parametre2 == 1:
            num2 = self.tipologia_color[num]
            num2 = num2 - 1
            cl = self.taula_colors[num2][4]
        else:
            cl = self.tipologia_lcolor[num]
        color = cl
        return color

    def color_aminoacid(self):
        try:
            num = self.color_aminoacids[self.parametre]
            num = num - 1
            linia = self.taula_colors[num]
            color = linia[4]
        except:
            color = (1.00, 0.98, 0.98, 1)
        return color

    # def nom_amino(self):
    #     nom = "Desconegut"
    #     self.amn = Atributs.mestre_aminoacids
    #     for i in range(len(self.amn)):
    #         if self.mestre_aminoacids[i][2] == self.parametre:
    #             nom = self.mestre_aminoacids[i][1]
    #     return (nom)


class Atributs(object):

    def __init__(self, parametre=None, parametre2=None):

        if parametre !=None:
            self.parametre = parametre
        else:
            self.patramtre = None

        if parametre !=None:
            self.parametre2 = parametre2
        else:
            self.patramtre2 = None

        self.atom_radis = {"Al": 1.82, "As": 1.33, "S": 1.09, "Br": 1.12, "Ca": 2.23, "C": 0.91, "Cl": 0.97, "Co": 1.67,
                       "Cu": 1.57, "Sr": 2.45, "F": 0.57, "P": 1.23, "H": 0.79, "Fe": 1.72, "I": 1.32, "Li": 2.05,
                       "Mg": 1.72, "Mn": 1.79, "Mo": 2.01, "N": 0.75, "O": 0.65, "Pb": 1.81, "K": 2.77, "Se": 1.22,
                       "Si": 1.46, "Na": 2.23, "V": 1.92, "Zn": 1.53}

        self.mestre_aminoacids =   [["ALA", "Alanina", "A", 67, "H", 1, 1.40],
                                    ["ARG", "Arginina", "R", 148, "C+", 4, 3.08],
                                    ["ASN", "Asparagina", "N", 96, "P", 2, 2.00],
                                    ["ASP", "Aspartato", "D", 91, "C-", 3, 1.90],
                                    ["CYS", "Cisteína", " C", 86, "P", 2, 1.79],
                                    ["GLU", "Glutamato", "E", 109, "C-", 4, 2.27],
                                    ["GLN", "Glutamina", "Q", 114, "P", 1, 2.38],
                                    ["GLY", "Glicina", "G", 48, "N", 2, 1.00],
                                    ["HIS", "Histidina", "H", 118, "P, C+", 2, 2.46],
                                    ["ILE", "Isoleucina", "I", 124, "H", 4, 2.58],
                                    ["LEU", "Leucina", "L", 124, "H", 1, 2.58],
                                    ["LYS", "Lisina", "K", 135, "C+", 1, 2.81],
                                    ["MET", "Metionina", "M", 124, "H", 2, 2.58],
                                    ["PHE", "Fenilalanina", "F", 135, "H", 3, 2.81],
                                    ["PRO", "Prolina", "P", 90, "H", 1, 1.88],
                                    ["SER", "Serina", "S", 73, "P", 2, 1.52],
                                    ["THR", "Treonina", "T", 93, "P", 2, 1.94],
                                    ["TRP", "Triptófano", " W  " , 163, "P", 1, 3.40],
                                    ["TYR", "Tirosina", "Y", 141, "P", 2, 2.94],
                                    ["VAL", "Valina", "V", 105, "H", 1, 2.19]]
    @staticmethod
    def campsAtoms(parametre):
        d = {"tipus": 0, "numser": 1, "sigatom": 2, "altloc": 3, "nomResidu": 4, "idChain": 5, "numSeqres": 6,
             "codiInsercio": 7, "xcoor": 8, "ycoor": 9, "zcoor": 10, "ocupacio": 11, "factorTemp": 12,
             "elemQuim": 13, "carrega": 14, "model": 15}
        return (d[parametre])

    @staticmethod
    def atomt(parametre):
        atomt = {"idModel": 0, "idChain": 1, "idResidu": 2, "idAtom": 3, "sigAtom": 4, "nomResidu": 5, "xcoor": 6,
                 "ycoor": 7, "zcoor": 8, "elemQuim": 9, "ca": 10, "idTAtom": 11}
        posicio = atomt[parametre]  # posicio dins el registres
        return posicio

    @staticmethod
    def residut(parametre):
        residut = {"idModel": 0, "idChain": 1, "idResidu": 2, "nomResidu": 3, "xcoor": 4, "ycoor": 5, "zcoor": 6,
                   "nAtoms": 7, "idTResidu": 8}
        posicio = residut[parametre]  # posicio dins el registres
        return posicio

    def radi(self):
        try:
            radi = self.atom_radis[self.parametre]
            return radi
        except:
            return 1.5

    def nom_aminoacid(self):
        aminos = self.mestre_aminoacids
        trobat= False
        for i in range(len(self.mestre_aminoacids)):
            if self.mestre_aminoacids[i][0] == self.parametre:
                nom = self.mestre_aminoacids[i][1]
                trobat = True
            if trobat:
                break
        return [nom]


    def llista_aminoacids(self):
        nom = []
        lletra = []
        sigles = []
        volum = []
        tipus1 = []
        tipus2 = []
        escala = []

        for i in range(len(self.mestre_aminoacids)):
            nom.append(self.mestre_aminoacids[i][1])
            lletra.append(self.mestre_aminoacids[i][0])
            sigles.append(self.mestre_aminoacids[i][2])
            volum.append(self.mestre_aminoacids[i][3])
            tipus1.append(self.mestre_aminoacids[i][4])
            tipus2.append(self.mestre_aminoacids[i][5])
            escala.append(self.mestre_aminoacids[i][6])
        return nom, lletra, sigles, volum, tipus1, tipus2, escala