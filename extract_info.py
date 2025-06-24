import regex as re
from typing import List, Optional

class ResumeInfoExtractor:
    def __init__(self):
        self.email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.phone_pattern = r'(\+?1[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})'
        self.date_pattern = r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}|\b\d{4}\s*[-–]\s*\d{4}|\b\d{4}\s*[-–]\s*(?:current|present)\b'
        
        self.name_indicators = [
            'NAME', 'FULL NAME', 'CANDIDATE', 'APPLICANT'
        ]
        
        self.name_exclusions = [
            'RESUME', 'CV', 'CURRICULUM VITAE', 'CONTACT', 'EMAIL', 'PHONE', 'ADDRESS',
            'MOBILE', 'TEL', 'TELEPHONE', 'FAX', 'WEBSITE', 'LINKEDIN', 'GITHUB',
            'OBJECTIVE', 'SUMMARY', 'PROFILE', 'ABOUT', 'INTRODUCTION',
            'EXPERIENCE', 'EDUCATION', 'SKILLS', 'PROJECTS', 'REFERENCES',
            'PERSONAL', 'DETAILS', 'INFORMATION', 'QUALIFICATIONS',
            'PROFESSIONAL', 'CAREER', 'BACKGROUND', 'PORTFOLIO',
            'JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE',
            'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER',
            'STREET', 'AVENUE', 'ROAD', 'LANE', 'DRIVE', 'BOULEVARD',
            'CITY', 'STATE', 'COUNTRY', 'ZIP', 'POSTAL'
        ]
        
        self.name_prefixes = ['MR', 'MRS', 'MS', 'DR', 'PROF', 'SIR', 'MISS']
        self.name_suffixes = ['JR', 'SR', 'III', 'IV', 'PHD', 'MD', 'ESQ']
        
        self.section_headers = {
            'education': ['EDUCATION', 'ACADEMIC', 'DEGREE', 'UNIVERSITY', 'COLLEGE', 'SCHOOL'],
            'skills': ['SKILLS', 'TECHNICAL SKILLS', 'COMPETENCIES', 'ABILITIES', 'TECHNOLOGIES'],
            'experience': ['WORK EXPERIENCE', 'EXPERIENCE', 'EMPLOYMENT', 'PROFESSIONAL EXPERIENCE', 'CAREER'],
            'projects': ['PROJECTS', 'PROJECT EXPERIENCE', 'PERSONAL PROJECTS', 'ACADEMIC PROJECTS'],
            'contact': ['CONTACT', 'CONTACT INFO', 'CONTACT INFORMATION']
        }
        
        self.skill_keywords = [
            'python', 'java', 'javascript', 'c++', 'c#', 'php', 'ruby', 'go', 'rust', 'swift',
            'html', 'css', 'react', 'angular', 'vue', 'node.js', 'express', 'django', 'flask',
            'sql', 'mysql', 'postgresql', 'mongodb', 'redis', 'sqlite',
            'git', 'docker', 'kubernetes', 'aws', 'azure', 'linux', 'windows',
            'photoshop', 'illustrator', 'figma', 'sketch', 'indesign', 'after effects',
            'excel', 'tableau', 'power bi', 'machine learning', 'data analysis', 'pandas', 'numpy',
            'teamwork', 'communication', 'problem-solving', 'leadership', 'management', 'analytical'
        ]
        
        self.quality_keywords = [
            'leadership', 'team player', 'collaborative', 'innovative', 'creative', 'analytical',
            'problem-solving', 'detail-oriented', 'organized', 'motivated', 'adaptable',
            'excellent communication', 'results-driven', 'goal-oriented', 'self-motivated',
            'initiative', 'mentoring', 'training', 'strategic thinking'
        ]

    def find_section_content(self, text: str, section_keywords: List[str]) -> str:
        text_upper = text.upper()
        
        for keyword in section_keywords:
            if keyword in text_upper:
                start_idx = text_upper.find(keyword)
                remaining_text = text[start_idx:]
                
                next_sections = []
                for other_section in self.section_headers.values():
                    for other_keyword in other_section:
                        if other_keyword != keyword and other_keyword in remaining_text.upper():
                            idx = remaining_text.upper().find(other_keyword)
                            if idx > 50: 
                                next_sections.append(idx)
                
                end_idx = min(next_sections) if next_sections else min(1000, len(remaining_text))
                return remaining_text[:end_idx]
        
        return ""

    def extract_email(self, text: str) -> Optional[str]:
        matches = re.findall(self.email_pattern, text, re.IGNORECASE)
        valid_emails = [email for email in matches if 'email.com' not in email.lower()]
        return valid_emails[0] if valid_emails else (matches[0] if matches else None)

    def extract_phone_number(self, text: str) -> Optional[str]:
        match = re.search(self.phone_pattern, text)
        if match:
            groups = match.groups()
            if groups[0]:  
                return f"{groups[0]}({groups[1]}) {groups[2]}-{groups[3]}"
            else:
                return f"({groups[1]}) {groups[2]}-{groups[3]}"
        return None

    def is_valid_name_token(self, token: str) -> bool:
        token_upper = token.upper()
        
        if not re.match(r"^[A-Za-z][A-Za-z\-'\.]*[A-Za-z]$|^[A-Za-z]$", token):
            return False
        
        if len(token) < 2 or len(token) > 25:
            return False
        
        if token_upper in self.name_exclusions:
            return False
        
        if '.' in token and any(tld in token.lower() for tld in ['.com', '.org', '.net', '.edu']):
            return False
        
        if re.search(r'\d', token):
            return False
        
        return True

    def clean_name_candidate(self, name_candidate: str) -> str:
        tokens = name_candidate.split()
        cleaned_tokens = []
        
        for token in tokens:
            token_upper = token.upper().rstrip('.,;:')
            
            if token_upper in self.name_prefixes or token_upper in self.name_suffixes:
                if len(tokens) > 2:
                    cleaned_tokens.append(token.title())
            elif self.is_valid_name_token(token):
                cleaned_tokens.append(token.title())
        
        return ' '.join(cleaned_tokens)

    def extract_name(self, text: str) -> Optional[str]:
        lines = text.split('\n')
        
        for i, line in enumerate(lines[:15]):
            line = line.strip()
            line_upper = line.upper()
            
            for indicator in self.name_indicators:
                if indicator in line_upper:
                    if ':' in line:
                        name_part = line.split(':', 1)[1].strip()
                        if name_part:
                            cleaned_name = self.clean_name_candidate(name_part)
                            if cleaned_name and len(cleaned_name.split()) >= 2:
                                return cleaned_name
                    
                    if i + 1 < len(lines):
                        next_line = lines[i + 1].strip()
                        cleaned_name = self.clean_name_candidate(next_line)
                        if cleaned_name and len(cleaned_name.split()) >= 2:
                            return cleaned_name
        
        potential_names = []
        
        for line in lines[:20]:
            line = line.strip()
            
            if not line or len(line) < 3:
                continue
            
            line_upper = line.upper()
            if any(exclusion in line_upper for exclusion in self.name_exclusions):
                continue
            
            if '@' in line or re.search(self.phone_pattern, line):
                continue
            
            if len(re.sub(r'[A-Za-z\s]', '', line)) > len(line) * 0.3:
                continue
            
            name_patterns = [
                r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]*\.?\s+)?[A-Z][a-z]+)$',
                r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]*\.?\s+)?[A-Z][a-z]+)[,\.]?\s*$',
                r'^([A-Z]+\s+[A-Z]+(?:\s+[A-Z]+)?)$',
                r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})$',
                r'^([A-Z][a-z]+(?:[-\'][A-Z][a-z]+)?\s+[A-Z][a-z]+(?:[-\'][A-Z][a-z]+)?)$'
            ]
            
            for pattern in name_patterns:
                match = re.match(pattern, line)
                if match:
                    candidate_name = match.group(1)
                    cleaned_name = self.clean_name_candidate(candidate_name)
                    
                    if cleaned_name and len(cleaned_name.split()) >= 2:
                        score = self.score_name_candidate(cleaned_name, lines.index(line + '\n') if line + '\n' in lines else 0)
                        potential_names.append((cleaned_name, score))
        
        if not potential_names:
            for i, line in enumerate(lines[:15]):
                line = line.strip()
                
                words = line.split()
                if len(words) >= 2:
                    capitalized_words = [w for w in words if w and w[0].isupper() and self.is_valid_name_token(w)]
                    
                    if len(capitalized_words) >= 2 and len(capitalized_words) <= 4:
                        candidate_name = ' '.join(capitalized_words)
                        cleaned_name = self.clean_name_candidate(candidate_name)
                        
                        if cleaned_name and len(cleaned_name.split()) >= 2:
                            score = self.score_name_candidate(cleaned_name, i)
                            potential_names.append((cleaned_name, score))
        
        if potential_names:
            potential_names.sort(key=lambda x: x[1], reverse=True)
            return potential_names[0][0]
        
        return None

    def score_name_candidate(self, name: str, line_position: int) -> float:
        score = 0.0
        
        if line_position <= 3:
            score += 3.0
        elif line_position <= 6:
            score += 2.0
        elif line_position <= 10:
            score += 1.0
        
        name_parts = name.split()
        if len(name_parts) == 2:
            score += 2.0
        elif len(name_parts) == 3:
            score += 1.5
        elif len(name_parts) == 4:
            score += 0.5
        
        if all(part[0].isupper() and part[1:].islower() for part in name_parts if part):
            score += 1.0
        elif all(part.isupper() for part in name_parts):
            score += 0.5
        
        avg_part_length = sum(len(part) for part in name_parts) / len(name_parts)
        if 3 <= avg_part_length <= 8:
            score += 0.5
        
        return score

    def extract_education(self, text: str) -> str:
        education_text = self.find_section_content(text, self.section_headers['education'])
        
        if not education_text:
            education_keywords = ['bachelor', 'master', 'phd', 'doctorate', 'degree', 'university', 
                                'college', 'b.a.', 'b.s.', 'm.a.', 'm.s.', 'mba', 'b.f.a.', 'm.ed.']
            education_lines = []
            for line in text.split('\n'):
                if any(keyword in line.lower() for keyword in education_keywords):
                    education_lines.append(line.strip())
            return '\n'.join(education_lines)
        
        lines = [line.strip() for line in education_text.split('\n') if line.strip()]
        filtered_lines = [line for line in lines if not any(header in line.upper() for header in self.section_headers['education'])]
        
        return '\n'.join(filtered_lines[:5])

    def extract_skills(self, text: str) -> str:
        skills_text = self.find_section_content(text, self.section_headers['skills'])
        found_skills = set()
        
        if skills_text:
            text_to_search = skills_text.lower()
        else:
            text_to_search = text.lower()
        
        for skill in self.skill_keywords:
            if skill.lower() in text_to_search:
                found_skills.add(skill.title())
        
        if skills_text:
            potential_skills = re.split(r'[•\n;,|]', skills_text)
            for skill in potential_skills:
                skill = skill.strip()
                if 2 < len(skill) < 30 and not any(header in skill.upper() for header in self.section_headers['skills']):
                    found_skills.add(skill)
        
        return ', '.join(sorted(found_skills))

    def extract_projects(self, text: str) -> str:
        projects_text = self.find_section_content(text, self.section_headers['projects'])
        
        if projects_text:
            lines = [line.strip() for line in projects_text.split('\n') if line.strip()]
            filtered_lines = [line for line in lines if not any(header in line.upper() for header in self.section_headers['projects'])]
            return '\n'.join(filtered_lines)
        
        project_keywords = ['project', 'developed', 'built', 'created', 'designed', 'implemented']
        project_lines = []
        for line in text.split('\n'):
            if any(keyword in line.lower() for keyword in project_keywords) and len(line.strip()) > 20:
                project_lines.append(line.strip())
        
        return '\n'.join(project_lines[:5])

    def extract_work_experience(self, text: str) -> str:
        exp_text = self.find_section_content(text, self.section_headers['experience'])
        
        if exp_text:
            lines = [line.strip() for line in exp_text.split('\n') if line.strip()]
            filtered_lines = [line for line in lines if not any(header in line.upper() for header in self.section_headers['experience'])]
            return '\n'.join(filtered_lines)
        
        experience_patterns = [
            r'.*(?:worked at|employed at|interned at|position at|role at).*',
            r'.*\d{4}\s*[-–]\s*(?:\d{4}|current|present).*',
            r'.*(?:manager|developer|analyst|coordinator|specialist|assistant|intern).*'
        ]
        
        exp_lines = []
        for line in text.split('\n'):
            for pattern in experience_patterns:
                if re.search(pattern, line, re.IGNORECASE) and len(line.strip()) > 15:
                    exp_lines.append(line.strip())
                    break
        
        return '\n'.join(exp_lines[:10])

    def extract_hobbies(self, text: str) -> str:
        hobbies_keywords = ['hobby', 'hobbies', 'interests', 'interest', 'reading', 'traveling', 
                          'sports', 'music', 'art', 'photography', 'cooking', 'gaming',
                          'volunteering', 'volunteer', 'activities', 'personal interests']
        
        found_hobbies = set()
        text_lower = text.lower()
        
        for keyword in hobbies_keywords:
            if keyword in text_lower:
                for line in text.split('\n'):
                    if keyword in line.lower() and len(line.strip()) > 5:
                        hobby_line = line.strip()
                        if not any(h in hobby_line.upper() for h in ['HOBBIES', 'INTERESTS']):
                            found_hobbies.add(hobby_line)
        
        return ', '.join(list(found_hobbies)[:5])

    def extract_qualities(self, text: str) -> str:
        found_qualities = set()
        text_lower = text.lower()
        
        for quality in self.quality_keywords:
            if quality.lower() in text_lower:
                found_qualities.add(quality.title())
        
        quality_patterns = [
            r'excellent\s+(\w+(?:\s+\w+)?)',
            r'strong\s+(\w+(?:\s+\w+)?)',
            r'proven\s+(\w+(?:\s+\w+)?)',
            r'outstanding\s+(\w+(?:\s+\w+)?)'
        ]
        
        for pattern in quality_patterns:
            matches = re.findall(pattern, text_lower)
            for match in matches:
                if len(match) > 3:
                    found_qualities.add(match.title())
        
        return ', '.join(sorted(found_qualities))

extractor = ResumeInfoExtractor()

def extract_email(text):
    return extractor.extract_email(text)

def extract_phone_number(text):
    return extractor.extract_phone_number(text)

def extract_name(text):
    return extractor.extract_name(text)

def extract_education(text):
    return extractor.extract_education(text)

def extract_skills(text):
    return extractor.extract_skills(text)

def extract_projects(text):
    return extractor.extract_projects(text)

def extract_work_experience(text):
    return extractor.extract_work_experience(text)

def extract_hobbies(text):
    return extractor.extract_hobbies(text)

def extract_qualities(text):
    return extractor.extract_qualities(text)

def extract_information(text):
    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone_number(text),
        "Education": extract_education(text),
        "Skills": extract_skills(text),
        "Projects": extract_projects(text),
        "Work Experience": extract_work_experience(text),
        "Hobbies": extract_hobbies(text),
        "Qualities": extract_qualities(text)
    }
