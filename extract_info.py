import re

def extract_email(text):
    """ Extracts the email address from the text. """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match = re.search(email_pattern, text)
    return match.group(0) if match else None

def extract_phone_number(text):
    """ Extracts the phone number from the text. """
    phone_pattern = r'(\+?[0-9]{1,2})?[\s.-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}'
    match = re.search(phone_pattern, text)
    return match.group(0) if match else None

def extract_name(text):
    """ Extracts the name from the text (assuming it's the first found). """
    name_pattern = r"([A-Z][a-z]\s[A-Z][a-z])"
    match = re.search(name_pattern, text)
    return match.group(0) if match else None

def extract_education(text):
    """ Extracts education-related information. """
    education_keywords = ['bachelor', 'master', 'phd', 'degree', 'university', 'college']
    education_info = []
    for line in text.split('\n'):
        if any(keyword in line.lower() for keyword in education_keywords):
            education_info.append(line.strip())
    return education_info

def extract_skills(text):
    """ Extracts skills from the text. """
    skills_keywords = ['python', 'java', 'c++', 'html', 'css', 'sql', 'excel', 'machine learning']
    skills = []
    for skill in skills_keywords:
        if skill.lower() in text.lower():
            skills.append(skill)
    return skills

def extract_projects(text):
    """ Extracts project-related information from the text. """
    project_keywords = ['project', 'worked on', 'developed', 'designed']
    projects = []
    for line in text.split('\n'):
        if any(keyword in line.lower() for keyword in project_keywords):
            projects.append(line.strip())
    return projects

def extract_information(text):
    """ Extracts all required information from the resume text. """
    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone_number(text)
    education = extract_education(text)
    skills = extract_skills(text)
    projects = extract_projects(text)
    
    return {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Education": "\n".join(education),
        "Skills": ", ".join(skills),
        "Projects": "\n".join(projects)
    }