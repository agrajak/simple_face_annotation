#-*- coding: utf-8 -*-
import os.path as p
import os
import cv2 as cv
import numpy as np
def load_images():
  global imageList, input_dir, output_dir
  imageList = []
  input_dir = p.normpath(os.getcwd()+'/input')
  if p.isdir(input_dir) == False:
    print(input_dir, 'is not directory!')
    exit(1)

  for f in os.listdir(input_dir):
    _f = p.join(input_dir, f)

    output_dir = p.join(input_dir, 'output')
    if p.exists(output_dir) == False:
      os.mkdir(output_dir)

    if p.isfile(_f):
      imageList.append(_f)
  print(len(imageList), 'image files available!')

def show_image(imagePath, idx):

  img = cv.imread(imagePath, -1)
  print('image shape is', img.shape)
  r = cv.selectROI(img, False)
  print(r[0], r[1], r[2], r[3])
  result = "%d_%s_%d_%d_%d_%d.jpg" % (idx, name, r[0], r[1], r[2], r[3])
  file_path = p.join(output_dir, result)
  print('target file_path is ', file_path)
  cv.imwrite(file_path, img)
  print('done!')
  
if __name__ == '__main__':
  global startNum, name
  load_images()
  print('[increasing number]_[x]_[y]_[width]_[height]_[name].jpg will be annoated in file name!')
  name = input('Name?')
  startNum = int(input('Number? (1 is recommended)'))
  
  print('===START===')
  for idx, image in enumerate(imageList):
    print(idx+'/'+len(imageList), 'target: ', image)

    show_image(image, idx+startNum)

  print('===END===')
