"""
A script to calculate the luminescence of pixels in an image and maybe do some other stuff.

started by Trist on july 04 at 1:14 in the am.
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt


#function takes image and returns luminosity array
def lumcalc(imagearray):
	
	#useful variables
	arraysize = imagearray[0].shape
	samplesize=[600,400]
	lumsample=[range(-1,2),range(-1,2)]
	#for i in lumsample[0]:
	#	print(str(i))
	print(str(len(lumsample[0])*len(lumsample[1]))+" equals 3*3 equals 9. at least it should.")
	
	#samplemode:::
	samplemode=True
	if samplemode:
		#set xy size of sample
		#####samplesize=[500,500]
		#define sample from image
		imsample=imagearray[0][arraysize[0]/2-samplesize[0]/2:arraysize[0]/2+samplesize[0],arraysize[1]/2-samplesize[1]:arraysize[1]/2+samplesize[1]]
	#else define imsample from full image:::
	else:
		imsample=imagearray[0]
		for i in(0,1):
			samplesize[i]=arraysize[i]
	
	
	#generate array full of zeros for the calculations
	luminescence=np.zeros((samplesize[0],samplesize[1],3))
	
	
	for i in range(1,samplesize[0]-1):
		#luminescence+=[]
		for j in range(1,samplesize[1]-1):
			for a in lumsample[0]:
				for b in lumsample[1]:
					luminescence[i,j]=imsample[i+a,j+b]
			luminescence[i,j]=imsample[i,j]-luminescence[i,j]/(len(lumsample[0])*len(lumsample[1]))
				#for k in range(1,3):
			#imsample[i,j][test]=imsample[i,j][test]=0
		print("I made the "+str(i)+"stest line!")
	
	return(luminescence)

