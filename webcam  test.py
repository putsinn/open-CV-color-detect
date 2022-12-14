import cv2
import numpy as np
cap = cv2.VideoCapture (0)
while True:
        ret, frame = cap.read()
        frame = cv2.flip (frame, 0)
        cv2.imshow ("Camera", frame)
        key = cv2.waitKey (0)
        if key == 27:
            break

cap. release ()
cv2.destroyAllWindows()
