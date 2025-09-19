import cv2
import platform
import numpy as np

# ---------- Cross-platform Volume Control ----------
if platform.system() == "Darwin":  # macOS
    from subprocess import call
    def set_volume(vol):
        call(["osascript", "-e", f"set volume output volume {int(vol)}"])

elif platform.system() == "Windows":  # Windows
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    from comtypes import CLSCTX_ALL
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_obj = interface.QueryInterface(IAudioEndpointVolume)
    def set_volume(vol):
        volume_obj.SetMasterVolumeLevelScalar(vol / 100.0, None)

else:  # Linux (placeholder)
    def set_volume(vol):
        print(f"[DEBUG] Would set volume to {vol}%")

# ---------- Gesture Functions ----------
def gesture_volume(tracker, img, hand_landmarks, thumb_id=4, index_id=8):
    """Control volume using distance between thumb & index finger"""
    dist, p1, p2 = tracker.get_distance(img, hand_landmarks, thumb_id, index_id)

    # Normalize distance into volume (0–100)
    vol = np.clip(np.interp(dist, [30, 200], [0, 100]), 0, 100)
    set_volume(vol)

    # Visual Feedback
    cv2.line(img, p1, p2, (255, 0, 255), 2)
    cv2.putText(img, f"Vol: {int(vol)}%", (50, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

def gesture_zoom(tracker, img, hand_landmarks, thumb_id=4, index_id=8):
    """Example: Use thumb-index distance to zoom"""
    dist, p1, p2 = tracker.get_distance(img, hand_landmarks, thumb_id, index_id)
    zoom = np.clip(np.interp(dist, [30, 200], [1.0, 3.0]), 1.0, 3.0)

    # Just draw a circle to show zoom level
    cv2.circle(img, (p1[0], p1[1]), int(20 * zoom), (0, 255, 255), 2)
    cv2.putText(img, f"Zoom x{zoom:.1f}", (50, 200),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

def gesture_draw(tracker, img, hand_landmarks, index_id=8):
    """Draw a trail with index finger tip"""
    x, y = tracker.get_position(img, hand_landmarks, index_id)
    cv2.circle(img, (x, y), 10, (0, 0, 255), cv2.FILLED)
