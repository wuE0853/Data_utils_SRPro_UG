import os

path='/root/HAT/results/HAT-S_SRx2/visualization/HE'

files=os.listdir(path)

for file in files:
    name,ext= file.split('.')
    if ext=='png':
        os.rename(path+'/'+file, path+'/'+file.replace('_HAT-S_SRx2', ''))
