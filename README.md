# AI Attendance System - Frontend

A modern, responsive frontend for the AI Attendance System using Flask and facial recognition technology.

## Features

✨ **Modern UI**
- Beautiful gradient design with smooth animations
- Fully responsive Bootstrap 5 framework
- Real-time facial recognition monitoring
- Comprehensive attendance logging

🎯 **Key Features**
- Live webcam monitoring with face detection overlays
- Student registration with photo upload
- Automatic attendance marking
- Complete attendance history and logs
- Intuitive navigation and user experience

## Pages

### 1. **Home Page** (`index.html`)
- Welcome screen with system overview
- Feature highlights
- Quick access to Live Monitor and Registration

### 2. **Live Monitor** (`monitor.html`)
- Real-time webcam feed with face detection
- Live overlay with detected student names
- Automatic attendance logging
- System status and statistics

### 3. **Student Registration** (`register.html`)
- Student information input form
- Profile photo upload
- Registration guidelines and best practices
- Form validation and error handling

### 4. **Attendance Log** (`attendance_view.html`)
- Complete attendance history
- Student details and timestamps
- Summary statistics
- Sortable and filterable records

### 5. **Base Template** (`base.html`)
- Navigation bar with all links
- Flash messages display
- Footer
- Global styling and layout

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/ai_attendance_frontend.git
cd ai_attendance_frontend
```

2. Copy these template files to your Flask app's `templates/` folder:
```bash
cp *.html /path/to/your/flask_app/app/templates/
```

3. Make sure your Flask backend is running and configured with these routes:
   - `/` - Home page
   - `/monitor` - Live monitoring
   - `/register` - Student registration
   - `/attendance` - Attendance logs
   - `/process_frame` - Frame processing endpoint (POST)

## Technologies Used

- **HTML5** - Semantic markup
- **Bootstrap 5** - Responsive framework
- **CSS3** - Advanced styling with gradients and animations
- **JavaScript** - Real-time camera feed handling
- **Font Awesome Icons** - Beautiful icon library

## Design Features

🎨 **Modern Design**
- Gradient backgrounds and buttons
- Smooth animations and transitions
- Professional color scheme
- Font Awesome icons throughout

📱 **Responsive**
- Mobile-friendly layouts
- Touch-optimized interfaces
- Works on all screen sizes

✨ **User Experience**
- Intuitive navigation
- Clear visual hierarchy
- Helpful tips and guidelines
- Real-time status updates

## Color Palette

- **Primary**: #6366f1 (Indigo)
- **Secondary**: #8b5cf6 (Purple)
- **Success**: #10b981 (Green)
- **Danger**: #ef4444 (Red)
- **Warning**: #f59e0b (Amber)

## Browser Support

- Chrome/Edge (Recommended)
- Firefox
- Safari
- Mobile browsers

## Usage

1. Start your Flask application
2. Open `http://localhost:5000` in your browser
3. Use the navigation menu to access different features
4. Register students with clear facial photos
5. Start the live monitor to track attendance

## Notes

- Ensure good lighting for accurate facial recognition
- Upload clear, frontal face photos for best results
- Allow camera permissions when prompted
- Keep student database up to date

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.

## Author

AI Attendance System Contributors

---

**Made with ❤️ for educational institutions**
