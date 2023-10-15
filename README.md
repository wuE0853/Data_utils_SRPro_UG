# Data_utils_SRPro_UG
the data utils procedure of the project Super-Revolution Reconstruction Method of Cytological Images of Endometrial Cancer Based on Deep Learning.

BRANCH- psnr_ssim_calcualtion

setting environment:(python 3.6)
conda install pytorch==1.1.0 torchvision==0.3.0 cudatoolkit=10.0 -c pytorch
pip install pillow==5.2.0
pip install opencv-python
pip install scipy


The data set(jpg image)
training set: the images begin with 0_1 or 1_1
testing set: the images begin with 0-9 or 1-9


Processing:
1. Editing the path in setcal.py
2. Run setcal.py
