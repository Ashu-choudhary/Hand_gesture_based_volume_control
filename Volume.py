import cv2
import mediapipe as mp
import pyautogui

x1 = y1 = x2 = y2 = 0

''' 
webcam is an object for Video Capture function form CV2 library And passing an integer parameter as 0,1,2,
...because how many number of webcam you have 0 for one, 1 for two and like that. 
'''
webcam = cv2.VideoCapture(0)

'''In my_hands variable can capture hands movements'''

my_hands = mp.solutions.hands.Hands()

'''And the drawing_utils can capture the points in our hands in all figures and thumb'''

drawing_utils = mp.solutions.drawing_utils
while True:

    '''webcam.read() function return 2 statement first is status of webcam and second is the image OR frame captured '''

    _, image = webcam.read()
    image = cv2.flip(image, 1)
    frame_height, frame_width, _ = image.shape

    '''The rgb_image object is convert the captured image from BGR to RGB'''

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    '''In this output object we can process our hands with the help of my_hands variable and RGB_Converted image'''

    output = my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if id == 8:
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                    x1 = x
                    y1 = y
                if id == 4:
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 255), thickness=3)
                    x2 = x
                    y2 = y

        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 // 4
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)
        if dist > 20:
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")

    '''cv2.imshow have to show the captured image in the read() function above'''

    cv2.imshow("Hand Based volume Control", image)

    '''cv2.waitkey function is used to wait for next turn of while loop. I passed 10 milliseconds'''

    key = cv2.waitKey(10)

    ''' '27' is the 'Esc' key, if user press 'Esc' key the capture video function was destroyed'''

    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()
