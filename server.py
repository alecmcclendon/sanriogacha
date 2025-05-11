from flask import Flask, send_file
import os
import random

app = Flask(__name__)

# Serve the homepage
@app.route('/')
def index():
    return send_file('home.html')

# Serve the summon route
@app.route('/summon')
def summon():
    videos = os.listdir('vid')
    chosen_video = random.choice(videos)
    print(f"Serving video: {chosen_video}")
    return send_file(f'vid/{chosen_video}')

# Serve the QR route
@app.route('/qr')
def qr():
    qr_images = os.listdir('qr')
    chosen_qr = random.choice(qr_images)
    print(f"Serving QR image: {chosen_qr}")
    return send_file(f'qr/{chosen_qr}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

