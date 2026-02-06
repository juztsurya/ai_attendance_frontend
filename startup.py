"""
Startup helper script for AI Attendance System
Run this to start the Flask application in the background
"""
import subprocess
import os
import time
import webbrowser

def start_app():
    """Start the Flask application"""
    os.chdir("C:\\AI_Attendance_App")
    
    print("=" * 60)
    print("🚀 AI Attendance System Startup")
    print("=" * 60)
    print("\n📝 Starting Flask application...")
    
    # Start Flask app
    subprocess.Popen([
        "python", 
        "run.py"
    ], 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE
    )
    
    print("✅ Flask application started!")
    print("\n🌐 Access Points:")
    print("   Local:   http://127.0.0.1:5000")
    print("   Network: http://192.168.1.68:5000")
    
    # Wait for server to start
    time.sleep(3)
    
    # Open browser
    print("\n📱 Opening browser...")
    webbrowser.open("http://127.0.0.1:5000")
    
    print("\n✨ Application is ready!")
    print("=" * 60)
    
    # Keep checking if app is running
    print("\nPress Ctrl+C to stop the application")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n⛔ Stopping application...")
        print("Goodbye!")

if __name__ == "__main__":
    start_app()
