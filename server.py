from flask import Flask, send_file
import os
import random
from summon import summon_video
from qr import get_qr_code

app = Flask(__name__)

@app.route('/')
def index():
    # Serve your home.html as the main page
    return send_file('home.html')

@app.route('/summon')
def summon():
    # Call your summon logic
    video = summon_video()
    print(f"Serving video: {video}")
    return send_file(f'vid/{video}')

@app.route('/qr')
def qr():
    # Call your QR logic
    qr_image = get_qr_code()
    print(f"Serving QR image: {qr_image}")
    return send_file(f'qr/{qr_image}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
