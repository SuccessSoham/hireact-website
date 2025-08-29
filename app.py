# app.py
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for serving static CSS files
@app.route('/static/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('static/css', filename)

# Route for serving static JS files
@app.route('/static/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('static/js', filename)

# Route for serving images
@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

if __name__ == '__main__':
    # Create static/css and static/js directories if they don't exist
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    os.makedirs('images', exist_ok=True) # Ensure images directory exists
    app.run(debug=True)

print("Please save the above code as 'app.py'.")
print("Make sure you have Flask installed: pip install Flask")
print("Also, ensure you have created 'static/css', 'static/js', and 'images' folders and placed the respective files inside them.")
