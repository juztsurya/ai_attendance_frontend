# AI Attendance System - Complete Application

A complete Flask-based AI Attendance System with facial recognition. This is the integrated backend application with the modern frontend.

## Features

✨ **Modern Frontend**
- Beautiful gradient design with smooth animations
- Fully responsive Bootstrap 5 framework
- Real-time facial recognition monitoring
- Comprehensive attendance logging

🎯 **Backend Capabilities**
- Live webcam monitoring with face detection overlays
- Student registration with photo upload
- Automatic attendance marking
- Complete attendance history and logs
- SQLite database for persistent storage
- LBPH face recognition model

## Project Structure

```
AI_Attendance_App/
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── models.py            # Database models (Student, Attendance)
│   ├── routes.py            # All API routes and endpoints
│   ├── templates/           # HTML templates
│   │   ├── base.html        # Base template with navigation
│   │   ├── index.html       # Home page
│   │   ├── register.html    # Registration form
│   │   ├── monitor.html     # Live monitoring
│   │   └── attendance_view.html  # Attendance logs
│   └── static/              # Static files (CSS, JS, images)
├── instance/                # Instance folder (database)
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
└── README.md               # Documentation
```

## Installation

### 1. Prerequisites
- Python 3.9+
- pip (Python package manager)
- Git

### 2. Clone the Repository
```bash
git clone https://github.com/juztsurya/ai_attendance_frontend.git
cd AI_Attendance_App
```

### 3. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
python run.py
```

The application will start at: `http://localhost:5000`

## Routes and Endpoints

### Frontend Routes
- **`/`** - Home page with system overview
- **`/monitor`** - Live monitoring dashboard with webcam
- **`/register`** - Student registration form
- **`/attendance`** - Attendance log viewer

### Backend API Endpoints
- **`POST /process_frame`** - Process video frames for face recognition
  - Accepts: Base64 encoded image
  - Returns: Detected faces with coordinates and names

## Database Models

### Student
```python
- id (Integer, Primary Key)
- name (String, 100 chars)
- student_id (String, 20 chars, Unique)
- created_at (DateTime)
- attendance_records (Relationship)
```

### Attendance
```python
- id (Integer, Primary Key)
- student_id (Integer, Foreign Key)
- timestamp (DateTime)
- status (String, default: 'Present')
```

## Usage Guide

### 1. Register Students
- Go to "Register Student" page
- Enter student name and ID
- Upload a clear facial photo
- System trains the recognition model automatically

### 2. Start Monitoring
- Go to "Live Monitor" page
- Allow camera permissions
- System will detect faces and automatically log attendance
- Detected students appear in green, unknowns in red

### 3. View Attendance
- Go to "Attendance Log" page
- View all recorded attendance with timestamps
- See student names and IDs
- Filter and search if needed

## Configuration

### Environment Variables
```bash
K_SERVICE          # Set for Cloud Run deployment
K_REVISION         # Set for Cloud Run deployment
```

### Settings (in `app/__init__.py`)
- `SECRET_KEY` - Change this in production!
- `SQLALCHEMY_DATABASE_URI` - Database connection
- Database location switches to `/tmp` on Cloud Run

## Technical Details

### Face Recognition
- **Algorithm**: LBPH (Local Binary Patterns Histograms)
- **Detection**: Haar Cascade Classifier
- **Confidence Threshold**: 80 (lower is better match)
- **Processing Speed**: 5 FPS (configurable)

### Image Processing
- Format: JPEG (quality: 0.8)
- Resolution: 640x480
- Color Space: Grayscale for processing
- Face Detection Parameters: scaleFactor=1.1, minNeighbors=4

## Deployment

### Local Development
```bash
python run.py
```

### Production (Gunicorn)
```bash
gunicorn --bind 0.0.0.0:8080 --workers 1 --threads 8 --timeout 0 run:app
```

### Docker
```bash
docker build -t ai-attendance .
docker run -p 8080:8080 ai-attendance
```

## Technologies Used

### Backend
- **Flask** - Web framework
- **Flask-SQLAlchemy** - ORM
- **OpenCV** - Computer vision
- **NumPy** - Array operations

### Frontend
- **HTML5** - Semantic markup
- **Bootstrap 5** - Responsive framework
- **CSS3** - Advanced styling
- **JavaScript** - Client-side processing

## Performance Tips

1. **Good Lighting**: Better for face detection accuracy
2. **Clear Photos**: Upload frontal, well-lit student photos
3. **Camera Quality**: Higher resolution helps
4. **Maintenance**: Retrain model when adding new students
5. **Database**: Consider migration to PostgreSQL for production

## Troubleshooting

### Camera not working
- Check browser permissions
- Use HTTPS in production (required for camera)
- Restart application

### Poor face recognition
- Upload clearer photos
- Ensure good lighting
- Train model with more student photos
- Adjust confidence threshold in code

### Database issues
- Delete `instance/database.sqlite`
- Restart application
- Check file permissions

## Security Notes

⚠️ **Before Production:**
- Change `SECRET_KEY` in `app/__init__.py`
- Use environment variables for configuration
- Enable HTTPS
- Implement user authentication
- Add rate limiting
- Validate all inputs
- Use strong database credentials

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License - See LICENSE file for details

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the code comments
3. Check GitHub issues
4. Contact the development team

---

**Made with ❤️ for educational institutions**

## Quick Start Command
```bash
# Windows
python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && python run.py

# macOS/Linux
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python run.py
```

---

**Repository**: https://github.com/juztsurya/ai_attendance_frontend
