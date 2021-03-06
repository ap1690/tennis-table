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

    - [X] Cleaned and Converted Custom CSV to PascalVoc XML . 
  
  
             Data Preprocessing/Cleaned_CSV2VOCxml.py

    - [X] Augumented Scaledup DataSet from 500->1200 images . Used Flip X,Shear X,y,Rotation ,Noise

    - [X] Finetuned YOLOV3 for 10 Epoch .
               
             Train/yoloV3_finetuning.py

    - [X] Total Loss : 33-->5.08 [For 10 Epoch]
    ![Augumented Data](src/aug_train.png)
    

    
    
    ![Fine Tuned YOLOV3](src/6-detected.jpg)
    
    
    
- [X] Instance Segmentation
    -  [X] Custom Dataset




        - [X] Converted The BBOX 512images to Instance Segmentation Dataset.  bbox_2_Segmentation_conversion.py

                data preprocessing/bbox_2_Segmentation_conversion.py 


        - [X] Trained COCO-InstanceSegmentation  mask_rcnn_R_50_FPN  over 512 training images. Train_Instance_Segmentation_MASKRCNN.py

                 Train/Train_Instance_Segmentation_MASKRCNN.py 
                 
                 
    - [X] Fine Tuning On OPENTTDATASET

        ![Segmentation Data](src/890.png)
        ![Segmentation Data](src/893.png)
        ![Segmentation Data](src/896.png)
        
        - [X] Preprocessing Of OpenTTDataset and Training. Coversion of masked with 3 classes-->Tennis Table Extracting
                                         
                -data processing/openttpreprocessing_Training.py

    # Custom
    ![Segmentation Data](src/1_seg.png)
    ![Segmentation Data](src/3_seg.png)
    
     # [MORE INFERENCE RESULT](https://drive.google.com/drive/folders/127Yg-1wEeQXEXr0qwPy0NpBwrkQB2XNc?usp=sharing)
     
    
    # OpenTTDataset
    ![Segmentation Data](src/opentt_cleaning.png)
    ![Segmentation Data](src/opentt_cleaning1.png)
    
     # [MORE INFERENCE RESULTS](https://drive.google.com/drive/folders/10DP4s95B4YTjctJFa5acgICWIOfsMtVN?usp=sharing)
    
   
    
    
    # TRAINING CURVE
    
        tennis-table/config/metrics.json
    ![Training Logs](src/logs.jpeg)
    
    
    ![Training Logs](src/tensorboard.png)
    
    
    ## Inference
    [GOOGLE COLAB](https://colab.research.google.com/drive/1rFHio8HCqRdpj-0YdcAYkPOaNWdiphBb?usp=sharing)
    
    ## Weights
    [GDRIVE](https://drive.google.com/drive/folders/1T4NpiQenrhYhE_IPrMrMQEwLsBaaE4V4?usp=sharing)
    
    
    
