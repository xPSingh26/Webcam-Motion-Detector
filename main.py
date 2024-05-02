import cv2
import time

# Start webcam
video = cv2.VideoCapture(0)
time.sleep(1)
staticFrame = None

while True:
    # Capture frame and convert into gray blurred
    check, frame = video.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayFrameGau = cv2.GaussianBlur(grayFrame, (21, 21), 0)

    # save static frame for comparison
    if staticFrame is None:
        staticFrame = grayFrameGau

    # save the difference between first frame and current
    deltaFrame = cv2.absdiff(staticFrame, grayFrameGau)
    threshFrame = cv2.threshold(deltaFrame, 70, 255, cv2.THRESH_BINARY)[1]
    dilFrame = cv2.dilate(threshFrame, None,  iterations=2)

    # draw rectangle around the object detected
    contours, check = cv2.findContours(dilFrame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("My video", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
