import cv2
import time
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640) # Genişlik
cap.set(4, 480) # Yükseklik
used_codes = []

camera = True
while camera == True:
    success, frame = cap.read()

    for code in decode(frame):
        if code.data.decode('utf-8') not in used_codes:
            print("Tarama yapabilirsiniz.")
            print(code.data.decode('utf-8'))
            used_codes.append(code.data.decode('utf-8'))
            time.sleep(5)
        elif code.data.decode('utf-8') in used_codes:
            print("Bu barkod daha önce taranmıştır.")
            time.sleep(5)
        else:
            pass
    
    cv2.imshow("Barkod Okuyucu", frame)
    cv2.waitKey(1)
