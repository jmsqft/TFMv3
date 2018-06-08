##!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
so=sys.platform
if so == 'win32' or  so=="win64":
    os.system('cls')
else:
    os.system('clear')

texts=[]

texts.append("OPCIO  2D i pseudo 3D        Matplotlib                                                     Param 1     Param2     ")
texts.append("----------------------------------------------------------------------------------         --------    ------------")
texts.append("A01.Representacio en pseudo-3d dels atoms acolorits per molecules                             a           molecula ")
texts.append("A02.Representacio en pseudo-3d dels residus (carbonis alfa) per molecules                     a           residu")
texts.append("A03.Representacio en 2D i pseudo 3D                                                           a           vistes")
texts.append("A04.Representacio en linies per molecules en pseudo 3D                                        c           molecula")
texts.append("A05.Representacio en linies dels residus en pseudo 3D segons tipus aminoacid                  c           tipus")
texts.append(" ")
texts.append(" ")
texts.append(" ")
texts.append("OPCIO  2D i pseudo 3D        Matplotlib                                                     Param 1       Param2          Param3")
texts.append("----------------------------------------------------------------------------------          --------      ---------     ------------")
texts.append("B01.Representacio del complex proteic seguns color aminoacids                                  a           residu")
texts.append("B02.Representacio dels elements externs a la proteina                                          a           extern")
texts.append("B03.Representacio per tipus aminoacids                                                         a           tipus")
texts.append("B04.Representacio ubicacio d'un aminoacid concret                                              a           amino       sigles_aminoa")
texts.append("B05.Representacio del complex per molecules                                                    a           molecula")
texts.append("B06.Representacio ball & stick els  acolorit per tipus  aminoàcid                              c           alfa")
texts.append("B07.Representacio tipus backbone                                                               c           tipus")
for text in texts:
    print(text)
    



