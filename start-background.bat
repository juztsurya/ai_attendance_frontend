@echo off
REM Launch Flask app in background
start "" python "C:\AI_Attendance_App\run.py"
echo AI Attendance System started in background
echo Access at: http://127.0.0.1:5000
timeout /t 3