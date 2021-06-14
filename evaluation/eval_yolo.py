from imageai.Detection.Custom import CustomObjectDetection, CustomVideoObjectDetection
import os

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(detection_model_path= "detection_model-ex-10--loss-5.86.h5")
detector.setJsonPath(configuration_json="detection_config.json")
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image= "18.jpg",
                                                 output_image_path="18-detected.jpg",
                                                 minimum_percentage_probability=40)
print(detections)

for detection in detections:
        print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
