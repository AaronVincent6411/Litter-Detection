import cv2

path = 'haarcascade_frontalface_default.xml'
color= (255,0,255)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


def empty(a):
    pass
cascade = cv2.CascadeClassifier(path)

while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    scaleValue =1 + (cv2.getTrackbarPos("Scale", "Result") /1000)
    neig=cv2.getTrackbarPos("Neig", "Result")
    objects = cascade.detectMultiScale(gray,scaleValue, neig)
    for (x,y,w,h) in objects:
        area = w*h
        minArea = cv2.getTrackbarPos("Min Area", "Result")
        if area >minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
            cv2.putText(img,'Litter',(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            roi_color = img[y:y+h, x:x+w]

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imshow("Result", img)
        cv2.waitKey(1)
