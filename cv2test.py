import cv2

# -------------------------------------------------------
# Short program to test that open cv live video is working
# --------------------------------------------------------
cap = cv2.VideoCapture(0)
while cap.isOpened():
    # read frame
    _, frame = cap.read()
    # display frame
    cv2.imshow('Output', frame)
    # Quit when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
          break
cap.release()
cv2.destroyAllWindows()