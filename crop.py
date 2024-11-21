import cv2
import sys
import numpy as np
import os

def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    # im decode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
    #cv_img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
    return cv_img

WIDTH = 1280
HEIGHT = 720

dir_name = sys.argv[1]
in_file_name = sys.argv[2]
filename = sys.argv[3]
out_file_name = dir_name + "\\cropped\\" + filename + ".png"
out_dir = dir_name + "\\cropped"

if not os.path.exists(out_dir):
    os.mkdir(out_dir)

img = cv_imread(in_file_name)
cropped = img[0:HEIGHT, 0:WIDTH]
#print(dir_name + "\\cropped\\" + filename + ".png")
#cv2.imwrite(dir_name + "\\cropped\\" + filename + ".png", cropped)
cv2.imencode('.png', cropped)[1].tofile(dir_name + "\\cropped\\" + filename + ".png")