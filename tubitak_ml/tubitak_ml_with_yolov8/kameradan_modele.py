import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2
import numpy as np
from modeli_deneme import YOLOv8Model  
class ImageProcessor(Node):
    def __init__(self):
        super().__init__('image_processor')
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10)
        self.subscription
        self.publisher_ = self.create_publisher(String, 'potato_classification', 10)
        self.bridge = CvBridge()
        self.model = YOLOv8Model()  
    def image_callback(self, msg):
       
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        results = self.model.predict(cv_image) 
        classification, width, height = self.get_classification(results)
       
        msg = String()
        msg.data = f'{classification},{width},{height}'
        self.publisher_.publish(msg) 
        self.get_logger().info(f'Publishing: "{msg.data}"')
    def get_classification(self, results):
        
        if results:
            for result in results:
                if result.boxes is not None:
                    for box in result.boxes:
                        class_id = int(box.cls[0])  # Sınıf ID'si
                        x_min, y_min, x_max, y_max = box.xyxy[0]  
                        width = x_max - x_min
                        height = y_max - y_min
                        classification = result.names[class_id]
                        return classification, width, height
        return 'Unknown', None, None
def main(args=None):
    rclpy.init(args=args)
    image_processor = ImageProcessor()
    rclpy.spin(image_processor)
    image_processor.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()