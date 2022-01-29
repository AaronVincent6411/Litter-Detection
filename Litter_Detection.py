import cv2
import imutils
import numpy as np
import os

path = 'Images0'
images = []
Names = []
List = os.listdir(path)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
color = (250,0,250)
path1 = 'haarcascade/haarcascade_frontalface_default.xml'


FileName = 'test.names'
with open(FileName, 'rt') as f:
    Names = f.read().rstrip('\n').split('\n')

net = cv2.dnn_DetectionModel('frozen_inference_graph.pb','ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt')
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def empty(a):
    pass

while True:
    success, img1 = cap.read()
    imgGray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    img1 = imutils.resize(img1, height=600)

    classID, conf, box = net.detect(img1, confThreshold=0.6)
    print(classID, box)


    def empty(a):
        pass

    cascade = cv2.CascadeClassifier(path1)
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    scaleValue = 1 + (cv2.getTrackbarPos("Scale", "Result") / 1000)
    neig = cv2.getTrackbarPos("Neig", "Result")
    objects = cascade.detectMultiScale(gray, scaleValue, neig)
    for (x, y, w, h) in objects:
       area = w * h
       minArea = cv2.getTrackbarPos("Min Area", "Result")
       if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
            cv2.putText(img, 'Litter', (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            roi_color = img[y:y + h, x:x + w]

    for classIDs, confidence, boxx in zip(classID.flatten(), conf.flatten(), box):
        cv2.rectangle(img1, boxx, color=(0, 0, 255), thickness=2)
        cv2.putText(img1, Names[classIDs - 1].upper(), (boxx[0] + 10, boxx[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1,
                    (255, 0, 0), 2)

    cv2.imshow("Result", img1)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

'''
for cl in List:
        img = cv2.imread(f'{path}/{cl}')
        images.append(img)
        Names.append(os.path.splitext(cl)[0])
        img = imutils.resize(img, height=600)
        cv2.imshow("Result", img)
'''

