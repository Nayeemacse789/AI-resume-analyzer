def match_resume_with_job(resume_data, job_description):
    matches = [skill for skill in resume_data['skills'] if skill.lower() in job_description.lower()]
    score = int((len(matches) / len(resume_data['skills']) * 100)) if resume_data['skills'] else 0
    return {
        'matched_skills': matches,
        'score': score
    }
