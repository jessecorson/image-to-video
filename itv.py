#!/usr/bin/env python

import cv2
import numpy as np
import glob
import sys
import os
import argparse
import datetime
import re
import helpers.helpers as h

parser = argparse.ArgumentParser(description='Convert images to video')
parser.add_argument('-p',metavar='path', type=str, help='Path of images')
parser.add_argument('-o',metavar='path', type=str, help='Output video path')
parser.add_argument('-n',metavar='path', type=str, help='Output video name')
args = parser.parse_args()

today = datetime.datetime.today()
# Checking args
if isinstance(args.p, str):
    path = args.p
else:
    path=os.getcwd()
path = h.endwith(path, '/')

if isinstance(args.o, str):
    output_path = h.endwith(args.o, '/')
else:
    output_path = './'

if isinstance(args.n, str):
    output_filename = 'project'
else:
    output_filename = today.strftime('Project-%Y-%m-%d-%H%M%S')
output_filename = h.endwith(output_filename, '.avi')

def makeVideo(path: str, output_path: str, output_filename: str):
    # Reading files
    img_array = []
    print('Finding files in ' + path)
    total = 0
    for filename in glob.glob(path + '/*.[J,j][P,p][G,g]'):
        total += 1
        # print(filename)
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    
    if total == 0:
        sys.exit('No jpeg files found in ' + path)

    print('Adding ' + str(total) + ' to video')
    
    video_filename = output_path + output_filename
    fps = 15

    out = cv2.VideoWriter(video_filename,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

    print('Created video ' + video_filename)

if __name__ == "__main__":
    makeVideo(path,output_path,output_filename)



