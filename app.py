# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow INFO/WARNING logs

# import streamlit as st
# import cv2
# from deepface import DeepFace
# import threading
# import time
# import contextlib
# from streamlit.runtime.scriptrunner import add_script_run_ctx

# # Use a thread-safe stop flag
# stop_signal = threading.Event()

# # Initialize session state variables
# if "frame" not in st.session_state:
#     st.session_state.frame = None
# if "emotion" not in st.session_state:
#     st.session_state.emotion = None

# def detect_emotion(frame):
#     try:
#         analysis = DeepFace.analyze(frame, actions=["emotion"], enforce_detection=False)
#         return analysis[0]['dominant_emotion']
#     except Exception as e:
#         print(f"Emotion detection error: {e}")
#         return None

# def camera_loop():
#     cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Force DirectShow backend for Windows

#     with contextlib.suppress(Exception):  # Prevent logging spam
#         while cap.isOpened() and not stop_signal.is_set():
#             ret, frame = cap.read()
#             if not ret:
#                 continue

#             # Convert BGR to RGB
#             rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#             # Run emotion detection
#             emotion = detect_emotion(rgb_frame)

#             # Update session state
#             try:
#                 st.session_state.frame = rgb_frame
#                 st.session_state.emotion = emotion
#             except Exception as e:
#                 pass  # Safe fallback if session state is out of context

#             time.sleep(0.5)

#     cap.release()

# def start_camera():
#     stop_signal.clear()
#     thread = threading.Thread(target=camera_loop, daemon=True)
#     add_script_run_ctx(thread)  # Proper Streamlit context to avoid warnings
#     thread.start()

# def stop_camera():
#     stop_signal.set()

# # Streamlit UI
# st.title("🎭 Real-time Emotion Detection")
# start_button = st.button("Start Camera")
# stop_button = st.button("Stop Camera")

# if start_button:
#     start_camera()

# if stop_button:
#     stop_camera()

# # Display video and emotion
# frame_placeholder = st.empty()
# emotion_placeholder = st.empty()

# while not stop_signal.is_set():
#     if st.session_state.frame is not None:
#         frame_placeholder.image(st.session_state.frame, channels="RGB", use_container_width=True)

#     if st.session_state.emotion:
#         emotion_placeholder.warning(f"😮 Detected Emotion: {st.session_state.emotion.upper()}")

#     time.sleep(0.1)



# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow INFO/WARNING logs

# import streamlit as st
# import cv2
# from deepface import DeepFace
# import threading
# import time
# import contextlib
# from streamlit.runtime.scriptrunner import add_script_run_ctx

# # Use a thread-safe stop flag
# stop_signal = threading.Event()

# # Initialize session state variables
# if "frame" not in st.session_state:
#     st.session_state.frame = None
# if "emotion" not in st.session_state:
#     st.session_state.emotion = None

# # Custom CSS for styling
# st.markdown("""
#     <style>
#     .emotion-box {
#         padding: 1rem;
#         border-radius: 15px;
#         background-color: #f0f2f6;
#         text-align: center;
#         margin-top: 10px;
#         font-size: 1.3rem;
#         font-weight: bold;
#         color: #333;
#     }
#     .header {
#         text-align: center;
#         font-size: 2rem;
#         color: #4A90E2;
#         font-weight: 700;
#         padding-bottom: 10px;
#     }
#     .subheader {
#         text-align: center;
#         color: #777;
#         padding-bottom: 20px;
#     }
#     .button-row button {
#         width: 48%;
#         font-size: 16px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Detect emotion from a frame
# def detect_emotion(frame):
#     try:
#         analysis = DeepFace.analyze(frame, actions=["emotion"], enforce_detection=False)
#         return analysis[0]['dominant_emotion']
#     except Exception as e:
#         print(f"Emotion detection error: {e}")
#         return None

# # Camera thread loop
# def camera_loop():
#     cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Force DirectShow on Windows

#     with contextlib.suppress(Exception):
#         while cap.isOpened() and not stop_signal.is_set():
#             ret, frame = cap.read()
#             if not ret:
#                 continue

#             rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             emotion = detect_emotion(rgb_frame)

#             try:
#                 st.session_state.frame = rgb_frame
#                 st.session_state.emotion = emotion
#             except:
#                 pass

#             time.sleep(0.5)

#     cap.release()

# def start_camera():
#     stop_signal.clear()
#     thread = threading.Thread(target=camera_loop, daemon=True)
#     add_script_run_ctx(thread)
#     thread.start()

# def stop_camera():
#     stop_signal.set()

# # UI Header
# st.markdown("<div class='header'>🎭 Real-time Emotion Detection</div>", unsafe_allow_html=True)
# st.markdown("<div class='subheader'>Detect user emotions live via webcam using Deep Learning</div>", unsafe_allow_html=True)

