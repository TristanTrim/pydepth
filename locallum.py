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
	
	######useful variables
	
	###get size value of the images in imagearray
	imagearray_imagesize=[]
	for i in imagearray:
		imagearray_imagesize.append(i.shape)
	print(imagearray_imagesize[0])
	testsize=[400,300]##in format: [y,x]..... Ill fix it if it ever becomes a problem.
	
	lumsample=[range(-1,2),range(-1,2)]
	#for i in lumsample[0]:
	#	print(str(i))

	input_image=[]


###this next if loop will neet to be in a loop of images for multiple images

	
	###for simulated for loop, we can change this lator.
	###the for loop is no longer simulated...
	imageNumberLoop=(len(imagearray))
	for imageNumber in range(0,imageNumberLoop):
		#print(str(imageNumber)+"####!!!!%$%$%$%$%")

		#if --test is on then only do one image, at testsize.
		if __main__.args.test: 
			#set xy size of sample
			#define sample from image
			input_image.append(imagearray[imageNumber][imagearray_imagesize[imageNumber][0]/2-testsize[0]/2:imagearray_imagesize[imageNumber][0]/2+testsize[0]/2,imagearray_imagesize[imageNumber][1]/2-testsize[1]/2:imagearray_imagesize[imageNumber][1]/2+testsize[1]/2])
			##set imagearray_imagesize to the new images size
			imagearray_imagesize[imageNumber]=input_image[imageNumber].shape###this only needs to  be done because the test size is smaller then the regular image.

		#else define imsample from full image:::
		else:
			input_image=imagearray
			#input_image[imageNumber].append(imagearray[imageNumber])
			#for i in(0,1):
				#samplesize[i]=arraysize[i]###Im not sure what this was supposed to do...oh, it was supposed to get the imagesize for creating the new image that data would be written to.
	
	
		###generate array full of zeros for the calculations
		print(imagearray_imagesize[imageNumber][0])
		luminescence=np.zeros((imagearray_imagesize[imageNumber][0],imagearray_imagesize[imageNumber][1],3))
		lumarray=[]	
		#Runs through every image that's passed to the command line (imagearray)
	#for image in imagearray:
		#print(image)
		##tells it to work with pixel data that's one pixel away from the edges, this way you're never trying to get something that doesn't exist in your 3*3 sample.
		for i in range(1,imagearray_imagesize[imageNumber][0]-1):
			#luminescence+=[]
			for j in range(1,imagearray_imagesize[imageNumber][1]-1):
				for a in lumsample[0]:
					for b in lumsample[1]:
						luminescence[i,j]+=input_image[imageNumber][i+a,j+b]
			luminescence[i,j]=input_image[imageNumber][i,j]-(luminescence[i,j]/(len(lumsample[0])*len(lumsample[1])))
					#for k in range(1,3):
				#imsample[i,j][test]=imsample[i,j][test]=0
			print("Currently on the "+str(i)+"irstest line of "+str(imagearray_imagesize[imageNumber][0])+" on the "+str(imageNumber)+"eth image", end='\r')
		lumarray.append(luminescence)
	return(lumarray)
#####in case I forget, luminescence is not interacting with imageNumber at all, so it would output the last image rendered only... this would suck.
