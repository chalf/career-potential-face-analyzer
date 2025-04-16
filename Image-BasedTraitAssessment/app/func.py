import face_recognition
import numpy as np
import cv2


# file: from request.files['']
def detect_faces_location(file):
    img_np = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(img_np, cv2.IMREAD_COLOR)

    # Convert to RGB for face_recognition
    rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_img)

    result = {
        'num_faces': len(face_locations),
        'faces': [{'top': t, 'right': r, 'bottom': b, 'left': l}
                  for (t, r, b, l) in face_locations]
    }

    return result
