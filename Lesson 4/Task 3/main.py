from flask import Flask, render_template, request, abort, jsonify, url_for
import os

app = Flask(__name__)

IMAGE_FOLDER = 'images'
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

image_files = [file for file in os.listdir(IMAGE_FOLDER) if os.path.isfile(os.path.join(IMAGE_FOLDER, file))]
image_index = 0

@app.route('/')
def index():
    return render_template('gallery.html', image=url_for('static', filename=f'images/{image_files[image_index]}'))

@app.route('/image', methods=['POST'])
def show_image():
    global image_index

    data = request.get_json()
    direction = data.get('direction', 'next')

    if direction == 'prev':
        image_index = (image_index - 1) % len(image_files)
    elif direction == 'next':
        image_index = (image_index + 1) % len(image_files)

    return jsonify({'image': url_for('static', filename=f'images/{image_files[image_index]}')})

app.run(debug=True)
