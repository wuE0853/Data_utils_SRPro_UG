import os
import numpy
from PIL import Image
from PIL import ImageFilter

dataset_dir='/root/autodl-tmp/valid_HR'
output_dir='/root/autodl-tmp/valid_LR'

file_list=os.listdir(dataset_dir)
for file in file_list:
	name,ext =file.split('.')
	img_path=dataset_dir+'/'+file
	if ext == 'png':
		save_path= output_dir+'/'+name+'.png'
		img=Image.open(img_path)
		blurred_img=img.filter(ImageFilter.GaussianBlur(radius=3))
		blurred_img.save(save_path)
		print('saved '+name)
		
