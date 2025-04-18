from app import app
from flask import request, jsonify
import math
import face_recognition
import numpy as np
import cv2
import mediapipe as mp
from analyze_faces import analyze_personality

# Mediapipe face mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1)


@app.route('/analyze-faces/', methods=['POST'])
def detect_faces():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    img_np = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(img_np, cv2.IMREAD_COLOR)

    h, w, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_image)

    if not results.multi_face_landmarks:
        return jsonify({'error': 'No face detected'}), 404

    # Lấy các điểm landmark (468 điểm)
    landmarks = []
    for lm in results.multi_face_landmarks[0].landmark:
        landmarks.append({
            'x': lm.x,
            'y': lm.y,
            'z': lm.z
        })

    data = analyze_personality(landmarks, w, h)

    return jsonify(data)


@app.route('/', methods=['GET'])
def index():
    return '<h1>Welcome</h1>'


if __name__ == '__main__':
    app.run(debug=True)
