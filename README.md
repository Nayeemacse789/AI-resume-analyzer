# AI Resume Analyzer

This is a simple Flask-based web app that analyzes resumes and matches them against a job description using basic NLP techniques.

## Features

- Upload `.docx` resumes
- Extract skills from resume content
- Compare with job description
- Show match score and matched skills

## How to Run

```bash
pip install flask docx2txt
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## Project Structure

- `app.py`: Main Flask app
- `resume_parser.py`: Extracts text and skills from resume
- `job_matcher.py`: Matches resume with job description
- `templates/`: HTML templates
- `resumes/`: Uploaded resumes

## License

MIT
