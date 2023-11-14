import os
import numpy
from PIL import Image

dataset_dir='/root/autodl-tmp/valid_HR'
output_dir='/root/autodl-tmp/valid_HR_128'
SIZE=128

file_list=os.listdir(dataset_dir)
for file in file_list:
	name,ext =file.split('.')
	img_path=dataset_dir+'/'+file
	if ext == 'png':
		save_path= output_dir+'/'+name+'.png'
		img=Image.open(img_path)
		resized_image = img.resize((SIZE,SIZE))
		resized_image.save(save_path)
		print('saved '+name)
		
