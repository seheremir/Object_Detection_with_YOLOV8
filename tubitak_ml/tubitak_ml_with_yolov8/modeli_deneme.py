import cv2
from ultralytics import YOLO

class YOLOv8Model:
    def __init__(self):
        # Modelinizi yükleyin
        self.model = YOLO('/home/seher/Desktop/Tubitak/tubitak_ml/tubitak_ml_with_yolov8/train4/weights/best.pt')  # Model dosyanızın yolunu girin

    def predict(self, image):
        # Model ile tahmin yapın
        resized_image = cv2.resize(image, (640, 640))  # YOLOv8 için genellikle 640x640 boyutunda olmalıdır
        results = self.model(resized_image)
        return results

    def get_classification(self, results):
        # Model sonuçlarını işleyin ve sınıflandırmayı döndürün
        if results:
            # 'results' nesnesinden tahminler alın
            for result in results:
                if result.boxes is not None:
                    # Her bir kutu için
                    for box in result.boxes:
                        # Kutu koordinatlarını, sınıf ID'sini ve olasılığı alın
                        class_id = int(box.cls[0])
                        confidence = box.conf[0]
                        # Sınıf adını ve olasılığı döndürün
                        classification = result.names[class_id]
                        return classification
        return 'Unknown'

# Örnek kullanım
if __name__ == '__main__':
    model = YOLOv8Model()
    # Örnek bir görüntü yükleme
    image_path = '/home/seher/Desktop/Tubitak/tubitak_ml/tubitak_ml_with_yolov8/deneme_gorselleri/kusurrlu.jpeg'  # Test etmek istediğiniz bir görselin yolu
    image = cv2.imread(image_path)
    
    results = model.predict(image)
    classification = model.get_classification(results)
    
    print(f'Classified as: {classification}')

