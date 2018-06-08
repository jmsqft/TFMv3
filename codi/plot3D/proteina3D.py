#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from direct.gui.OnscreenText import OnscreenText, TextNode
from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import *

from codi.atributs.atributs import Atributs
from codi.atributs.atributs import Colors
from codi.atributs.estructura import Entitat
from codi.atributs.pat import pat


# Posar el títol
def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(0.8, 0.64, 0.4, 1), scale=.045,
                        parent=base.a2dBottomRight, align=TextNode.ARight,
                        pos=(-0.04, 0.04), shadow=(1, 1, 1, 1))


# Posar instruccions
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1, 1, 1, 1), scale=.045,
                        shadow=(0, 0, 0, 1), parent=base.a2dTopLeft,
                        pos=(0.08, -pos - 0.04), align=TextNode.ALeft)


class Proteines(ShowBase):
    pas_mov = 15
    pas_rot = 20

    def __init__(self, tipus, fitxer, amino=None):

        ShowBase.__init__(self)

        base.setBackgroundColor(0.2, 0.2, 0.2, 1.0)
        ample = 1000
        alt = 800

        loadPrcFileData("", "window-title Visor 3D")
        loadPrcFileData("", "win-size %s %s" % (ample, alt))
        self.fitxer = fitxer
        self.pat = pat("db")
        self.dades = self.pat + self.fitxer
        self.esfera = pat("model") + "atom_sphere.egg"
        self.dirlight = pat("model") + "Dirlight.egg"
        e = Entitat(self.fitxer)
        dadestotals = e.crear_entitat()
        self.capcalera = dadestotals[0]
        self.molecules = dadestotals[2]
        self.nmol = len(self.molecules)
        self.residus = dadestotals[3]
        self.atoms = dadestotals[4]
        self.nom_taula = dadestotals[5]
        if self.capcalera == "":
            self.capcalera = "Fitxer: %s, sense descripció" % (fitxer)
        self.win.setClearColor((0, 0, 0, 1))
        self.tipus = tipus
        if self.tipus == 4:
            self.amino = amino
        else:
            self.amino = ""
        self.accept('c', self.centrar_camera)
        self.accept('escape', sys.exit)
        self.xc = Atributs.atomt("xcoor")
        self.yc = Atributs.atomt("ycoor")
        self.zc = Atributs.atomt("zcoor")
        self.id = Atributs.atomt("sigAtom")
        self.elem = Atributs.atomt("elemQuim")
        self.c = Atributs.atomt("idChain")
        self.prot = Atributs.atomt("idTAtom")
        self.nomRes = Atributs.atomt("nomResidu")
        self.sig = Atributs.atomt("sigAtom")

        #######################################################################

        text = TextNode('node name')
        textNodePath = aspect2d.attachNewNode(text)
        text.setTextColor(0.8, 0.64, 0.4, 1)
        textNodePath.setPos(-0.15, 0, 0.9)
        textNodePath.setScale(0.05)
        align = TextNode.ALeft
        if tipus == 1:
            text.setText("Representació complex proteic seguns color aminoàcids")
        if tipus == 5:
            text.setText("Representació complex per molècules")
        if tipus == 7:
            text.setText("Representació per tipus aminoàcid")
        if tipus == 2:
            text.setText("Representació elements externs a la proteïna")
        if tipus == 4:
            text.setText("Representació ubicació d'un aminoaàcid concret dins la proteïna")
        if tipus == 3:
            text.setText("Representació dels carbonis alfa per tipus aminoàcids")
        if tipus == 6:
            text.setText("Representació en backbone")
        text.setShadow(0.02, 0.02)
        text.setShadowColor(1, 1, 1, 1)

        ########################################################################

        # Instruccions

        self.title = addTitle(self.capcalera)
        self.inst01 = addInstructions(0.06, "[ESC]: Sortir")
        self.inst02 = addInstructions(0.12, "[z]: Zoom in ")
        self.inst03 = addInstructions(0.18, "[x]: Zoom out ")
        self.inst04 = addInstructions(0.24, "[fletxa dreta: Girar cap a la dreta")
        self.inst05 = addInstructions(0.30, "[fletxa esquerra: Girar cap a l'esquerra")
        self.inst06 = addInstructions(0.36, "[fletxa amunt]: Girar cap endavant")
        self.inst07 = addInstructions(0.42, "[fletxar avall]: Girar cap avall")
        self.inst08 = addInstructions(0.48, "[e]: Girar cap amunt eix y")
        self.inst09 = addInstructions(0.54, "[r]: Girar cap avall eix y")
        if self.tipus == 3 or self.tipus == 7:
            self.inst10 = addInstructions(1.40, "Llegenda")
            self.inst11 = addInstructions(1.46, "Verd forsc - Hidrofòbics")
            self.inst12 = addInstructions(1.52, "Or - Hidrofilics")
            self.inst13 = addInstructions(1.58, "Violeta - Àcids")
            self.inst14 = addInstructions(1.64, "Rosa clar - Bàsics")
        if self.tipus == 1:
            pass

        self.keyMap = {"z": 0, "x": 0, "q": 0, "w": 0, "c": 0, "dreta": 0, "esquerra": 0, "endavant": 0, "enrrera": 0,
                       "e": 0, "r": 0}

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

        self.proteina = render.attachNewNode("Proteina")
        if self.tipus == 1:
            self.atomic(self.atoms, self.tipus, self.amino, self.proteina)
        if self.tipus == 2:
            self.atomic(self.atoms, self.tipus, self.amino, self.proteina)
        if self.tipus == 3:
            self.ball_stick(self.atoms, self.tipus, self.molecules, self.proteina)
        if self.tipus == 4:
            self.atomic(self.atoms, self.tipus, self.amino, self.proteina)
        if self.tipus == 5:
            self.atomic(self.atoms, self.tipus, self.amino, self.proteina)
        if self.tipus == 6:
            self.backbone(self.atoms, self.tipus, self.amino, self.proteina)
        if self.tipus == 7:
            self.atomic(self.atoms, self.tipus, self.amino, self.proteina)
        self.proteina.reparentTo(render)

        # Centrar proteina
        self.centrar_proteina()

        # Fons
        base.setBackgroundColor(0.2, 0.2, 0.2, 1.0)

        # Centrar camera

        self.centrar_camera()
        self.center = loader.loadModel(self.esfera)
        self.center.setColor(0.0, 0.4, 0.0, 1.0)
        self.centrar_camera()

        # llum ambiental

        self.ll_ambient = AmbientLight('ll_ambient')
        self.ll_ambient.setColor(LVecBase4f(0.60, 0.60, 0.6, 1))
        self.amb_np = render.attachNewNode(self.ll_ambient)
        render.setLight(self.amb_np)

        # llum direccional número 1

        self.dllum = DirectionalLight('dllum')
        self.dllum.setColor(VBase4(0.8, 0.8, 0.8, 0.75))
        self.dlnp = render.attachNewNode(self.dllum)
        self.dlnp.setHpr(0, -45, 0)
        self.dlnp.setPos(10, -100, 0)
        render.setLight(self.dlnp)

        # llum direccional número 2

        self.dllum2 = DirectionalLight('dllum')
        self.dllum2.setColor(VBase4(0.8, 0.8, 0.8, 0.75))
        self.dlnp2 = render.attachNewNode(self.dllum)
        self.dlnp2.setHpr(0, 45, 0)
        self.dlnp2.setPos(-100, -100, 30)
        render.setLight(self.dlnp2)

        # Llum spotlight

        self.slight = Spotlight('slight')
        self.slight.setColor(VBase4(0.8, 0.8, 0.8, 1))
        self.lens = PerspectiveLens()
        self.slight.setLens(self.lens)
        self.slnp = render.attachNewNode(self.slight)
        self.slnp.setPos(-50, -50, 30)
        self.slnp.lookAt(0, 0, 0)
        render.setLight(self.slnp)

        render.setAntialias(AntialiasAttrib.MAuto)

        # Tecles acció

        self.tecles_accio()

    def tecles_accio(self):

        self.accept("escape", sys.exit)
        self.accept('z', self.setKey, ["z", True])
        self.accept('z-up', self.setKey, ["z", False])
        self.accept('x', self.setKey, ["x", True])
        self.accept('x-up', self.setKey, ["x", False])
        self.accept('arrow_left', self.setKey, ["esquerra", True])
        self.accept('arrow_left-up', self.setKey, ["esquerra", False])
        self.accept('arrow_right', self.setKey, ["dreta", True])
        self.accept('arrow_right-up', self.setKey, ["dreta", False])
        self.accept('arrow_up', self.setKey, ["endavant", True])
        self.accept('arrow_up-up', self.setKey, ["endavant", False])
        self.accept('arrow_down', self.setKey, ["enrrera", True])
        self.accept('arrow_down-up', self.setKey, ["enrrera", False])
        self.accept('c', self.setKey, ["centrar", True])
        self.accept('e', self.setKey, ["e", True])
        self.accept('e-up', self.setKey, ["e", False])
        self.accept('r', self.setKey, ["r", True])
        self.accept('r-up', self.setKey, ["r", False])

        # Funcions moviments

        taskMgr.add(self.moviments, 'moviments')

    def setKey(self, key, value):
        # Record the state of the arrow keys
        self.keyMap[key] = value

    def moviments(self, task):

        # Moviments depenent de les tecles

        dt = globalClock.getDt()

        pas = Proteines.pas_mov * dt
        rot = Proteines.pas_rot * dt

        if self.keyMap["z"]:
            self.proteina.setY(self.proteina.getY() - pas)
        if self.keyMap["x"]:
            self.proteina.setY(self.proteina.getY() + pas)
        if self.keyMap["esquerra"]:
            self.proteina.setH(self.proteina.getH() - rot)
        if self.keyMap["dreta"]:
            self.proteina.setH(self.proteina.getH() + rot)
        if self.keyMap["endavant"]:
            self.proteina.setP(self.proteina.getP() - rot)
        if self.keyMap["enrrera"]:
            self.proteina.setP(self.proteina.getP() + rot)
        if self.keyMap["e"]:
            self.proteina.setR(self.proteina.getR() - rot)
        if self.keyMap["r"]:
            self.proteina.setR(self.proteina.getR() + rot)
        if self.keyMap["c"]:
            self.centrar_proteina()
        return task.cont

    #####################################################
    ##            REPRESENTACIONS
    #####################################################

    def atomic(self, atoms, tipus, amino, node):
        if self.tipus == 4:
            atr = Atributs(self.amino)
            aminoacid = atr.nom_aminoacid()
            text = TextNode('aminoacid')
            text.setText("Aminoacid %s . color Vermell" % (aminoacid[0]))
            textNodePath = aspect2d.attachNewNode(text)
            textNodePath.setScale(0.05)
            textNodePath.setPos(-1.1, 0, -0.80)
        for linia in self.atoms:
            resid = linia[self.nomRes]
            x = linia[self.xc]
            y = linia[self.yc]
            z = linia[self.zc]
            # id = linia[self.elem]
            atr = Atributs(linia[self.elem])
            radi = atr.radi()
            (red, green, blue, alf) = Proteines.ccolor(self, linia)
            a = loader.loadModel(self.esfera)
            a.setPos(x, y, z)
            a.setColor(red, green, blue, alf)
            a.setScale(radi)
            a.reparentTo(node)
        xmax, ymax, zmax, xmin, ymin, zmin = Proteines.extrems(self)
        eixos = LineSegs()
        eixos.moveTo(xmax + 4, 0, 0)
        eixos.drawTo(xmin - 4, 0, 0)
        eixos.moveTo(0, ymax + 4, 0)
        eixos.drawTo(0, ymin - 4, 0)
        eixos.moveTo(0, 0, zmax + 4)
        eixos.drawTo(0, 0, zmin - 4)
        eixos.setThickness(1)
        eixos.setColor(1, 1, 1, 1)
        lnode = eixos.create()
        linen = NodePath(lnode)
        linen.reparentTo(node)

        # Centre coordenades

        a = loader.loadModel(self.esfera)
        a.setPos(0, 0, 0)
        a.setColor(0, 0, 0, 1)
        a.setScale(radi)
        a.reparentTo(node)
        node.flattenStrong()

    #####################################################

    def ball_stick(self, atoms, tipus, molecules, node):
        coordenades = []

        # Posicio dels camps dins el registre atomsCA

        for idCadena in self.molecules:
            linies = [linies for linies in atoms if
                      linies[self.c] == idCadena and linies[self.prot] == True and linies[self.sig] == "CA"]
            nlin = len(linies)
            for indx in range(nlin):
                linia = linies[indx]

                # Registre atom

                x = linia[self.xc]
                y = linia[self.yc]
                z = linia[self.zc]
                elemQuim = linia[self.elem]

                # Gravar llista coordenades

                coordenades.append([x, y, z])

                # Atributs dibuix

                atr = Colors(linia[self.nomRes], 1)
                color = atr.color_tipus()
                color_LVecBase4f = (color[0], color[1], color[2], color[3])
                atr = Atributs(linia[self.elem])
                radi = atr.radi()
                a = loader.loadModel(self.esfera)
                a.setPos(x, y, z)
                a.setColor(color_LVecBase4f)
                a.setScale(0.90*radi)
                a.reparentTo(node)

            lins = LineSegs()
            for j in range(len(coordenades)):
                linia = coordenades[j]
                xx = linia[0]
                yy = linia[1]
                zz = linia[2]
                if j == 0:
                    lins.moveTo(xx, yy, zz)
                else:
                    lins.drawTo(xx, yy, zz)
            coordenades = []
            lins.setThickness(3)
            lins.setColor(1, 1, 1, 1)
            lnode = lins.create()
            linen = NodePath(lnode)
            linen.reparentTo(node)

        '''Eixos de coordenades'''

        xmax, ymax, zmax, xmin, ymin, zmin = Proteines.extrems(self)
        eixos = LineSegs()
        eixos.setColor(0, 0, 0, 1)
        eixos.setThickness(1)
        eixos.moveTo(xmax + 4, 0, 0)
        eixos.drawTo(xmin - 4, 0, 0)
        eixos.moveTo(0, ymax + 4, 0)
        eixos.drawTo(0, ymin - 4, 0)
        eixos.moveTo(0, 0, zmax + 4)
        eixos.drawTo(0, 0, zmin - 4)
        enode = eixos.create()
        elinen = NodePath(enode)
        elinen.reparentTo(node)
        node.flattenStrong()

    #####################################################

    def backbone(self, atoms, tipus, molecules, node):
        molvella = ""
        lin = LineSegs()
        for linia in atoms:
            molnova = linia[self.c]
            x = linia[self.xc]
            y = linia[self.yc]
            z = linia[self.zc]
            if molnova != molvella:
                molvella = molnova
                lin.moveTo(x, y, z)
            else:
                lin.drawTo(x, y, z)
            atr = Colors(linia[self.nomRes])
            color = atr.color_aminoacid()
            color_LVecBase4f = (color[0], color[1], color[2], color[3])
            lin.setColor(color_LVecBase4f)
        lin.setThickness(3)
        lnode = lin.create()
        linen = NodePath(lnode)
        linen.reparentTo(node)
        xmax, ymax, zmax, xmin, ymin, zmin = Proteines.extrems(self)
        eixos = LineSegs()
        eixos.setColor(0, 0, 0, 1)
        eixos.setThickness(1)
        eixos.moveTo(xmax + 4, 0, 0)
        eixos.drawTo(xmin - 4, 0, 0)
        eixos.moveTo(0, ymax + 4, 0)
        eixos.drawTo(0, ymin - 4, 0)
        eixos.moveTo(0, 0, zmax + 4)
        eixos.drawTo(0, 0, zmin - 4)
        enode = eixos.create()
        elinen = NodePath(enode)
        elinen.reparentTo(node)
        node.flattenStrong()

    ###################################################

    def linia_titol(self):

        # Canvi propietats finestra

        loadPrcFileData("", "window-title Visor proteines")
        loadPrcFileData("", "fullscreen 0")
        loadPrcFileData("", "win-size %s %s" % (1200, 1200))
        titol = self.capcalera
        title = OnscreenText(
            text=titol,
            parent=base.a2dBottomRight, align=TextNode.A_right,
            style=1, fg=(1, 1, 1, 1), pos=(-0.1, 0.1), scale=.05)

    def centrar_camera(self):

        ''' Centrar camera en l'escena '''

        self.centre = (self.proteina.getBounds().getCenter())
        proteina_radi = self.proteina.getBounds().getRadius()
        centre_escena = self.centre
        self.cam.setPos(centre_escena[0], - centre_escena[1] - 2 * proteina_radi, centre_escena[2])
        self.cam.lookAt(self.centre)

    def ccolor(self, linia):
        resid = linia[self.nomRes]
        es_prot = linia[self.prot]
        atr = Colors(resid)
        xcolor = atr.color_aminoacid()
        cl = (0, 0, 0, 1)
        if self.tipus == 2:
            if es_prot:
                atr = Colors("NNN")
                cl = atr.color_aminoacid()
            else:
                if resid != "HOH":
                    cl = (0.29, 0.4, 0.55, 1)
                else:
                    cl = (0, 0, 0, 0)
        elif self.tipus == 1:
            if es_prot:
                cl = xcolor
            else:
                cl = (0, 0, 0, 1)
        elif self.tipus == 4:
            if es_prot:
                if resid == self.amino:
                    cl = (0.65, 0.16, 0.16, 1)
                else:
                    cl = (1.00, 0.84, 0.00, 1)
            else:
                cl = (0, 0, 0, 0)
        elif self.tipus == 5:
            atr = Colors(linia[self.c], 1)
            cl = atr.color_molecula()
        elif self.tipus == 7 or self.tipus == 6:
            atr = Colors(resid, 1)
            cl = atr.color_tipus()
        else:
            cl = (0, 0, 0, 1)
        red, green, blue, alfa = cl
        return (red, green, blue, alfa)

    def centrar_proteina(self):
        self.p_radi = self.proteina.getBounds().getRadius()
        self.p_centre = self.proteina.getBounds().getCenter()
        self.x_centre, self.y_centre, self.z_centre = self.p_centre
        dx = 0 - self.x_centre
        dy = 0 - self.y_centre
        dz = 0 - self.z_centre
        self.proteina.setPos(self.x_centre + dx, self.y_centre + dy + self.p_radi, self.z_centre + dz)
        self.centre2 = self.proteina.getBounds().getCenter()

    def extrems(self):
        linies = [linies for linies in self.atoms if linies[self.prot] == True]
        xmin = 9999999
        xmax = -9999999
        ymin = 9999999
        ymax = -9999999
        zmin = 9999999
        zmax = -9999999
        for linia in linies:
            x = round(linia[self.xc], 4)
            y = round(linia[self.yc], 4)
            z = round(linia[self.zc], 4)
            if x > xmax:
                xmax = x
            if x < xmin:
                xmin = x
            if y > ymax:
                ymax = y
            if y < ymin:
                ymin = y
            if z > zmax:
                zmax = z
            if z < zmin:
                zmin = z
        return xmax, ymax, zmax, xmin, ymin, zmin
