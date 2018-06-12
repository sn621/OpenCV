########################################
#
# AnalysiBiColorImageOTSU.py
# 
# Developed by Shunsuke Sakurai
# 
# Last update: 4 Jun 2018
#
########################################

##############################
# import libraries
##############################
import cv2
import numpy as np
from matplotlib import pyplot as plt

##############################
# read image to opencv
##############################
name_img = "../Work20180604/ARP-NWP1861_033_crop.jpg"
img = cv2.imread(name_img,0) # add 0 for gray scale

##############################
# convert image using OTSU threshold
##############################
ret, gray = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU) # for avoid addtional data, use "ret"
cv2.imwrite("fig_test_01_20180315.jpg",gray) # for checking "gray" by image file output

##############################
# draw graph about amount of black point along horizontal line
##############################
x = []
y = []

##############################
# count brack point along vertical axis
##############################
# for jj in range(len(gray[0])):
#     sums = 0
#     x.append(jj)
#     for ii in range(len(gray)):
#         sums += gray[ii][jj]
#     y.append(len(gray)-sums/255) 

##############################
# count brack point along horizontal axis
##############################
for ii in range(len(gray)):
     x.append(ii)
     y.append(len(gray[ii])-sum(gray[ii])/255)
   
thres_peak = 50
list_peakinfo = []
is_peak = False
for j_points in range(len(x)):
     if (False == is_peak and
         y[j_points] >= thres_peak):
          is_peak = True
          list_peakinfo.append(x[j_points])
     elif(True == is_peak and
          y[j_points] < thres_peak):
          is_peak = False
          list_peakinfo.append(x[j_points])
     else:
          continue
print(list_peakinfo)

for i_crop in range(int((len(list_peakinfo)-1)/2)):
     if(i_crop==0):
          #print(0,list_peakinfo[i_crop])
          continue
     else:
          print(list_peakinfo[2*i_crop],list_peakinfo[2*i_crop+1])
          cv2.imwrite("fig_test_20180604_%02d.jpg" % i_crop,gray[list_peakinfo[2*i_crop]:list_peakinfo[2*i_crop+1]]) # for checking "gray" by image file output
     
     


fig = plt.figure()
##############################
# draw graph x pix vs # black points 
##############################
g_blkp = fig.add_subplot(2,1,1)
label_blkp = [""] * 2
label_blkp[0] = "x [pixel]"
label_blkp[1] = "# of Black point along x pix"
# label_blkp[0] = "y [pixel]"
# label_blkp[1] = "# of Black point along x pix"
plt.xlabel(label_blkp[0])
plt.ylabel(label_blkp[1])
#g_blkp.set_yscale('log')
g_blkp.plot(x,y,"-")
##############################
# draw histogram x pix vs # black points 
##############################
h_blkp = fig.add_subplot(2,1,2)
label_hblkp = [""] * 2
label_hblkp[0] = "Entries"
label_hblkp[1] = "# of Black point along x pix"
# label_hblkp[1] = "# of Black point along x pix"
plt.xlabel(label_hblkp[0])
plt.ylabel(label_hblkp[1])
plt.hist(y,100)
h_blkp.set_yscale('log')
h_blkp.plot()


fig.show()


