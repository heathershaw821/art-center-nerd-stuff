#!/usr/bin/env python3

from flask import Flask, Response
from picamera2 import Picamera2
import cv2

app = Flask(__name__)

# Initialize camera
picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"size": (320, 240), "format": "RGB888"}))
picam2.set_controls({"FrameDurationLimits": (100000, 100000)})  # 10 FPS
picam2.start()

def generate_frames():
    while True:
        frame = picam2.capture_array()
        # flip the frame due to the camera being mounted upside down
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

        # Add AI processing here
        # frame = process_with_ai(frame)

        # Encode frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return '''
    <html>
    <head><title>ROBOT Stream</title></head>
    <body><center>
    <h1>Live MJPEG ROBOT Stream</h1>
    <img src="/video_feed" width="640" height="480">
    </center></body>
    </html>
    '''

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=True)