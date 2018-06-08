#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codi.atributs.atributs import Atributs
from codi.atributs.pat import pat

class Entitat(object):

    def __init__(self, fitxer):
        self.models = []
        self.fitxer = fitxer
        self.pat = pat('db')
        self.dades = self.pat + self.fitxer
        self.nomtaula = fitxer
        self.atoms = []
        self.molecules = []
        self.residus = []


        f = open(self.dades)
        self.linies = f.readlines()
        f.close()

    def get_linies(self):
            return self.linies

    @staticmethod
    def get_models(lin):
        '''
            El registre MODEL especifica el numero de serie del model quan hi ha diversos models de la mateixa estructura
            es presenten en una unica entrada de coordenades, com sovint passa amb les estructures que determina la RMN.
            Format de registre
            1 - 6   Nom del registre "MODEL"
            11 - 14 Numero de serie del model en serie Integer.
        '''
        return (int(lin[11:14]))

    @staticmethod
    def flinia_atoms(linia):
        return (
            Entitat.cad(linia[0:6]),  # 0   Tipu
            int(linia[6:11]),           # 1   Numero de serie de l atom
            Entitat.cad(linia[12:16]),  # 2   Nom d'atom
            Entitat.cad(linia[16:17]),  # 3   Indicador d'ubicacio alternatiu
            Entitat.cad(linia[17:20]),  # 4   Nom de residu
            Entitat.cad(linia[21:22]),  # 5   Identificador de la cadena
            Entitat.cad(linia[22:26]),  # 6   Numero de sequencia de residus
            Entitat.cad(linia[26:27]),  # 7   Codi d'insercio de residus
            float(linia[30:38]),  # 8   Coordenades ortogonals per a x en Angstrongs
            float(linia[38:46]),  # 9   Coordenades ortogonals per a y en Angstrongs
            float(linia[46:54]),  # 10  Coordenades ortogonals per a z en Angstrongs
            float(linia[54:60]),  # 11  Ocupacio
            float(linia[60:66]),  # 12  Factor de temperatura
            Entitat.cad(linia[76:78]),  # 13  Simbol d'element, justificat per la dreta
            Entitat.cad(linia[78:80])  # 14  Carrega de l'atom
            
        )


    @staticmethod
    def cad(param):
        cadparam = str(param)
        a = param.strip(' \t\n\r')
        return (a)

    def crear_entitat(self):

        self.models.append(1)
        widModel = 1
        idModel = 1
        wnmodels = 1
        widChain = ""
        wwidChain = ""
        widnumSeqres = 0
        idTAtom = True
        widTResidu = True
        idCA = False
        wnAtoms = 0
        primer = True
        xCA = 0.0
        yCA = 0.0
        zCA = 0.0
        totalAtoms = 0
        wclau = ""

        # posicions dels camps necessaris en el registre d'atoms del pdb

        ntipus = Atributs.campsAtoms("tipus")
        nnumser = Atributs.campsAtoms("numser")
        nsigatom = Atributs.campsAtoms("sigatom")
        nnomResidu = Atributs.campsAtoms("nomResidu")
        nidChain = Atributs.campsAtoms("idChain")
        nidnumSeqres = Atributs.campsAtoms("numSeqres")
        nxcoor = Atributs.campsAtoms("xcoor")
        nycoor = Atributs.campsAtoms("ycoor")
        nzcoor = Atributs.campsAtoms("zcoor")
        nelemQuim = Atributs.campsAtoms("elemQuim")

        # Càlcul del centre de la proteian i diferencia respecte a les coordenades (0,0.0)

        self.dx, self.dy, self.dz = Entitat.cercar_centre_proteina(self)
        primer = True
        '''  Models '''
        sx = 0
        sy = 0
        sz = 0
        num = 0
        idCA = False
        for lin in self.linies:
            tipus = lin[0:6]
            if tipus == "MODEL ":
                idModel = Atributs.get_models(lin)
                if idModel > 1:
                    self.models.append(idModel)
                    nmodels += 1
            ''' Ordre dels camps en el registre de atom'''
            if tipus == "ATOM  " or tipus == "HETATM":
                linia = Entitat.flinia_atoms(lin)
                nomResidu = linia[nnomResidu]
                if nomResidu != "HOH":
                    clau = ""
                    tipus = linia[ntipus]
                    sigatom = linia[nsigatom]
                    idChain = linia[nidChain]
                    idAtom = linia[nnumser]
                    idnumSeqres = linia[nidnumSeqres]
                    xcoor = round(linia[nxcoor] + self.dx, 4)  # Coordenada transformada,
                    ycoor = round(linia[nycoor] + self.dy, 4)  # Coordenada transformada
                    zcoor = round(linia[nzcoor] + self.dz, 4)  # Coordenada transformada
                    sx = sx + xcoor
                    sy = sy + ycoor
                    sz = sz + zcoor
                    num += 1
                    elemQuim = linia[nelemQuim]

                    ''' Clau de comparacio'''
                    clau = str(idModel) + idChain + str(idnumSeqres).rjust(4, "0")

                    '''  Proteina o Estranys '''
                    if tipus == "ATOM":
                        idTAtom = True
                    else:
                        idTAtom = False
                    idTResidu = idTAtom

                    ''' Molecules '''
                    if idChain != wwidChain:
                        wwidChain = idChain
                        if idChain in self.molecules:
                            pass
                        else:
                            self.molecules.append(idChain)

                    ''' carbono alfa'''
                    if sigatom == "CA":
                        idCA = True
                        xCA = xcoor
                        yCA = ycoor
                        zCA = zcoor

                    if primer:

                        widModel = idModel
                        widChain = idChain
                        widAtom = idAtom
                        widnumSeqres = idnumSeqres
                        wnomResidu = nomResidu
                        widTResidu = idTResidu
                        wclau = clau
                        primer = False
                        self.atoms.append([idModel, idChain, idnumSeqres, idAtom, sigatom, nomResidu, xcoor, ycoor,
                                           zcoor, elemQuim, idCA, idTAtom])
                        wnAtoms = 1
                        totalAtoms = 1

                    elif clau != wclau:
                        self.atoms.append([idModel, idChain, idnumSeqres, idAtom, sigatom, nomResidu, xcoor, ycoor,
                                           zcoor, elemQuim, idCA, idTAtom])
                        if idCA == False:
                            xCA = round(sx/num,4)
                            yCA = round(sy/num,4)
                            zCA = round(sz/num,4)
                        self.residus.append([widModel, widChain, widnumSeqres, wnomResidu, xCA, yCA, zCA, wnAtoms,
                                             widTResidu])
                        sx = 0
                        sy = 0
                        sz = 0
                        num = 0
                        xCA = 0.0
                        yCA = 0.0
                        zCA = 0.0
                        idCA= False
                        wnAtoms = 1
                        totalAtoms += 1
                        widModel = idModel
                        widChain = idChain
                        widnumSeqres = idnumSeqres
                        wnomResidu = nomResidu
                        widTResidu = idTResidu
                        wclau = clau
                    elif clau == wclau:
                        self.atoms.append([idModel, idChain, idnumSeqres, idAtom, sigatom, nomResidu, xcoor, ycoor,
                                           zcoor, elemQuim, idCA, idTAtom])
                        wnAtoms += 1
                        totalAtoms += 1
                else:
                    continue
            # ultim registre
            if idCA ==  False:
                if num> 0:
                    xCA = round(sx / num, 4)
                    yCA = round(sy / num, 4)
                    zCA = round(sz / num, 4)
                    xCA = sx + self.dx
                    yCA = sy + self.dy
                    zCA = sz + self.dz
        self.residus.append([widModel, widChain, widnumSeqres, wnomResidu, xCA, yCA, zCA, wnAtoms, widTResidu])
        caps = [linia for linia in self.linies if linia[0:6] == "TITLE "]
        text = ""
        for cap in caps:
            nom = str(cap[10:80].strip(' \t\n\r'))
            text = text + nom
            self.capcalera = text
        return self.capcalera, self.models, self.molecules, self.residus, self.atoms, self.nomtaula

   # Cercar distància des del centre de la proteina al centre de coordenades
    def cercar_centre_proteina(self):
        sx = 0
        sy = 0
        sz = 0
        atms = 0
        for linia in self.linies:
            if linia[0:4] == "ATOM":
                atom = Entitat.flinia_atoms(linia)
                x = atom[Atributs.campsAtoms("xcoor")]
                y = atom[Atributs.campsAtoms("ycoor")]
                z = atom[Atributs.campsAtoms("zcoor")]
                sx += x
                sy += y
                sz += z
                atms += 1
        dx = 0 - round(sx / atms, 4)
        dy = 0 - round(sy / atms, 4)
        dz = 0 - round(sz / atms, 4)

        return (dx, dy, dz)




def maxmins(atoms):
    xmax = -999999999
    xmin = 999999999
    ymax = -999999999
    ymin = 999999999
    zmax = -99999999
    zmin = 999999999
    xs = 0
    ys = 0
    zs = 0
    num = 0
    nx = Atributs.atomt("xcoor")
    ny = Atributs.atomt("ycoor")
    nz = Atributs.atomt("zcoor")
    for i in range(len(atoms) - 1):
        linia = atoms[i]
        x = linia[nx]
        y = linia[ny]
        z = linia[nz]
        if x > xmax: xmax = x
        if x <= xmin: xmin = x
        if y > ymax: ymax = y
        if y <= ymin: ymin = y
        if z > zmax: zmax = z
        if z <= zmin: zmin = z
        num += 1
        xs = xs + x
        ys = ys + y
        zs = zs + z
        llista = [xmin, ymin, zmin], [xmax, ymax, zmax], [(round(xs / num, 4)), round(ys / num, 4),
                                                          round(zs / num, 4)]
    return (llista)





