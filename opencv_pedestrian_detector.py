#Early Remote Syslog detection System using OpenCV
#Used for person detection and intrusion detection
#Use the Remote Syslog python module to log a event

import cv2
import imutils

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def live_detection(capture_device):
    cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)
    cap = cv2.VideoCapture(capture_device)

    while cap.isOpened():
        sec = 0
        while sec != 2:
            ret, image = cap.read()
            sec += 1

        if ret:
            image = imutils.resize(image, width=min(400, image.shape[1]))
            (regions, _) = hog.detectMultiScale(image, winStride=(5,5,), padding=(4,4),scale=1.4)
            for (x,y,w,h) in regions:
                cv2.rectangle(image,(x,y), (x+w, y+h), (0,255,255),2)

            cv2.imshow("Webcam", image)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

#Use function(capture device) / usually 0 or 1
#live_detection(1)
