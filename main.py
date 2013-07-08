import numpy as np
import locallum
import argparse
import os
import matplotlib.pyplot as plt
from scipy import misc 



parser = argparse.ArgumentParser()
parser.add_argument('files', metavar='file', type=str, nargs='+',
                   help='list of files, in order from front to back')
parser.add_argument("--raw", action="store_true",
                    help="Display raw files")
parser.add_argument("--test", action="store_true",
                   help="Get a sample from the middle of the picture, instead of proccessing the entire image")

filepaths=[]
imagearray=[]


args = parser.parse_args()
for i in  args.files:
	filepaths.append(os.path.abspath(i))

for i in filepaths:
	print (i)
	imagearray.append(misc.imread(i))

#for i in imagearray:
#	if args.raw:
		#plt.imshow(imagearray[0][1:22,1:22])

localarray = locallum.lumcalc(imagearray)

for i in localarray:
	plt.imshow(i)
plt.show()
