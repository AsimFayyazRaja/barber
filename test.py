import argparse

import torch
import numpy as np
import sys
import os
import dlib


from PIL import Image


from models.Embedding import Embedding
from models.Alignment import Alignment
from models.Blending import Blending

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

'''
mydict = {'val':'it works'}
nested_dict = {'val':'nested works too'}
mydict = dotdict(mydict)
mydict.val
'''

arguments={}


arguments['FS_steps']=250 # embedding steps
arguments['W_steps']=1100  # embedding steps
arguments['align_steps1']=140
arguments['align_steps2']=100
arguments['blend_steps']=400
arguments['ce_lambda']=1.0
arguments['channel_multiplier']=2
arguments['ckpt']='pretrained_models/ffhq.pt'
arguments['device']='cuda'
arguments['face_lambda']=1.0
arguments['hair_lambda']=1.0
arguments['im_path1']='90.png'
arguments['im_path2']='15.png'
arguments['im_path3']='117.png'
arguments['input_dir']='input/face'
arguments['l2_lambda']=1.0
arguments['l_F_lambda']=0.1

arguments['latent']=512
arguments['learning_rate']=0.01
arguments['lr_schedule']='fixed'
arguments['n_mlp']=8
arguments['opt_name']='adam'
arguments['output_dir']='output'
arguments['p_norm_lambda']=0.001
arguments['percept_lambda']=1.0
arguments['save_intermediate']=False
arguments['save_interval']=300
arguments['seed']=None
arguments['seg_ckpt']='pretrained_models/seg.pth'
arguments['sign']='fidelity'
arguments['size']=1024
arguments['smooth']=5
arguments['style_lambda']=40000.0
arguments['tile_latent']=False
arguments['verbose']=False

arguments = dotdict(arguments)

'''
FS_steps=250, W_steps=1100, align_steps1=140, align_steps2=100, blend_steps=400, ce_lambda=1.0, 
channel_multiplier=2, ckpt='pretrained_models/ffhq.pt', device='cuda', face_lambda=1.0, hair_lambda=1.0, im_path1='90.png', 
im_path2='15.png', im_path3='117.png', input_dir='input/face', l2_lambda=1.0, l_F_lambda=0.1, latent=512, learning_rate=0.01, 
lr_schedule='fixed', n_mlp=8, opt_name='adam', output_dir='output', p_norm_lambda=0.001, percept_lambda=1.0, 
save_intermediate=False, save_interval=300, seed=None, seg_ckpt='pretrained_models/seg.pth', sign='fidelity', size=1024, 
smooth=5, style_lambda=40000.0, tile_latent=False, verbose=False
'''


def blend_imgs(names=['90.png','15.png','117.png'],fs=250,wsteps=1100,align_steps1=140,align_steps2=100,blend_steps=400):
    print("--- blend_imgs ---")
    
    arguments.FS_steps=fs
    arguments.W_steps=wsteps
    arguments.align_steps1=align_steps1
    arguments.align_steps2=align_steps2
    arguments.blend_steps=blend_steps
    
    ii2s = Embedding(arguments)
    
    im_path1 = os.path.join(arguments.input_dir, names[0])
    im_path2 = os.path.join(arguments.input_dir, names[1])
    im_path3 = os.path.join(arguments.input_dir, names[2])

    im_set = {im_path1, im_path2, im_path3}
    ii2s.invert_images_in_W([*im_set])
    ii2s.invert_images_in_FS([*im_set])

    align = Alignment(arguments)
    align.align_images(im_path1, im_path2, sign=arguments.sign, align_more_region=False, smooth=arguments.smooth)
    if im_path2 != im_path3:
        align.align_images(im_path1, im_path3, sign=arguments.sign, align_more_region=False, smooth=arguments.smooth, save_intermediate=False)

    blend = Blending(arguments)
    blend.blend_images(im_path1, im_path2, im_path3, sign=arguments.sign)