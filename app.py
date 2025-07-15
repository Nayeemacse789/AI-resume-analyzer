from flask import Flask, render_template, request
import os
from resume_parser import parse_resume
from job_matcher import match_resume_with_job

app = Flask(__name__)
UPLOAD_FOLDER = 'resumes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    resume_file = request.files['resume']
    job_description = request.form['job_description']
    if resume_file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
        resume_file.save(filepath)
        resume_data = parse_resume(filepath)
        match_result = match_resume_with_job(resume_data, job_description)
        return render_template('result.html', resume=resume_data, match=match_result)
    return 'No file uploaded'

if __name__ == "__main__":
    app.run(debug=True)
