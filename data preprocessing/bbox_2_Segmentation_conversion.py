import torch, torchvision
print(torch.__version__, torch.cuda.is_available())
assert torch.__version__.startswith("1.8")
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()
import numpy as np
import os, json, cv2, random
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog

import pandas as pd
import cv2
import numpy as np
import ast
import matplotlib.pyplot as plt
from detectron2.structures import BoxMode

def mydataset():
  d=[]
  df=pd.read_csv("images/annotation.csv")
  for row1 in df.iterrows():
      json_dict={}
      row1=row1[1]
      pts=np.array([[ast.literal_eval(row1["top left "]),ast.literal_eval(row1["top right"]),ast.literal_eval(row1["bottom right"]),ast.literal_eval(row1["bottom left"])]],np.int32)
      filename=row1["NAME "].strip()
      image_id=0
      height=720
      width=1280
      try:
        image=cv2.resize(cv2.imread("images/"+filename),(1280,720))
        image=np.zeros([image.shape[0],image.shape[1]])
        
      except:
        print("skipped")
        continue
      x=[]
      y=[]
      cv2.fillPoly(image, [pts], 255)
      for i in range(0,len(image)):
          for j in range(0,len(image[0])):
              if image[i,j]==255:
                  x.append(j)
                  y.append(i)
      px=x
      py=y
      poly = [(x + 0.5, y + 0.5) for x, y in zip(px, py)]
      poly = [p for x in poly for p in x]ś
      annotations=[{
                      "bbox": [np.min(px), np.min(py), np.max(px), np.max(py)],
                      "bbox_mode": BoxMode.XYXY_ABS,
                      "segmentation": [poly],
                      "category_id": 0
                  }]

      json_dict["file_name"]="images/"+filename
      json_dict["image_id"]=image_id
      json_dict["height"]=image.shape[0]
      json_dict["width"]=image.shape[1]
      json_dict["annotations"]=annotations
      d.append(json_dict)
    return d