#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codi.atributs.atributs import Atributs
from codi.atributs.estructura import Entitat


class Dades(object):

    def __init__(self, fitxer):
        self.fitxer = fitxer
        E = Entitat(self.fitxer)
        self.linies = E.get_linies()
        dadestotals = E.crear_entitat()
        self.capcalera = dadestotals[0]
        self.molecules = dadestotals[2]
        self.residus = dadestotals[3]
        self.atoms = dadestotals[4]
        self.nom_taula = dadestotals[5]

        self.nomResidu = Atributs.residut("nomResidu")
        self.nomElement = Atributs.atomt("elemQuim")
        self.idTResidu = Atributs.residut("idTResidu")
        self.idTAtom = Atributs.atomt("idTAtom")

    ############################################################################

    def entrades(self):
        return self.capcalera, self.molecules, self.nom_taula

    def get_header(self):
        caps = [linia for linia in self.linies if linia[0:6] == "HEADER"]
        text= caps[0][7:]
        text.strip(' \t\n\r')
        return str(text)

    def get_helix(self):
        caps = [linia for linia in self.linies if linia[0:6] == "HELIX "]
        text= "Hi ha %d subestructures helix alfa " % (len(caps))
        return text

    def get_sheet(self):
        caps = [linia for linia in self.linies if linia[0:6] == "SHEET "]
        full=""
        num1=0
        num2=0
        for cap in caps:
            num1+=1
            a=cap[11:14].strip(' \t\n\r')
            if a != full:
                num2+=1
                full=a
        text= "Hi ha %d lamines beta i %d subestructures de lamina" % (num2,num1)
        return text



    def get_title(self):
        noms = []
        caps = [linia for linia in self.linies if linia[0:6] == "TITLE "]
        text = ""
        for cap in caps:
            nom = str(cap[10:80].strip(' \t\n\r'))
            text = text + nom
        self.titol = text
        return str(text)

    def get_models_dades(self):
        noms = []
        caps = [linia for linia in self.linies if linia[0:6] == "MODEL "]
        n = 0
        for cap in caps:
            noms += 1
        if n == 0:
            noms = 1
        return noms

    def get_keywds(self):
        caps = [linia for linia in self.linies if linia[0:6] == "KEYWDS"]
        linia=""
        for cap in caps :
            a= cap[7:].strip(' \t\n\r')
            linia= linia + " " + a
        return linia

    def get_compnd(self):
        noms = []
        caps = [linia for linia in self.linies if linia[0:6] == "COMPND"]
        for i in range(len(caps)):
            text = caps[i][10:80]
            noms.append(text)
        return noms

    #####################################################################################

    def get_heterogenis(self):
        hets = []
        cadenes = []
        natoms = []
        hetnams = []
        hetsyn = []
        formuls = []
        linies = [linia for linia in self.linies if linia[0:6] == "HET   "]
        for linia in linies:
            hets.append(linia[7:10])
            cadenes.append(linia[11:14])
            natoms.append(linia[20:25])
            num = len(hets)
        for i in range(num):
            hetnams.append(" ")
            hetsyn.append(" ")
            formuls.append(" ")

        linies = [linia for linia in self.linies if linia[0:6] == "HETNAM" or linia[0:6] == "HETSYN"
                  or linia[0:6] == "FORMUL"]
        for linia in linies:
            tipus = linia[0:6]
            if tipus == "HETNAM":
                het = linia[11:14]
                valor = linia[15:70].strip(' \t\n\r')
                if het in hets:
                    idx = hets.index(het)
                    hetnams[idx] = hetnams[idx] + valor

            if tipus == "HETSYM":
                het = linia[11:14]
                valor = linia[15:70].strip(' \t\n\r')
                if het in hets:
                    idx = hets.index(het)
                    hetsyn[idx] = hetsyn[idx] + valor

            if tipus == "FORMUL":
                het = linia[12:15]
            if het != "HOH":
                valor = linia[19:70].strip(' \t\n\r')
                if het in hets:
                    idx = hets.index(het)
                    formuls[idx] = valor
        return hets, cadenes, natoms, hetnams, hetsyn, formuls

    def get_natoms(self):
        return len(self.atoms)

    def get_nresidus(self):
        return len(self.residus)

    def get_elements(self):
        self.latoms = []
        self.latomsn = []
        self.lhets = []
        self.lhetsn = []

        for atom in self.atoms:
            prot = atom[self.idTAtom]
            elem = atom[self.nomElement]
            if prot:
                if elem in self.latoms:
                    idx = self.latoms.index(elem)
                    self.latomsn[idx] = int(self.latomsn[idx]) + 1
                else:
                    self.latoms.append(elem)
                    self.latomsn.append(1)
            else:
                if elem in self.lhets:
                    idx = self.lhets.index(elem)
                    self.lhetsn[idx] = int(self.lhetsn[idx]) + 1
                else:
                    self.lhets.append(elem)
                    self.lhetsn.append(1)
        return self.latoms, self.latomsn, self.lhets, self.lhetsn

    def get_residus(self):
        a = Atributs(self,)
        self.lresidus = []
        self.lresidusn = []
        self.lresiduts = []
        self.lresidutsn = []
        self.lreshets = []
        self.lreshetsn = []
        self.sig = []
        self.nom_amino = []
#       self.nom, self.lletra, self.sig, self.tipologia = a.llista_aminoacids()
        self.mestre_aminoacids = a.mestre_aminoacids
        n=len(self.mestre_aminoacids)
        for i in range(len(self.mestre_aminoacids)):
            self.sig.append(self.mestre_aminoacids[i][0])
            self.nom_amino.append(self.mestre_aminoacids[i][2])
        for residu in self.residus:
            res = residu[self.nomResidu]
            prot = residu[self.idTResidu]
            if prot:
                if res in self.sig:
                    if res in self.lresidus:
                        idx = self.lresidus.index(res)
                        self.lresidusn[idx] = int(self.lresidusn[idx]) + 1
                    else:
                        self.lresidus.append(res)
                        self.lresidusn.append(1)
                else:
                    if res in self.lresiduts:
                        idx = self.lresiduts.index(res)
                        self.lresidutsn[idx] = int(self.lresidutsn[idx]) + 1
                    else:
                        self.lresiduts.append(res)
                        self.lresidutsn.append(1)
            else:
                if res in self.lreshets:
                    idx = self.lreshets.index(res)
                    self.lreshetsn[idx] = int(self.lreshetsn[idx]) + 1
                else:
                    self.lreshets.append(res)
                    self.lreshetsn.append(1)

        return self.lresidus, self.lresidusn, self.lresiduts, self.lresidutsn, self.lreshets, self.lreshetsn
