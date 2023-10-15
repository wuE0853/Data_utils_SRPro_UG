import cv2
import torch
import math
import numpy as np
import pytorch_ssim
from PIL import Image
from skimage.measure import compare_psnr, compare_ssim

def image(hr_name, sr_name):
    hr_image = cv2.imread(hr_name)
    sr_image = cv2.imread(sr_name)
    sr_image = cv2.resize(sr_image,(256,256))
    hr_image = cv2.resize(hr_image,(256,256))

    psnr= compare_psnr(hr_image, sr_image)
    ssim = compare_ssim(hr_image, sr_image, multichannel= True)
    print (hr_name+' '+sr_name)
    print(psnr)
    print(ssim)
    result=[psnr,ssim]
    return result
