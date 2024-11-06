#pip install googletrans==4.0.0-rc1
from googletrans import Translator
from flask import Flask,request,jsonify
from PIL import Image
import io
import easyocr
import numpy as np
from flask_cors import CORS

tran = Translator()
app =Flask(__name__)
CORS(app)
reader = easyocr.Reader(['en','ko'])
@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'error' : 'no image file provided'}), 400
    img_file = request.files['image'].read()
    img = Image.open(io.BytesIO(img_file))
    img_np = np.array(img)
    results = reader.readtext(img_np, detail=0)

    if results:
        text =' '.join(results)
        result = tran.translate(text, src='en', dest='ko')
        print (result.text)
        trans = result.text
    else:
        trans="번역 가능 텍스트 업음"
    return jsonify({'translation':trans})

if __name__ =='__main__':
    app.run(port=5000)
