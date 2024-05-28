from torchvision import transforms
import os
import numpy
from PIL import Image

dataset_dir='/root/resnet/data/val/0'
output_dir='/root/resnet/data/val_t/0'
SIZE=224
angles=[90, 180, 270]

file_list=os.listdir(dataset_dir)

for file in file_list:
    name,ext =file.split('.')
    img_path=dataset_dir+'/'+file
    if ext == 'png':
        save_path= output_dir+'/'+name+'.png'
        img=Image.open(img_path)
        #resize
        img_resized = img.resize((SIZE,SIZE))
        img_resized.save(output_dir+'/'+file)
        #horizonal flip
        img_flip = transforms.functional.hflip(img_resized)
        img_flip.save(output_dir+'/'+name+'_flip'+'.png')
        for a in angles:
            img_r=transforms.functional.rotate(img_resized,a)
            img_r.save(output_dir+'/'+name+'_'+str(a)+'.png')
            img_flip_r=transforms.functional.rotate(img_flip,a)
            img_flip_r.save(output_dir+'/'+name+'_flip_'+str(a)+'.png')
        
        print('saved '+name)
