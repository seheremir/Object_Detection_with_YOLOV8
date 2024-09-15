from ultralytics import YOLO

# YOLOv8 modelini yükle
model = YOLO('yolov8n.pt')  # 'n' küçük model, daha hızlıdır

# Modeli eğit
model.train(data='tubitak_ml_with_yolov8/patates.yaml', epochs=50, imgsz=640)

# Eğitim sonrası modeli değerlendirme
metrics = model.val()

# Sonuçları görüntüle
print(metrics)
