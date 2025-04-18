# career-potential-face-analyzer
Facial analysis for speculative personality and career path insights. Note: Lacks scientific backing, use responsibly.

## Key Features:
- Analyze facial features from images.
- Speculate on personality traits based on facial features.
- Suggest potential career paths.

---

## Technologies Used:
- Python (Flask framework)
- OpenCV, mediapine, dlib for image processing
- Supporting libraries such as numpy and pandas

---

## Setup and Installation

### 1. System Requirements
Ensure you have:
- Python 3.12
- pip (Python Package Installer)

### 2. Clone Repository
```bash
git clone https://github.com/yourusername/career-potential-face-analyzer.git
cd career-potential-face-analyzer
cd Image-BasedTraitAssessment
```

### 3. Environment
First, install cmake, and python 3.12.

Then open the project.

*`Note`: open the Image-Based Trait Assessment project folder in the IDE, not the repository folder*
```
python -m venv venv
```

**For Ubuntu**
```
python3.12 -m venv venv
```

**Windows**
```
venv\Scripts\activate 
```

**MacOS or Ubuntu**
```
source venv/bin/activate
```


### 4. Install Required Libraries
```
pip install -r requirements.txt
```

**For Ubuntu**
```
python3.12 -m pip install setuptools
```
Install dlib library separately to avoid errors:
```
git clone https://github.com/davisking/dlib.git
cd dlib
python3.12 setup.py install
```
```
pip install -r requirements.txt
```

### 5. Run Flask Server
```
python app/index.py
```

**For Ubuntu**
```
sudo apt update
sudo apt install libffi-dev
```
libffi is the library that Python uses to build _ctypes. Python uses the _ctypes module to support calling functions from C dynamic libraries, and _ctypes depends on libffi to do this. 

After installation is complete, check:
```
python3.12 -c "import _ctypes"
```
If there is no error, it is ok.

```
export PYTHONPATH=/var/www/Image-BasedTraitAssessment
python app/index.py
```

### 6. Access the Application
Open your browser and go to: http://127.0.0.1:5000

---

## Project Structure

---

## Usage Guide

- Upload a facial image.
- Receive analysis results.
- Explore suggested career paths.

---

## Important Notes
This project is experimental and not based on any scientific research. Results should not be used for making critical decisions.

