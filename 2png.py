import os
import numpy as np
from PIL import Image

dataset_dir='../autodl-tmp/1'
output_dir='../autodl-tmp/1_png'
file_list=os.listdir(dataset_dir)

for file in file_list:
	name,ext =file.split('.')
	img_path=dataset_dir+'/'+file
	save_path=output_dir+'/'+file
	if ext == 'jpg':
		save_path= output_dir+'/'+name+'.png'
	img=Image.open(img_path)
	img.save(save_path)
