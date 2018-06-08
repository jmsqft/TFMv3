#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
========================
Colors
========================
'''

from __future__ import division

import matplotlib.pyplot as plt


taula_colors=[
[[1,"Negre","u'Negre'",u'#000000',[0.00,0.00,0.00]],
[2,"Verd fosc","u'Verd fosc'",u'#006400',[0.00,0.39,0.00]],
[3,"Gris","u'Gris'",u'#808080',[0.50,0.50,0.50]],
[4,"Vermell fosc","u'Vermell fosc'",u'#8B0000',[0.55,0.00,0.00]],
[5,"Marró","u'Marró'",u'#A52A2A',[0.65,0.16,0.16]],
[6,"Roig indi","u'Roig indi'",u'#CD5C5C',[0.80,0.36,0.36]],
[7,"Carmesí","u'Carmesí'",u'#DC143C',[0.86,0.08,0.24]],
[8,"Caqui fosc","u'Caqui fosc'",u'#BDB76B',[0.74,0.72,0.42]],
[9,"Taronja fosc","u'Taronja fosc'",u'#FF8C00',[1.00,0.55,0.00]],
[10,"Verd llima","u'Verd llima'",u'#32CD32',[0.20,0.80,0.20]],
[11,"Groc verd","u'Groc verd'",u'#9ACD32',[0.60,0.80,0.20]],
[12,"Or","u'Or'",u'#FFD700',[1.00,0.84,0.00]],
[13,"Groc","u'Groc'",u'#FFFF00',[1.00,1.00,0.00]],
[14,"Mig violeta vermell","u'Mig violeta vermell'",u'#C71585',[0.78,0.08,0.52]],
[15,"Rosa profund","u'Rosa profunda'",u'#FF1493',[1.00,0.08,0.58]],
[16,"Cian fosc","u'Cian fosc'",u'#008B8B',[0.00,0.55,0.55]],
[17,"Llum mar verd","u'Llum mar verd'",u'#20B2AA',[0.13,0.70,0.67]],
[18,"Mar verd fosc","u'Mar verd fosc'",u'#8FBC8F',[0.56,0.74,0.56]],
[19,"Marron Rosy ","u'Marron Rosy '",u'#BC8F8F',[0.74,0.56,0.56]],
[20,"Plata","u'Plata'",u'#C0C0C0',[0.75,0.75,0.75]],
[21,"Verd pàl·lid","u'Verd pàl·lid'",u'#98FB98',[0.60,0.98,0.60]],
[22,"Blau","u'Blau'",u'#0000FF',[0.00,0.00,1.00]],
[23,"Blau reial","u'Blau reial'",u'#4169E1',[0.25,0.41,0.88]],
[24,"Violeta mitjà","u'Violeta mitjà'",u'#9370DB',[0.58,0.44,0.86]],
[25,"Orquídia fosca","u'Orquídia fosca'",u'#9932CC',[0.60,0.20,0.80]],
[26,"Fucsia","u'Fucsia'",u'#FF00FF',[1.00,0.00,1.00]],
[27,"Blau profund marí","u'Blau profund marí'",u'#00BFFF',[0.00,0.75,1.00]],
[28,"Blau Dodger","u'Blau Dodger'",u'#1E90FF',[0.12,0.56,1.00]],
[29,"Prunera","u'Prunera'",u'#DDA0DD',[0.87,0.63,0.87]],
[30,"Rosa clar","u'Rosa clar'",u'#FFB6C1',[1.00,0.71,0.76]],
[31,"Pale Turquesa","u'Pale Turquesa'",u'#AFEEEE',[0.69,0.93,0.93]],
[32,"Lavanda","u'Lavanda'",u'#E6E6FA',[0.90,0.90,0.98]],
[33,"Blanc antic","u'Blanc antic'",u'#FAEBD7',[0.98,0.92,0.84]],
[34,"Neu","u'Neu'",u'#FFFAFA',[1.00,0.98,0.98]]]]

colors = {u'Negre' : u'#000000',	u'Verd fosc' : u'#006400',	u'Gris' : u'#808080',	u'Vermell fosc' : u'#8B0000',
        u'Marró' : u'#A52A2A',	u'Roig indi' : u'#CD5C5C',	u'Carmesí' : u'#DC143C',	u'Caqui fosc' : u'#BDB76B',
        u'Taronja fosc' : u'#FF8C00',	u'Verd llima' : u'#32CD32',	u'Groc verd' : u'#9ACD32',	u'Or' : u'#FFD700',
        u'Groc' : u'#FFFF00',	u'Mig violeta vermell' : u'#C71585',	u'Rosa profund' : u'#FF1493',
        u'Cian fosc' : u'#008B8B',	u'Llum mar verd' : u'#20B2AA',	u'Mar verd fosc' : u'#8FBC8F',
        u'Marron Rosy ' : u'#BC8F8F',	u'Plata' : u'#C0C0C0',	u'Verd pàl·lid' : u'#98FB98',	u'Blau' : u'#0000FF',
        u'Blau reial' : u'#4169E1',	u'Violeta mitjà' : u'#9370DB',	u'Orquídia fosca' : u'#9932CC',
        u'Fucsia' : u'#FF00FF',	u'Blau profund marí' : u'#00BFFF',	u'Blau Dodger' : u'#1E90FF',
        u'Prunera' : u'#DDA0DD',	u'Rosa clar' : u'#FFB6C1',	u'Turquesa Pal·lit' : u'#AFEEEE',	u'Lavanda' : u'#E6E6FA',
        u'Blanc antic' : u'#FAEBD7',	u'Neu' : u'#FFFAFA'}

noms=[]
color=[]


for key in colors:
    noms.append(key)
    color.append(colors[key])
    
n = len(noms)
ncols = 4
nrows = n // ncols + 1

fig, ax = plt.subplots(figsize=(5,6))

# Get height and width
X, Y = 150 * fig.get_size_inches()
h = Y / (nrows + 1)
w = X / ncols

for i, nom in enumerate(noms):
    col = i % ncols
    row = i // ncols
    y = Y - (row * h) - h
    xi_line = w * (col + 0.05)
    xf_line = w * (col + 0.25)
    xi_text = w * (col + 0.3)
    ax.text(xi_text, y, nom, fontsize=(h * 0.2), horizontalalignment='left', verticalalignment='center')
    ax.hlines(y + h * 0.1, xi_line, xf_line, color=colors[nom], linewidth=(h * 0.6))

ax.set_xlim(0, X)
ax.set_ylim(0, Y)
ax.set_axis_off()

fig.subplots_adjust(left=0, right=1, top=1, bottom=0, hspace=0, wspace=0)
plt.show()

