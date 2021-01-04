import glob
import os

import cv2
import numpy

MonsterList = os.listdir('ScaledMonsters')
FormattedList = []


def read_img(img_list, img):

    numpyarray = numpy.array(img_list, dtype=object)

    return numpyarray


path = glob.glob(r"C:\Users\18862\Desktop\Overworld Bot\Main\ScaledMonsters\*.png")  # or jpg
list_ = []
cv_image = []
# cv_image = [read_img(list_, img) for img in path]

for img in path:
  cv_image.append(img)
print(cv_image)




