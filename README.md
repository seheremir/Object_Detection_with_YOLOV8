# Object_Detection_with_YOLOV8
Object Detection and Tracking in Smart Factories Using Real-Time Image Processing
Within the scope of TUBITAK supported project, object detection in fully automated smart factories with YOLOV8. In this study, potatoes on the production line in a factory were detected on the basis of 5 classes:  'Defected potato', 'Damaged potato', 'Diseased-fungal potato', 'Potato' and 'Sprouted potato'.

As a result of this image recognition process:  
Total number of images in the validation set (1785 images).
Total number of detected objects (6360).
Box detection accuracy (Precision): 0.797, i.e. 79.7% of the detected objects are correct.
R (Recall): 0.757, i.e. 75.7% of the actual objects were detected correctly.
mAP50 Average accuracy with IoU of 0.5: 83.9%.
Average accuracy with mAP50-95 IoU values ranging from 0.5 to 0.95: 68.9%.

Results by Class:

-Damaged potato:
Precision: 0.739 (Accuracy 73.9%)
Recall: 0.708 (Sensitivity 70.8%)
mAP50: 0.782 (78.2% accuracy for IoU 0.5)
mAP50-95: 0.663 (66.3% accuracy between IoU 0.5-0.95)

-Defected potato
Precision: 0.763
Recall: 0.743
mAP50: 0.8
mAP50-95: 0.67

-Diseased-fungal potato
Precision: 0.809
Recall: 0.782
mAP50: 0.879
mAP50-95: 0.747

-Potato
Precision: 0.82
Recall: 0.839
mAP50: 0.902
mAP50-95: 0.758

-Sprouted potato
Precision: 0.852
Recall: 0.711
mAP50: 0.832
mAP50-95: 0.606

These values obtained within the scope of the project will be simulated in the ROS2 environment.
