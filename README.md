 🎓 Face Recognition Based Attendance System

A Python-based Face Recognition Attendance System that automatically
marks student attendance using facial recognition technology.

This project uses face encoding and recognition techniques to identify
students and update attendance records efficiently.

------------------------------------------------------------------------

## 🚀 Features

-   🔍 Real-time face detection\
-   🧠 Face recognition using pre-trained encodings\
-   📸 Image-based student dataset\
-   📝 Automatic attendance marking\
-   📂 JSON-based student data management\
-   🎨 Simple UI with background & mode screens

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   Python 3.9\
-   OpenCV\
-   dlib\
-   face_recognition\
-   NumPy\
-   JSON

------------------------------------------------------------------------

## 📁 Project Structure

Face-Recognition-Attendance-System/ │ ├── main.py\
├── main1.py\
├── generate_encodings.py\
├── EncodeFile.p\
├── students.json\
├── Images/\
└── Resources/

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

git clone
https://github.com/yourusername/Face-Recognition-Attendance-System.git\
cd Face-Recognition-Attendance-System

### 2️⃣ Create Virtual Environment (Recommended)

python -m venv venv\
venv`\Scripts`{=tex}`\activate  `{=tex}

### 3️⃣ Install Required Libraries

pip install opencv-python\
pip install face_recognition\
pip install numpy\
pip install dlib

------------------------------------------------------------------------

## ▶️ How to Run

### Step 1: Generate Face Encodings

python generate_encodings.py

### Step 2: Run Main Application

python main.py

The system will: - Open webcam\
- Detect face\
- Match with stored encodings\
- Mark attendance

------------------------------------------------------------------------

## 🧠 How It Works

1.  Student images are stored in the `Images` folder.\
2.  Face encodings are generated and saved in `EncodeFile.p`.\
3.  When webcam detects a face, it compares with stored encodings.\
4.  If matched → Attendance is marked and stored in JSON file.

------------------------------------------------------------------------

## 📌 Future Improvements

-   🗄️ Database integration (MySQL / Firebase)\
-   🌐 Web-based dashboard\
-   📊 Attendance report export (CSV / Excel)\
-   🔐 Admin login system\
-   ☁️ Cloud deployment

------------------------------------------------------------------------

## 👨‍💻 Author

Vivek Shukla\
B.Tech CSE (AIML)\
Passionate about AI, ML & Computer Vision
