import cv2
import time
from hand_tracking import HandTracker
import gestures

# Landmark IDs
THUMB_TIP = 4
INDEX_TIP = 8

# Init tracker
tracker = HandTracker()
last_frame_time = 0

while True:
    img, results = tracker.get_frame()
    if img is None:
        continue

    # FPS display
    this_frame_time = time.time()
    fps = 1 / (this_frame_time - last_frame_time) if last_frame_time else 0
    last_frame_time = this_frame_time
    cv2.putText(img, f"FPS: {int(fps)}", (20, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Process detected hands
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            tracker.draw_hand(img, hand_landmarks)

            # Call different gestures
            gestures.gesture_volume(tracker, img, hand_landmarks, THUMB_TIP, INDEX_TIP)
            gestures.gesture_zoom(tracker, img, hand_landmarks, THUMB_TIP, INDEX_TIP)
            gestures.gesture_draw(tracker, img, hand_landmarks, INDEX_TIP)

    cv2.imshow("Gesture Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

tracker.release()
