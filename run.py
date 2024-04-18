from flask import Flask, Response
import cv2
from ultralytics import YOLO

app = Flask(__name__)

model = YOLO('trash_best.pt')

def gen():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, frame = cap.read()

        if success:
            results = model(frame)

            annotated_frame = results[0].plot()

            image_np = cv2.resize(annotated_frame,(840,660))
            # cv2.imshow("Litter Detection", image_np)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            ret, buffer = cv2.imencode('.jpg', image_np)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        else:
            break

    cap.release()
    cv2.destroyAllWindows()

@app.route('/')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)

# import cv2
# from ultralytics import YOLO

# model = YOLO('trash_best.pt')

# cap = cv2.VideoCapture(0)

# while cap.isOpened():
#     success, frame = cap.read()

#     if success:
#         results = model(frame)

#         annotated_frame = results[0].plot()

#         image_np = cv2.resize(annotated_frame,(840,660))
#         cv2.imshow("Litter Detection", image_np)

#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break

# cap.release()
# cv2.destroyAllWindows()