from flask import Flask, request, redirect, url_for, render_template, session
import subprocess
import os
import csv

app = Flask(__name__)
app.secret_key = 'your_secret_key'  
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Save the uploaded video
    video = request.files['video']
    video_path = os.path.join(video.filename)
    video.save(video_path)

    # Run the Python scripts
    subprocess.run(['python', 'annotate_init_bbox.py', '--video', video_path, '--paper_frame_size', '2'])
    subprocess.run(['python', 'velocity_pipeline.py', '--video', video_path])


    session['patient_data'] = {
        'first_name': request.form.get('firstName'),
        'last_name': request.form.get('lastName'),
        'age': request.form.get('age'),
        'email': request.form.get('email')
    }

    # Redirect to results page
    return redirect(url_for('results')) 


@app.route('/results')
def results():
    patient_data = session.get('patient_data', {})

    # read data from CSV file
    csv_data = []
    with open('output_ref_error.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            csv_data.append(row)

    # Render the results template
    return render_template('results.html', patient_data=patient_data, csv_data=csv_data)


if __name__ == '__main__':
    app.run(debug=True)
