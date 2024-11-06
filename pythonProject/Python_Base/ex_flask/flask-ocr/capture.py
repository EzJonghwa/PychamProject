

from flask import Flask,request,jsonify
from PIL import Image
from io import BytesIO
import base64
import easyocr
import numpy as np

app = Flask(__name__)
reader = easyocr.Reader(['ko','en'])
@app.route("/upload", methods=['POST'])
def upload_image():
    data = request.json['image']
    image_data = base64.b64decode(data.split(",")[1])
    image = Image.open(BytesIO(image_data)).convert("RGB")
    image_np = np.array(image)
    result =reader.readtext(image_np,detail=0)
    return jsonify({'result':' '.join(result)})



if __name__ == '__main__':
    app.run(debug=True, port=5000)


