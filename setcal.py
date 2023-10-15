import os
import calculate

hr_path='/root/autodl-tmp/valid_HR'
sr_path='/root/autodl-tmp/valid_SR'
hr_set=os.listdir(hr_path)
sr_set=os.listdir(sr_path)
hr_set.sort()
sr_set.sort()
scale= len(hr_set)

output=[0,0]

for i in range(scale):
    name_hr, ext_hr = hr_set[i].split('.')
    name_sr, ext_sr = sr_set[i].split('.')
    if (ext_hr=='png') & (ext_sr=='png'):
        result= calculate.image(hr_path+'/'+hr_set[i], sr_path+'/'+sr_set[i])
        output[0]+=result[0]
        output[1]+=result[1]
    
print('psnr='+str(output[0]/scale))
print('ssim='+str(output[1]/scale))
