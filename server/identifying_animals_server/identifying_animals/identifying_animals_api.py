import os
from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename
from server.identifying_animals_server.identifying_animals.identification_processing import evaluate_one_image

IDENTIFYING_ANIMALS_API = Blueprint("identifying_animals_api", __name__)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@IDENTIFYING_ANIMALS_API.route("/v1/bing/distinguish/animals", methods=["GET", "POST"])
def post_poi_mapping_data():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join("./static/images/", filename))
            result = evaluate_one_image(filename)
            return render_template('upload_ok.html', result=result, imagename=filename)

        return render_template('upload_ok.html', result="耗子尾汁", imagename="error.jpg")

    return render_template('upload_image.html')
