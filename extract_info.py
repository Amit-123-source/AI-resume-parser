import regex as re

def extract_email(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match = re.search(email_pattern, text)
    return match.group(0) if match else None

def extract_phone_number(text):
    phone_pattern = r'(\+?[0-9]{1,2}[\s.-]?)?(\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})'
    match = re.search(phone_pattern, text)
    return match.group(0) if match else None

def extract_name(text):
    name_pattern = r"([A-Z][a-z]+\s[A-Z][a-z]+)"
    match = re.search(name_pattern, text)
    return match.group(0) if match else None

def extract_education(text):
    education_keywords = ['bachelor', 'master', 'phd', 'degree', 'university', 'college']
    return [line.strip() for line in text.split('\n') if any(k in line.lower() for k in education_keywords)]

def extract_skills(text):
    skills_keywords = ['python', 'java', 'c++', 'html', 'css', 'sql', 'excel', 'machine learning',
                       'teamwork', 'communication', 'problem-solving', 'leadership']
    return list({skill for skill in skills_keywords if skill.lower() in text.lower()})

def extract_projects(text):
    project_keywords = ['project', 'worked on', 'developed', 'designed']
    return [line.strip() for line in text.split('\n') if any(k in line.lower() for k in project_keywords)]

def extract_work_experience(text):
    experience_keywords = ['experience', 'worked at', 'employed at', 'interned at', 'role', 'position']
    return [line.strip() for line in text.split('\n') if any(k in line.lower() for k in experience_keywords)]

def extract_hobbies(text):
    hobbies_keywords = ['hobby', 'hobbies', 'interests', 'reading', 'traveling', 'sports', 'music', 'art']
    return [line.strip() for line in text.split('\n') if any(k in line.lower() for k in hobbies_keywords)]

def extract_qualities(text):
    qualities_keywords = ['teamwork', 'leadership', 'problem-solving', 'adaptability', 'creativity', 'initiative']
    return list({quality for quality in qualities_keywords if quality.lower() in text.lower()})

def extract_information(text):
    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone_number(text),
        "Education": "\n".join(extract_education(text)),
        "Skills": ", ".join(extract_skills(text)),
        "Projects": "\n".join(extract_projects(text)),
        "Work Experience": "\n".join(extract_work_experience(text)),
        "Hobbies": ", ".join(extract_hobbies(text)),
        "Qualities": ", ".join(extract_qualities(text))
    }
