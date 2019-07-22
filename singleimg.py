-4# -*- coding: utf-8 -*-
"""
Single Himawari Image Processing

@author: chnan 2019 0613
"""
import numpy as np
import matplotlib
matplotlib.rcsetup.interactive_bk
matplotlib.use('Qt4Agg')
import re
import os
patha=r'D:\Users\CHNAN\Documents\pork\hima'
import time
os.chdir(patha)
import cv2                
import matplotlib.pyplot as plt 
tfnam='hima0803.png'
from matplotlib.pyplot import ginput
img=cv2.imread(tfnam)
data=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

fig=plt.figure(figsize=(14,14),edgecolor='w')
## original pictures Display ---------------------
plt.imshow(data,cmap='gray')
#ss=ginput(2)
plt.draw()
plt.pause(0.0001)

#pictures info from IPython Ginputs =============================
figcorner=np.array([(164.8738738738739, 84.85097597597587),
 (162.21496496496502, 1855.6843093093094),
 (1935.7072072072067, 1853.0254004004005),
 (1933.0482982982978, 84.85097597597587)])

lonr=np.array([(381.16974415802144, 968.7414126664892),
 (678.2303113511065, 968.7414126664892),
 (973.1225532362128, 968.7414126664892),
 (1270.1831204292978, 968.7414126664892),
 (1567.2436876223828, 968.7414126664892)])

latr=np.array([(680.3986366590851, 1192.0789193882974),
 (680.3986366590851, 968.7414126664892),
 (678.2303113511065, 745.4039059446807),
 (678.2303113511065, 524.234724530851),
 (678.2303113511065, 303.0655431170212)])

actlon=np.array([100,120,140,160,180])
actlat=np.array([-15,0,15,30,45])

#End of IPython Ginputs =========================================


figcorner=np.round(figcorner)
figcol=np.round(np.array([np.average(figcorner[0:2,0]),np.average(figcorner[2:4,0])]))
figrow=np.array([np.average(figcorner[0:4,1]),np.average(figcorner[1:3,1])])
figrow[0]=figrow[0]*2-figrow[1]
figrow=np.round(figrow)
print('='*50)
print('Himawari8 Axis Column pixels range = ',figcol)
print('Himawari8 Axis Row pixels range = ',figrow)
print('='*50)

# lon resolution
tmplon=np.round(lonr[:,0])
tmplat=np.round(latr[:,1])
tmplondif=np.round(np.average(np.diff(tmplon)))
tmplatdif=np.round(np.average(np.diff(tmplat)))

minlon=np.round(np.average(actlon)-(np.average(tmplon)-figcol[0])/tmplondif*20)
maxlon=np.round(np.average(actlon)-(np.average(tmplon)-figcol[1])/tmplondif*20)
minlat=-60.0
maxlat=60.0

degperpix=tmplondif/20 # manual confirmed lon/lat resolution pix/deg are identical
print('Resolution (pixel/deg) is ',degperpix)
print(' Spatial resolution is (km/pixel near equator) is ~',round(110/degperpix,1),' km')
print('='*50)
print('Himawari8 Lon range = ',[minlon,maxlon])
print('Himawari8 Lat range = ',[minlat,maxlat])
print('='*50)


tyboxlen=297 # typhoon box size (pixel)

# CV2 Box
#x, y, w, h = cv2.boundingRect(mask)
#rect1 = cv2.rectangle(img.copy(),(x,y),(x+w,y+h),(0,255,0),3) 
#print("x:{0}, y:{1}, width:{2}, height:{3}".format(x, y, w, h))
#plt.imshow(rect1)
#plt.show()



