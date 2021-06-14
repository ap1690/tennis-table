import glob
import cv2
count=0
for i in glob.glob("images/*.jpg"):
  try:
    cv2.imwrite(i,cv2.resize(cv2.imread(i),(1280,720)))
    count+=1
  except:
    print("skipped")