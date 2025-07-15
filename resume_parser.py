import docx2txt
import re

def parse_resume(file_path):
    text = docx2txt.process(file_path)
    skills = re.findall(r'(?i)(python|java|c\+\+|machine learning|data science|sql|react)', text)
    return {
        'text': text,
        'skills': list(set(skills)),
        'length': len(text)
    }
