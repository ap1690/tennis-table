from imageai.Detection.Custom import DetectionModelTrainer
trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="tt_table")
trainer.setTrainConfig(object_names_array=["table"], batch_size=10, num_experiments=20, train_from_pretrained_model="/content/drive/MyDrive/tt_table/models/detection_model-ex-10--loss-5.86.h5",)
trainer.trainModel()

