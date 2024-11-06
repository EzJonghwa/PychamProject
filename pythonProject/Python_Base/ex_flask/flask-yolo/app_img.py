from flask import Flask , render_template, request, jsonify
from ultralytics import YOLO
import os
from werkzeug.utils import secure_filename
import cv2

app = Flask(__name__)
model = YOLO('yolov8n.pt')
UPLOAD_DIR = 'static/uploads'

@app.route("/")
def index():
    return render_template('yolo_index.html')

@app.route("/analyze", methods=["POST"])
def analyze():
    if 'file' not in request.files:
        return jsonify({'error' : 'no file'})
    file = request.files['file']
    if file :
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_DIR, filename)
        file.save(filepath)
    results = model(filepath)

    # 분석 파일 저장
    result_img = os.path.join(UPLOAD_DIR, 'result_'+ filename)
    cv2.imwrite(result_img,results[0].plot(show=False))
    return jsonify({'original_image':filepath, 'result_image': result_img})
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")