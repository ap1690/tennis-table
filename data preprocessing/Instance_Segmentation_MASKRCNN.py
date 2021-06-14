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
from bbox_2_Segmentation_conversion.py import *
from detectron2.engine import DefaultTrainer

DatasetCatalog.register("images", mydataset)
MetadataCatalog.get("images").set(thing_classes=["tennistable"])
balloon_metadata = MetadataCatalog.get("images")

dataset_dicts = mydataset()
for d in random.sample(dataset_dicts, 3):
    img = cv2.imread("images/"+d["filename"])
    print(d["filename"])
    visualizer = Visualizer(img[:, :, ::-1], metadata=balloon_metadata, scale=0.5)
    out = visualizer.draw_dataset_dict(d)
    plt.imshow(out.get_image()[:, :, ::-1])




def train():
        cfg = get_cfg()
        cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
        cfg.DATASETS.TRAIN = ("images",)
        cfg.DATASETS.TEST = ()
        cfg.DATALOADER.NUM_WORKERS = 2
        cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml") 
        cfg.SOLVER.IMS_PER_BATCH = 2
        cfg.SOLVER.BASE_LR = 0.00025  
        cfg.SOLVER.MAX_ITER = 2000    
        cfg.SOLVER.STEPS = []       
        cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 128  
        cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1 
        os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)
        trainer = DefaultTrainer(cfg) 
        trainer.resume_or_load(resume=True)
        trainer.train()
train()