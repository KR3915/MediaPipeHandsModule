import cv2
import mediapipe as mp 
import time
import numpy as np
#init camera on camera 0 (inbuilt)

class handDetector():
    def __init__(self, mode=False, max_hands=2, detection_con=0.5, track_con=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_con = detection_con
        self.track_con = track_con

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):
         if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:        
               imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #convert to rgb
               self.results = self.hands.process(imgRGB) #get landmarks from image
               self.mpDraw.draw_landmarks(img, handLms, self.mp_hands.HAND_CONNECTIONS)
               return img
         else:
            return 0

    def find_position(self, img, hand_no=0, draw=True):

        lm_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]
            for handLms in self.results.multi_hand_landmarks: #get landmarks of each hand
                for id, lm in enumerate(handLms.landmark):  
                    h, w, c = img.shape # get shape of image (height, width, color channel)
                    cx, cy = int(lm.x*w), int(lm.y*h) #get x and y of landmark in pixels
                    lm_list.append[id, cx, cy]
                    #draws on the landmark 0
                    if draw:
                        cv2.circle(img, (cx, cy), 28, (255,0,255), cv2.FILLED) #draw circle at landmark 0 (img, (x, y, radius_px, (R,G,B), type)

                self.mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) 
        return lm_list 

    # cTime = time.time()
    # fps = 1/(cTime-pTime)
    # pTime = cTime
    # # draw fps on screen 
    # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,(255,0,255), 3)
    #
    # cv2.imshow("Image", img)
    # cv2.waitKey(1)

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    cTime = 0
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.find_hands(img)    # count fps
        lm_list = find_position(img)
        print(lm_list[1])
        # cTime = time.time()
        # fps = 1/(cTime-pTime)
        # pTime = cTime
        # # draw fps on screen 
        # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,(255,0,255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

if __name__ == "__main__":
    main()
