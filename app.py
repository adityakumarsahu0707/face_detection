from flask import Flask, render_template, request, Response
import cv2

app=Flask(__name__)
cap=cv2.VideoCapture(0)

def gen_frames():  
    while True:
        ret, photo = cap.read()  # read the camera frame
        if not ret:
            break
        else:
            ret1, buffer = cv2.imencode('.jpg', photo)
            photo = buffer.tobytes()
            yield (b'--frame' b'Content-Type: image/jpg\r\n\r\n' + photo)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def live_video():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace); boundary=frame')

if __name__ == '__main__':
    app.run()