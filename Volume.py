import cv2
import mediapipe as mp
import pyautogui

x1 = y1 = x2 = y2 = 0

webcam = cv2.VideoCapture(0) #webcam is an object for Video Capture function form CV2 library And passing an integer parameter as 0,1,2,...because how many number of webcam you have 0 for one, 1 for two and like that.
my_hands = mp.solutions.hands.Hands() #In my_hands variable can capture hands movements
drawing_utils = mp.solutions.drawing_utils #And the drawing_utils can capture the points in our hands in all figures and thumb
while True:

    _, image = webcam.read() #webcam.read() function return 2 statement first is status of webcam and second is the image OR frame captured
    image = cv2.flip(image, 1) #This flip function
    frame_height, frame_width, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #The rgb_image object is convert the captured image from BGR to RGB
    output = my_hands.process(rgb_image) #In this output object we can process our hands with the help of my_hands variable and RGB_Converted image
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand)# It draws points in our hands
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if id == 8:
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 0), thickness=5) # It can create a circle in my index finger of black color
                    x1 = x
                    y1 = y
                if id == 4:
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 255), thickness=5)# It can create a circle in my thumb of red color
                    x2 = x
                    y2 = y

        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 // 4 #Calculate the distance between our finger and the thumb
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)# Make a line between our finger and the thumb
        if dist > 20:
            pyautogui.press("volumeup")#It can increase the volume, if the calculated distance is greater then 20
        else:
            pyautogui.press("volumedown")#It can Decrease the volume, if the calculated distance is smaller then 20

    cv2.imshow("Hand Based volume Control", image) #cv2.imshow have to show the captured image in the read() function above
    key = cv2.waitKey(10) #cv2.waitkey function is used to wait for next turn of while loop. I passed 10 milliseconds

    if key == 27:# '27' is the 'Esc' key, if user press 'Esc' key the programs is closed
        break
webcam.release()#It can release the webcam
cv2.destroyAllWindows()#This is to close all the running windows
