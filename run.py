import cv2
import numpy as np
import streamlit as st
from ultralytics import YOLO

model = YOLO('trash_best.pt')

st.set_page_config(layout='wide')

def main():
    st.markdown("<style>body {background-color: white;}</style>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>Litter Detection</h1>", unsafe_allow_html=True)

    # col1, col2 = st.columns([1, 1]) 

    # with col2:
    cap = cv2.VideoCapture(0)
    frame_container = st.empty()
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            st.error("Failed to capture image.")
            continue

        results = model(frame)
        annotated_frame = results[0].plot()
        annotated_frame = cv2.resize(annotated_frame, (720, 480))

        frame_container.image(annotated_frame, channels="BGR", use_column_width=(720,600))

    cap.release()    

if __name__ == "__main__":
    main()