# # Buttons
# col1, col2 = st.columns(2)
# with col1:
#     if st.button("▶️ Start Camera"):
#         start_camera()
# with col2:
#     if st.button("⏹️ Stop Camera"):
#         stop_camera()

# # Display
# frame_placeholder = st.empty()
# emotion_placeholder = st.empty()

# # Main loop
# while not stop_signal.is_set():
#     if st.session_state.frame is not None:
#         frame_placeholder.image(st.session_state.frame, channels="RGB", use_container_width=True)

#     emotion = st.session_state.get("emotion")
#     if emotion:
#         emotion = emotion.lower()
#         if emotion == "sad":
#             color = "#ff6b6b"
#             msg = "😢 Crying Detected"
#         elif emotion == "angry":
#             color = "#ff4b4b"
#             msg = "😠 Angry Detected"
#         elif emotion == "happy":
#             color = "#50fa7b"
#             msg = "😊 Happy Detected"
#         else:
#             color = "#ffe66d"
#             msg = f"🙂 Emotion: {emotion.upper()}"

#         emotion_placeholder.markdown(f"""
#             <div class='emotion-box' style="background-color:{color};color:white;">
#                 {msg}
#             </div>
#         """, unsafe_allow_html=True)

#     time.sleep(0.1)




import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow INFO/WARNING logs

import streamlit as st
import cv2
from deepface import DeepFace
import threading
import time
import contextlib
from streamlit.runtime.scriptrunner import add_script_run_ctx

# Thread-safe stop flag
stop_signal = threading.Event()

# Initialize session state
if "frame" not in st.session_state:
    st.session_state.frame = None
if "emotion" not in st.session_state:
    st.session_state.emotion = None

# Custom dark theme CSS
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #FFFFFF;
    }
    .stApp {
        background-color: #121212;
    }
    .emotion-box {
        padding: 1rem;
        border-radius: 12px;
        text-align: center;
        margin-top: 15px;
        font-size: 1.4rem;
        font-weight: 600;
        color: white;
    }
    .header {
        text-align: center;
        font-size: 2.2rem;
        color: #00ADB5;
        font-weight: 700;
        padding-bottom: 0.3rem;
    }
    .subheader {
        text-align: center;
        color: #b0b0b0;
        font-size: 1rem;
        padding-bottom: 2rem;
    }
    button[kind="secondary"] {
        background-color: #333333;
        color: #FFFFFF;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-size: 1rem;
        border: none;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Detect emotion from frame
def detect_emotion(frame):
    try:
        analysis = DeepFace.analyze(frame, actions=["emotion"], enforce_detection=False)
        return analysis[0]['dominant_emotion']
    except Exception as e:
        print(f"Emotion detection error: {e}")
        return None

# Camera thread loop
def camera_loop():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    with contextlib.suppress(Exception):
        while cap.isOpened() and not stop_signal.is_set():
            ret, frame = cap.read()
            if not ret:
                continue
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            emotion = detect_emotion(rgb_frame)
            try:
                st.session_state.frame = rgb_frame
                st.session_state.emotion = emotion
            except:
                pass
            time.sleep(0.5)
    cap.release()

# Camera controls
def start_camera():
    stop_signal.clear()
    thread = threading.Thread(target=camera_loop, daemon=True)
    add_script_run_ctx(thread)
    thread.start()

def stop_camera():
    stop_signal.set()

# Header
st.markdown("<div class='header'>🎭 Real-time Emotion Detection</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Powered by Deep Learning - Detect real-time emotions from your webcam feed.</div>", unsafe_allow_html=True)

# Control Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("▶️ Start Camera"):
        start_camera()
with col2:
    if st.button("⏹️ Stop Camera"):
        stop_camera()

# Placeholders
frame_placeholder = st.empty()
emotion_placeholder = st.empty()

# Main UI loop
while not stop_signal.is_set():
    if st.session_state.frame is not None:
        frame_placeholder.image(st.session_state.frame, channels="RGB", use_container_width=True)

    emotion = st.session_state.get("emotion")
    if emotion:
        emotion = emotion.lower()
        if emotion == "sad":
            color = "#e74c3c"
            msg = "😢 Crying Detected"
        elif emotion == "angry":
            color = "#c0392b"
            msg = "😠 Angry Detected"
        elif emotion == "happy":
            color = "#2ecc71"
            msg = "😊 Happy Detected"
        elif emotion == "surprise":
            color = "#f39c12"
            msg = "😲 Surprised Detected"
        else:
            color = "#3498db"
            msg = f"🙂 Emotion: {emotion.upper()}"

        emotion_placeholder.markdown(f"""
            <div class='emotion-box' style="background-color:{color};">
                {msg}
            </div>
        """, unsafe_allow_html=True)

    time.sleep(0.1)
