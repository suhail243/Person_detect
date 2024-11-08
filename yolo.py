from ultralytics import YOLO
import cv2
model=YOLO("yolov8n.pt")

image_path = r"C:\Users\Suhai\Downloads\my.jpg"


img = cv2.imread(image_path)
result=model(img,show=True)
