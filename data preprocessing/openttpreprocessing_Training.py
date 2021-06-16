import glob
import matplotlib.pyplot as plt
import detectron2
from detectron2.utils.logger import setup_logger
import torch
assert torch.__version__.startswith("1.8") 
setup_logger()
import numpy as np
import os, json, cv2, random
from google.colab.patches import cv2_imshow
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.structures import BoxMode
import os
import cv2
def openttcleaned():
  l=[]
  for i in glob.glob("opentt/masks/*"):
        json_dict={}
        img_path="opentt/combined/"+"img_"+str(i.split("/")[-1].split(".")[0].zfill(6))+".jpg"
        if os.path.exists(img_path):
            json_dict["file_name"]=img_path
            json_dict["image_id"]=0
            json_dict["height"]=128
            json_dict["width"]=320
            mask=cv2.imread(i)
            mask=cv2.cvtColor(mask, cv2.COLOR_RGB2HSV)

            m=cv2.inRange(mask, (100,150,0),(140,255,255))
            masked_image=cv2.cvtColor(cv2.cvtColor(cv2.bitwise_and(mask, mask, mask=m),cv2.COLOR_HSV2BGR),cv2.COLOR_BGR2GRAY)
            x=[]
            y=[]
            for i in range(0,len(masked_image)):
                  for j in range(0,len(masked_image[0])):
                        if masked_image[i,j]==29:
                            x.append(j)
                            y.append(i)
            px=x
            py=y
            poly = [(x + 0.5, y + 0.5) for x, y in zip(px, py)]
            poly = [p for x in poly for p in x]                
            annotations=[{
                      "bbox": [np.min(px), np.min(py), np.max(px), np.max(py)],
                      "bbox_mode": BoxMode.XYXY_ABS,
                      "segmentation": [poly],
                      "category_id": 0
                  }]
            json_dict["annotations"]=annotations
            l.append(json_dict)

  return l
DatasetCatalog.register("opentt", openttcleaned)
MetadataCatalog.get("opentt").set(thing_classes=["tennistable"])
balloon_metadata = MetadataCatalog.get("opentt")
from detectron2.engine import DefaultTrainer

cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
cfg.DATASETS.TRAIN = ("opentt",)
cfg.DATASETS.TEST = ()
cfg.DATALOADER.NUM_WORKERS = 2
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")  
cfg.SOLVER.IMS_PER_BATCH = 2
cfg.SOLVER.BASE_LR = 0.00025 
cfg.SOLVER.MAX_ITER = 3000   
cfg.SOLVER.STEPS = []       
cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 100  
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1 
os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)
trainer = DefaultTrainer(cfg) 
trainer.resume_or_load(resume=True)
trainer.train()
  