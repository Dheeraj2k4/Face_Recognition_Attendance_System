
# 👨‍🏫 Face Recognition Attendance System

> ⚡ **Fast, accurate, and smart** attendance system using **InsightFace**, **Streamlit**, and **Excel automation** — built for seamless classroom or workplace use.

---

## 🚀 Overview

The **Face Recognition Attendance System** is a cutting-edge application that leverages **InsightFace** for facial verification and identification. Designed with simplicity and speed in mind, the app allows **teachers to log in**, automatically mark attendance from **live camera feed**, and download an **Excel sheet** — all from a clean and intuitive **Streamlit interface**.

---

## ✨ Features

✅ **Highly Accurate Face Recognition** using InsightFace
✅ **Streamlit UI** – clean, modern, and easy to use
✅ **Teacher Login System** with authentication
✅ **Attendance Marking** in real-time via webcam
✅ **Downloadable Excel Sheet** with attendance log
✅ **Filters** for date-wise or student-wise attendance view
✅ **Add/Delete Students** with one-click functionality
✅ **Fast Processing** — optimized for real-time response
✅ **Face Embedding Storage** for future comparisons
✅ **Responsive & Lightweight**

---

## 🧰 Tech Stack

| Tech             | Purpose                            |
| ---------------- | ---------------------------------- |
| **Python**       | Core backend logic                 |
| **Streamlit**    | Web-based UI                       |
| **InsightFace**  | Face detection & recognition model |
| **OpenCV**       | Webcam access and image processing |
| **Pandas**       | Excel sheet handling and filtering |
| **SQLite / CSV** | Student data & attendance logging  |
| **Excel Writer** | Auto-generate downloadable reports |

---

## 📸 How It Works

1. **Teacher logs in** with their credentials.
2. Student faces are captured live via webcam.
3. Faces are matched with stored embeddings using **InsightFace**.
4. Attendance is **automatically marked** for recognized faces.
5. Teacher can **download the Excel sheet** with timestamps, names, and filters.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/face-attendance-system.git
cd face-attendance-system
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ Make sure `insightface` and `opencv-python` are properly installed.

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Navigate to `http://localhost:8501` in your browser.

---

## 🧠 Core Modules

* `face_encoder.py` – Generates and stores facial embeddings
* `attendance_logic.py` – Compares embeddings and marks attendance
* `authenticator.py` – Handles teacher login
* `excel_handler.py` – Creates and filters Excel sheets
* `app.py` – Main Streamlit app

---

## 📂 Folder Structure

```
face-attendance-system/
├── app.py
├── face_encoder.py
├── attendance_logic.py
├── authenticator.py
├── excel_handler.py
├── student_data/
│   ├── faces/                 # Stored student images
│   └── embeddings.pkl         # Precomputed face embeddings
├── attendance/
│   └── attendance_log.xlsx    # Daily attendance file
├── screenshot/
│   └── demo.gif               # Demo preview
└── requirements.txt
```

---

## 📊 Excel Report Sample

| Name  | Date       | Time     | Status  |
| ----- | ---------- | -------- | ------- |
| Alice | 2025-07-29 | 09:05 AM | Present |
| Bob   | 2025-07-29 | –        | Absent  |

> Downloaded reports include timestamps and can be filtered by student name or date range.

---

## 🔐 Teacher Login Example

```python
credentials = {
    "usernames": {
        "teacher1": {"name": "John Doe", "password": "1234"},
        ...
    }
}
```

Uses `streamlit_authenticator` for a secure login experience.

---

## 🔮 Future Enhancements

* 📱 Mobile camera integration
* ⏱ Class-wise period tracking
* 🔔 Notification for absent students
* 📧 Email alerts for attendance reports
* ☁️ Cloud sync via Google Drive / Firebase

---

## 🙋‍♂️ Why This Project?

Manual attendance is **slow**, **error-prone**, and **boring**.
This system offers a **smart alternative** by combining real-time face recognition with a modern UI — making attendance smooth for educators and engaging for students.

---

## 🛡️ Security

* No images are stored unless explicitly added for training.
* Authentication protects the admin dashboard.
* Embeddings are stored locally in a `.pkl` file, never exposed online.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE)

---

## 🤝 Contributions

Contributions, issues, and feature requests are welcome!
Feel free to fork, star ⭐, and submit pull requests.

