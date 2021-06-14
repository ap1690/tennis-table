# Tennis-Table-Detection

- [X] Table Detection Using Basic Opencv Thresholding & Contouring

- [X] Table Detection Using Object Detector

- [X] Table Detection Using Segmentation 


![Segmentation Data](https://github.com/ap1690/tennis-table/blob/master/src/3_seg.png)
![Segmentation Data](https://github.com/ap1690/tennis-table/blob/master/src/98_seg.jpg)
![Segmentation Data](https://github.com/ap1690/tennis-table/blob/master/src/65_seg.jpg)
![Segmentation Data](https://github.com/ap1690/tennis-table/blob/master/src/93_seg.jpg)
![Segmentation Data](https://github.com/ap1690/tennis-table/blob/master/src/53.jpg)



# [MORE Inferences](https://drive.google.com/drive/folders/127Yg-1wEeQXEXr0qwPy0NpBwrkQB2XNc?usp=sharing)











- [X] Object Detector

    - [X] Cleaned and Converted Custom CSV to PascalVoc XML .  Data Preprocessing/Cleaned_CSV2VOCxml.py

    - [X] Augumented Scaledup DataSet from 500->1200 images . Used Flip X,Shear X,y,Rotation ,Noise
    ![Augumented Data](https://github.com/ap1690/tennis-table/blob/master/src/aug_train.png)
    
    - [X] Finetuned YOLOV3 for 10 Epoch .


    - [X] Total Loss : 33-->5.08 [For 10 Epoch]
    
    
    ![Fine Tuned YOLOV3](https://github.com/ap1690/tennis-table/blob/master/src/6-detected.jpg)
    
    
    
- [X] Instance Segmentation

    - [X] Converted The BBOX 512images to Instance Segmentation Dataset.  bbox_2_Segmentation_conversion.py


    - [X] Trained COCO-InstanceSegmentation  mask_rcnn_R_50_FPN  over 512 training images. Train_Instance_Segmentation_MASKRCNN.py

    ![Segmentation Data](https://github.com/ap1690/tennis-table/blob/master/src/1_seg.png)
    ![Segmentation Data](https://github.com/ap1690/tennis-table/blob/master/src/3_seg.png)
    
       
    ![Training Logs](https://github.com/ap1690/tennis-table/blob/master/src/logs.jpeg)
    
    
    ![Training Logs](https://github.com/ap1690/tennis-table/blob/master/src/tensorboard.png)
    
    
    ## Inference
    [GOOGLE COLAB](https://colab.research.google.com/drive/1rFHio8HCqRdpj-0YdcAYkPOaNWdiphBb?usp=sharing)
    
    ## Weights
    [GDRIVE](https://drive.google.com/drive/folders/1T4NpiQenrhYhE_IPrMrMQEwLsBaaE4V4?usp=sharing)
    
    
    
