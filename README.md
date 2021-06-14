# Tennis-Table-Detection



![Fine Tuned YOLOV3](https://github.com/ap1690/tennis-table/blob/master/src/14-detected.jpg)

- [X] Object Detector

    -[X] Cleaned 

    -[X] Augumented Scaledup DataSet from 500->1200 images . Used Flip X,Shear X,y,Rotation ,Noise
    ![Augumented Data](https://github.com/ap1690/tennis-table/blob/master/src/aug_train.png)
    
    -[X] Finetuned YOLOV3 for 10 Epoch .
    -[X] Total Loss : 33-->5.08 [For 10 Epoch]
    
- [X] Instance Segmentation

    -[X] Converted The BBOX 512images to Instance Segmentation Dataset.  bbox_2_Segmentation_conversion.py
    ![Segmentation Data](https://github.com/ap1690/tennis-table/blob/master/src/1_seg.png)
    ![Segmentation Data](https://github.com/ap1690/tennis-table/blob/master/src/3_seg.png)
    -[X] Trained COCO-InstanceSegmentation  mask_rcnn_R_50_FPN  over 512 training images. Train_Instance_Segmentation_MASKRCNN.py
    
    ![Training Logs](https://github.com/ap1690/tennis-table/blob/master/src/WhatsApp Image 2021-06-14 at 16.44.57.jpeg)
    
    
    ![Training Logs](https://github.com/ap1690/tennis-table/blob/master/src/tensorboard.png)
    
    
    
