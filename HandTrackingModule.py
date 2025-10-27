import cv2
import mediapipe as mp 
import time
import numpy as np
#init camera on camera 0 (inbuilt)

class handDetector():
    def __init__(self, mode=False, max_hands, detection_con=0.5, track_con=0.5):
        self.mode = mode
        seld.max_hands = max_hands
        detection_con = detection_con
        track_con = track_con

       self.mp_hands = mp.solutions.hands
       self.hands = self.mpHands.Hands(self.mode, self.max_hands, self.detection_con, self.track_con)
       self.mpDraw = mp.solutions.drawing_utils
       
pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #convert to rgb
    results = hands.process(imgRGB) #get landmarks from image
    if results.multi_hand_landmarks: 
        for handLms in results.multi_hand_landmarks: #get landmarks of each hand
            for id, lm in enumerate(handLms.landmark):  
                h, w, c = img.shape # get shape of image (height, width, color channel)
                cx, cy = int(lm.x*w), int(lm.y*h) #get x and y of landmark in pixels
                print(id, cx, cy)
                #draws on the landmark 0
                if id == 0: 
                    cv2.circle(img, (cx, cy), 28, (255,0,255), cv2.FILLED) #draw circle at landmark 0 (img, (x, y, radius_px, (R,G,B), type)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) #draw skeleton
    # count fps
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    # draw fps on screen 
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,(255,0,255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)


if __name__ == "__main__"
    cap = cv2.VideoCapture(0)
    pTime = 0
    cTime = 0

    while True:
        success, img = cap.read()
    # count fps
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    # draw fps on screen 
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,(255,0,255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)


