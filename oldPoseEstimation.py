import cv2
import mediapipe as mp
import numpy as np

# Initialise Pose Estimator
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(model_complexity=0)

# Create a 2D 
videoPoseData = np.empty([0, 12])

cap = cv2.VideoCapture(0)
while cap.isOpened():
    # read frame
    _, frame = cap.read()
    try: 
        # process the frame for pose detection
        results = pose.process(frame)
        LEFT_SHOULDER = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        RIGHT_SHOULDER = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        LEFT_ELBOW = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
        RIGHT_ELBOW = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW]
        LEFT_WRIST = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
        RIGHT_WRIST = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]

        LEFT_HIP = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
        RIGHT_HIP = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]
        LEFT_KNEE = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]
        RIGHT_KNEE = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE]
        LEFT_ANKLE = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE]
        RIGHT_ANKLE = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]

        videoPoseData = np.append(videoPoseData, [[LEFT_SHOULDER, RIGHT_SHOULDER, LEFT_ELBOW, RIGHT_ELBOW, LEFT_WRIST, RIGHT_WRIST, LEFT_HIP, RIGHT_HIP, LEFT_KNEE, RIGHT_KNEE, LEFT_ANKLE, RIGHT_ANKLE]], axis=0)
        
        # draw skeleton on the frame
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        # display the frame
        cv2.imshow('Output', frame)

    except Exception as e:
        print(e)
        break
    if cv2.waitKey(1) == ord('q'):
          break
          
cap.release()
cv2.destroyAllWindows()