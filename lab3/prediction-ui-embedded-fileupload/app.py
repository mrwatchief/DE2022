# importing Flask and other modules
import os
from pathlib import Path

import pandas as pd
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename

from diabetes_predictor import DiabetesPredictor

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@app.route('/checkdiabetes', methods=["GET", "POST"])
def check_diabetes():
    if request.method == "POST":
        # we are going to save the file locally at a folder. if the folder does not exist, we need to create it
        home = str(Path.home())
        soda_home = os.path.join(home, ".service")
        if not os.path.exists(soda_home):
            os.makedirs(soda_home)
        # pfile is the name we used in the user_form.html
        if 'pfile' not in request.files:
            return jsonify({'message': 'No file part in the request'}, sort_keys=False, indent=4), 400

        file = request.files['pfile']

        if file.filename == '':
            return jsonify({'message': 'No file selected for uploading'}, sort_keys=False, indent=4), 400
        else:
            # save the uploaded file locally (at the server side)
            filename = secure_filename(file.filename)
            file_path = os.path.join(soda_home, filename)
            file.save(file_path)
            # make predictions
            df = pd.read_json(file_path)
            dp = DiabetesPredictor()
            status = dp.predict_single_record(df)
            # clean up - remove the downloaded file
            try:
                os.remove(file_path)
            except Exception as error:
                app.logger.error("Error removing or closing downloaded file handle", error)
            return jsonify({'result': str(status[0])}), 200

    return render_template(
        "user_form.html")  # this method is called of HTTP method is GET, e.g., when browsing the link


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)
