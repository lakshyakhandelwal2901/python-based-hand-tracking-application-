# Hand Tracking Gesture Control  

A real-time hand-tracking project built using **OpenCV**, **MediaPipe**, and **Python**. This system uses your webcam to detect hand landmarks and perform actions like:  

- Volume Control (thumb–index distance)  
- Zoom Simulation (digital zoom effect via pinch gesture)  
- Drawing Mode (index finger tracking)  
- Can be extended with more gestures  

---

## Features
- Real-time hand landmark detection using **MediaPipe** (21 points on each hand).  
- Modular design with separate files:  
  - `main.py` → Entry point for the app  
  - `hand_tracking.py` → Handles camera & landmark detection  
  - `gestures.py` → Defines custom gestures (volume, zoom, drawing, etc.)  
- Easy to extend: Add new gestures with just a function!  
- Cross-platform (Windows/Linux/Mac) — OS-specific volume control included.  

---

## Project Structure
```
📦 hand-tracking-gesture-control
├── main.py            # Main script (runs the system)
├── hand_tracking.py   # HandTracker class (camera + mediapipe processing)
├── gestures.py        # Gesture functions (volume, zoom, draw, etc.)
├── requirements.txt   # Python dependencies
└── README.txt         # Documentation (this file)
```

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/hand-tracking-gesture-control.git
cd hand-tracking-gesture-control
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the project:
```bash
python main.py
```

---

## Requirements
Your `requirements.txt` should contain:
```
opencv-python
mediapipe
numpy
pycaw   # (for Windows volume control)
```

---

## Landmark IDs Reference

MediaPipe uses **21 hand landmarks**:  

| ID  | Landmark       | Description |
|-----|----------------|-------------|
| 0   | Wrist          | Base of palm |
| 1-4 | Thumb joints   | CMC → MCP → IP → Tip |
| 5-8 | Index finger   | MCP → PIP → DIP → Tip |
| 9-12| Middle finger  | MCP → PIP → DIP → Tip |
| 13-16 | Ring finger  | MCP → PIP → DIP → Tip |
| 17-20 | Pinky finger | MCP → PIP → DIP → Tip |

<img width="1455" height="1977" alt="hand_landmarks_diagram" src="https://github.com/user-attachments/assets/359f6c7f-81f4-420b-a9dc-041eeb92522a" />


📌 Example:  
- `4` → Thumb Tip  
- `8` → Index Tip  
- These two are used for pinch gestures (zoom/volume control).

---

## How It Works
1. OpenCV captures webcam frames.  
2. MediaPipe processes frames to detect **21 landmarks** per hand.  
3. Gestures are recognized by measuring distances between key landmarks.  
4. Actions are triggered:
   - Volume Control: Distance between thumb tip (`4`) and index tip (`8`).  
   - Zoom: Pinch distance mapped to digital zoom effect.  
   - Draw: Tracks index tip (`8`) on the canvas.  

---

## Demo (Screenshots / GIFs)
👉 Add screenshots or a GIF showing the project running here.  

---

## Future Improvements
- Multi-hand gesture support  
- Gesture recognition with ML model (custom gestures)  
- System-level integration (brightness, media control, etc.)  
- Export as a desktop app with **PyInstaller**  

---

## Contributing
Feel free to fork this project, open issues, and submit pull requests.  

---

## License
This project is licensed under the MIT License — free to use and modify.  
