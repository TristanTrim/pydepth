"""
A script to calculate the luminescence of pixels in an image and maybe do some other stuff.

started by Trist on july 04 at 1:14 in the am.
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt
import __main__

#function takes image and returns luminosity array

#simply adds the red values for every pixel in a 3*# square, then divids by 9 avergining it out. Then it does the same for blue and green, finaly building a new image with that colour value.

def lumcalc(imagearray):
	
	#useful variables
	arraysize = imagearray[0].shape
	samplesize=[600,400]
	lumsample=[range(-1,2),range(-1,2)]
	#for i in lumsample[0]:
	#	print(str(i))

	#if --test is on then only do one image, at samplesize.
	if __main__.args.test: 
		#set xy size of sample
		#define sample from image
		imsample=imagearray[0][arraysize[0]/2-samplesize[0]/2:arraysize[0]/2+samplesize[0],arraysize[1]/2-samplesize[1]:arraysize[1]/2+samplesize[1]]
	#else define imsample from full image:::
	else:
		imsample=imagearray[0]
		for i in(0,1):
			samplesize[i]=arraysize[i]
	
	
	#generate array full of zeros for the calculations
	luminescence=np.zeros((samplesize[0],samplesize[1],3))
	lumarray=[]	
	#Runs through every image that's passed to the command line (imagearray)
	for image in imagearray:
		print(image)
		##tells it to work with pixel data that's one pixel away from the edges, this way you're never trying to get something that doesn't exist in your 3*3 sample.
		for i in range(1,samplesize[0]-1):
			#luminescence+=[]
			for j in range(1,samplesize[1]-1):
				for a in lumsample[0]:
					for b in lumsample[1]:
						luminescence[i,j]+=imsample[i+a,j+b]
			luminescence[i,j]=imsample[i,j]-(luminescence[i,j]/(len(lumsample[0])*len(lumsample[1])))
					#for k in range(1,3):
				#imsample[i,j][test]=imsample[i,j][test]=0
			print("Currently on the "+str(i)+"stest line!", end='\r')
		lumarray.append(luminescence)
	return(lumarray)

