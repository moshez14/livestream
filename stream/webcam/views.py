from django.shortcuts import render
from django.http import StreamingHttpResponse

import cv2
# Create your views here.
def index(request):
    return render(request,'index.html')

def stream1():
    cap = cv2.VideoCapture('rtmp://34.243.140.144:1935/live_hls/drone1')
    while True:
        ret, frame = cap.read()
        if not ret:
            print("EROOR: faild to capture image")
            break
        image_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')

def stream2():
    #cap2 = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture('rtmp://34.243.140.144:1935/live_hls/drone2')
    while True:
        ret, frame = cap2.read()
        if not ret:
            print("EROOR: faild to capture image")
            break
        image_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')
def stream3():
    #cap2 = cv2.VideoCapture(0)
    cap3 = cv2.VideoCapture('rtmp://34.243.140.144:1935/live_hls/drone3')
    while True:
        ret, frame = cap3.read()
        if not ret:
            print("EROOR: faild to capture image")
            break
        image_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')

def camera():
    #cap2 = cv2.VideoCapture(0)
    cap4 = cv2.VideoCapture('rtmp://34.243.140.144:1935/live_hls/camera1')
    while True:
        ret, frame = cap4.read()
        if not ret:
            print("EROOR: faild to capture image")
            break
        image_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')
       
def video_feed1(request):
    return StreamingHttpResponse(stream1(), content_type='multipart/x-mixed-replace; boundary=frame')
def video_feed2(request):
    return StreamingHttpResponse(stream2(), content_type='multipart/x-mixed-replace; boundary=frame')
def video_feed3(request):
    return StreamingHttpResponse(stream3(), content_type='multipart/x-mixed-replace; boundary=frame')
def video_feed_camera(request):
    return StreamingHttpResponse(camera(), content_type='multipart/x-mixed-replace; boundary=frame')


