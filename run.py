from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    # Development mode (local)
    debug = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug, threaded=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
