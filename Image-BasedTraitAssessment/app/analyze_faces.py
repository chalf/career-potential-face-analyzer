

def analyze_personality(landmarks, image_width, image_height):
    # Chuyển landmarks từ tỉ lệ → pixel
    points = [(lm['x'] * image_width, lm['y'] * image_height) for lm in landmarks]

    def distance(p1, p2):
        return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) ** 0.5

    # Tính các chỉ số
    face_width = distance(points[234], points[454])  # hai bên mặt (điểm gần tai)
    face_height = distance(points[10], points[152])  # trán → cằm

    eye_distance = distance(points[133], points[362])  # hai khóe mắt
    nose_length = distance(points[1], points[2]) + distance(points[2], points[98])  # trán → chóp mũi
    mouth_width = distance(points[78], points[308])  # khóe miệng
    chin_prominence = distance(points[152], points[199])  # cằm nhô ra bao nhiêu

    # Tính các tỷ lệ (Normalize)
    face_ratio = face_width / face_height if face_height else 1
    eye_ratio = eye_distance / face_width if face_width else 1
    mouth_ratio = mouth_width / face_width if face_width else 1
    nose_ratio = nose_length / face_height if face_height else 1
    chin_ratio = chin_prominence / face_height if face_height else 1

    data = rule_based_classification(face_ratio, eye_ratio, mouth_ratio, nose_ratio, chin_ratio)

    return {
        "face_ratio": round(face_ratio, 3),
        "eye_ratio": round(eye_ratio, 3),
        "mouth_ratio": round(mouth_ratio, 3),
        "nose_ratio": round(nose_ratio, 3),
        "chin_ratio": round(chin_ratio, 3),
        'summary': data['summary'],
        "personality": list(set(data['personality'])),
        "suggested_careers": list(set(data['careers']))
    }


def rule_based_classification(face_ratio, eye_ratio, mouth_ratio, nose_ratio, chin_ratio):
    # Rule-based classification (Gán tính cách theo rule đơn giản)
    personality = []
    careers = []

    # FACE RATIO
    if face_ratio < 0.80:
        personality += ["Sâu sắc", "Quan sát nội tâm"]
        careers += ["Nhà trị liệu", "Nhà văn", "Nhà nghiên cứu"]
    elif face_ratio < 0.90:
        personality += ["Trầm tính", "Sống lý trí"]
        careers += ["Chuyên gia dữ liệu", "Giảng viên", "Tư vấn viên"]
    elif face_ratio <= 1.00:
        personality += ["Cân bằng", "Dễ thích nghi", "Cởi mở"]
        careers += ["Chuyên viên nhân sự", "Quản lý", "Freelancer"]
    elif face_ratio <= 1.10:
        personality += ["Hòa đồng", "Tự tin", "Dễ kết nối"]
        careers += ["Content Creator", "MC", "Chuyên gia đào tạo"]
    else:
        personality += ["Nổi bật", "Lãnh đạo bẩm sinh", "Chủ động"]
        careers += ["CEO", "Influencer", "Nhà đầu tư", "Leader startup"]

    # EYE RATIO
    if eye_ratio < 0.25:
        personality += ["Khép kín", "Giữ khoảng cách"]
        careers += ["Nhà nghiên cứu", "Kỹ sư phần mềm", "Biên tập viên"]
    elif eye_ratio < 0.30:
        personality += ["Tập trung cao", "Tư duy phân tích"]
        careers += ["Data Analyst", "Chuyên gia bảo mật", "QA Tester"]
    elif eye_ratio < 0.35:
        personality += ["Linh hoạt", "Dễ tiếp thu"]
        careers += ["Giảng viên", "Tư vấn", "Project coordinator"]
    else:
        personality += ["Sáng tạo", "Trí tưởng tượng tốt", "Thẩm mỹ cao"]
        careers += ["Thiết kế UX/UI", "Nghệ sĩ thị giác", "Nhiếp ảnh", "Fashion stylist"]

    # MOUTH RATIO
    if mouth_ratio < 0.30:
        personality += ["Kín tiếng", "Ít nói", "Lắng nghe tốt"]
        careers += ["Chuyên viên pháp lý", "Lập trình viên", "Quản trị hệ thống"]
    elif mouth_ratio < 0.40:
        personality += ["Điềm đạm", "Thân thiện", "Kiên nhẫn"]
        careers += ["Tư vấn tâm lý", "Nhân sự", "Giáo viên"]
    elif mouth_ratio < 0.50:
        personality += ["Nhiệt huyết", "Tự tin", "Khả năng giao tiếp tốt"]
        careers += ["Chuyên viên sale", "Giảng viên", "Team Leader"]
    else:
        personality += ["Hoạt ngôn", "Ảnh hưởng cao", "Giao tiếp chủ động"]
        careers += ["Diễn giả", "Luật sư", "Chuyên gia đàm phán", "TikToker"]

    # NOSE RATIO
    if nose_ratio < 0.28:
        personality += ["Nhẹ nhàng", "Không thích kiểm soát", "Thích an toàn"]
        careers += ["Thủ thư", "Trợ lý cá nhân", "Y tá"]
    elif nose_ratio < 0.35:
        personality += ["Thực tế", "Thận trọng", "Kiểm soát cảm xúc tốt"]
        careers += ["Kế toán", "QA QC", "Tài chính"]
    elif nose_ratio < 0.40:
        personality += ["Tham vọng", "Có định hướng", "Tư duy kinh doanh"]
        careers += ["Marketing planner", "Chuyên viên chiến lược", "Founder"]
    else:
        personality += ["Lãnh đạo", "Quyết đoán", "Tư duy hệ thống"]
        careers += ["Product Owner", "Manager", "Đầu tư mạo hiểm"]

    # CHIN RATIO
    if chin_ratio < 0.12:
        personality += ["Mềm mỏng", "Nhạy cảm", "Dễ bị chi phối"]
        careers += ["Chăm sóc khách hàng", "Thư ký", "Chuyên viên hỗ trợ"]
    elif chin_ratio < 0.17:
        personality += ["Nhẹ nhàng", "Biết lắng nghe", "Hài hòa"]
        careers += ["Chuyên viên tư vấn", "Tâm lý học", "Trị liệu viên"]
    elif chin_ratio < 0.21:
        personality += ["Kiên định", "Tự chủ", "Ổn định cảm xúc"]
        careers += ["Project Manager", "Nhà hoạch định", "Giảng viên"]
    else:
        personality += ["Cứng rắn", "Kiên cường", "Bản lĩnh"]
        careers += ["Lãnh đạo nhóm", "Founder", "Chuyên gia đàm phán"]

    # ---- Tạo summary ----
    top_traits = personality[:3]
    top_careers = careers[:3]

    # Viết thành một đoạn văn ngắn
    summary = (
        f"Dựa vào tỉ lệ khuôn mặt, bạn có những tính cách nổi bật như "
        f"{', '.join(top_traits[:-1])} và {top_traits[-1]}. "
        f"Những nghề nghiệp phù hợp với phong thái này gồm {', '.join(top_careers[:-1])} và {top_careers[-1]}. "
        "Hãy cân nhắc thử sức ở các lĩnh vực này!"
    )

    return {
        'personality': personality,
        'careers': careers,
        'summary': summary,
    }




