import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PotatoProcessor(Node):
    def __init__(self):
        super().__init__('potato_processor')
        self.subscription = self.create_subscription(
            String,
            'potato_classification',
            self.classification_callback,
            10)
        self.subscription
        # Üretim hattına sinyal gönderen yayıncılar
        self.normal_potato_pub = self.create_publisher(String, 'normal_potato_line', 10)
        self.defective_potato_pub = self.create_publisher(String, 'defective_potato_line', 10)

    def classification_callback(self, msg):
        # Gelen sınıflandırma ve boyut bilgilerini işler
        data = msg.data.split(',')
        classification = data[0]
        width = float(data[1]) if data[1] != 'None' else None
        height = float(data[2]) if data[2] != 'None' else None

        self.get_logger().info(f'Received: Classification: {classification}, Width: {width}, Height: {height}')

        # Sınıflandırmaya göre yönlendirme kararını alır
        if classification == 'Normal Patates' and width is not None and height is not None:
            self.route_to_normal_line(width, height)
        else:
            self.route_to_defective_line()

    def route_to_normal_line(self, width, height):
        msg = String()
        msg.data = f"Patates normal üretim hattına yönlendiriliyor. Boyutlar: {width}x{height}"
        self.normal_potato_pub.publish(msg)
        self.get_logger().info(f"Normal üretim hattına yönlendirildi: {msg.data}")

    def route_to_defective_line(self):
        msg = String()
        msg.data = "Kusurlu patates üretim hattına yönlendiriliyor."
        self.defective_potato_pub.publish(msg)
        self.get_logger().info("Kusurlu üretim hattına yönlendirildi.")

def main(args=None):
    rclpy.init(args=args)
    potato_processor = PotatoProcessor()
    rclpy.spin(potato_processor)
    potato_processor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

