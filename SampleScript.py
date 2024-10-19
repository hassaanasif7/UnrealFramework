from PIL import Image
from matplotlib import gridspec
import matplotlib.pylab as plt
import numpy as np
import cv2
import json
from unrealcv import client
from unrealcv.util import read_npy
import socket

PORT, HOST_IP = 8080, '127.0.0.1'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST_IP, PORT))
s.listen()
print("starting to listen")
conn, addr = s.accept()
print("Connected")

def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

@run_once
def Move(x,y):
    global conn
    if conn:
        conn.sendall("Move".encode())
        data_string = json.dumps({"x":x,"y":y})
        conn.sendall(data_string.encode())

@run_once
def SaySomething(string):
    global conn
    if conn:
        conn.sendall("Say".encode())
        data_string = json.dumps({"Hiiii":string})
        conn.sendall(data_string.encode())




def CamStream():
    client.connect()
    if not client.isconnected():
        print('UnrealCV server is not running')
        exit()
    while True:
        res = client.request('vget /camera/1/lit png')
        res = np.frombuffer(res, np.uint8)
        content_image = cv2.imdecode(res, -1)

        global conn
        if conn:
            data = conn.recv(16384)
            print(data)
        else:
            s.listen()
            conn, addr = s.accept()
            print("starting to listen")
            print("Connected")
            data = conn.recv(16384)
            print(data)
        cv2.putText(content_image, "Robot Position {}".format(data), (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255)
        cv2.imshow("Render", content_image)
        cv2.waitKey(1)


        """res = client.request('vget /camera/2/depth npy')
        depth = read_npy(res)
        print(depth)
        depth = depth * 0.0005
        cv2.imshow("Render", depth)
        cv2.waitKey(1)"""

CamStream()



