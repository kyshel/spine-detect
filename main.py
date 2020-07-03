import os
from pprint import pprint
import numpy as np
import png
import pydicom
import matplotlib.pyplot as plt
import time

def get_date():
	return str(int(round(time.time() * 1000)))[-4:]


def dcm2png(dcm_filepath,png_filepath):
	ds = pydicom.dcmread(dcm_filepath)

	shape = ds.pixel_array.shape

	# Convert to float to avoid overflow or underflow losses.
	image_2d = ds.pixel_array.astype(float)

	# Rescaling grey scale between 0-255
	image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0

	# Convert to uint
	image_2d_scaled = np.uint8(image_2d_scaled)

	# mkdir
	dirname = os.path.dirname(png_filepath)
	if not os.path.exists(dirname):
		os.makedirs(dirname)

	# Write the PNG file
	with open(png_filepath, 'wb') as png_file:
		w = png.Writer(shape[1], shape[0], greyscale=True)
		w.write(png_file, image_2d_scaled)


 

def plotDcmList(dcm_filepath_list):
	for file in dcm_filepath_list:
		dataset = pydicom.dcmread(file)
		
		pprint(dataset.pixel_array)
		plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)

	plt.show()
 



def get_dcmFilePathList(dcm_dir):
	dcm_filepath_list =[]
	for root, dirs, files in os.walk(dcm_dir):
		for file in files:
			if file.endswith(".dcm"):
				filepath = os.path.join(root, file)
				dcm_filepath_list += [filepath]
	 
	return dcm_filepath_list









if __name__ == "__main__":

	dcm_filepath_list = get_dcmFilePathList('t')
	CUT_dcm_filepath_list = dcm_filepath_list[:]

	print(CUT_dcm_filepath_list)
	print(len(dcm_filepath_list))
 




	for file in CUT_dcm_filepath_list:
		dcm2png(file,'png\\'+file+'.png')
	print('png CREATED')
 