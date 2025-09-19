import cv2
import mediapipe as mp
import numpy as np

class HandTracker:
    def __init__(self, max_hands=2, detection_confidence=0.7, tracking_confidence=0.7):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=max_hands,
                                         min_detection_confidence=detection_confidence,
                                         min_tracking_confidence=tracking_confidence)
        self.mp_draw = mp.solutions.drawing_utils
        self.cap = cv2.VideoCapture(0)

    def get_frame(self):
        success, img = self.cap.read()
        if not success:
            return None, None
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        return img, results

    def draw_hand(self, img, hand_landmarks):
        self.mp_draw.draw_landmarks(img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

    def get_position(self, img, hand_landmarks, landmark_id):
        """Return (x, y) position of a landmark in pixels"""
        h, w, _ = img.shape
        lm = hand_landmarks.landmark[landmark_id]
        return int(lm.x * w), int(lm.y * h)

    def get_distance(self, img, hand_landmarks, id1, id2):
        """Euclidean distance between two landmarks"""
        x1, y1 = self.get_position(img, hand_landmarks, id1)
        x2, y2 = self.get_position(img, hand_landmarks, id2)
        distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance, (x1, y1), (x2, y2)

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
