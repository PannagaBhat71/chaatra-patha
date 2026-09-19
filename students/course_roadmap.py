import os
import re
import urllib.parse
from pathlib import Path
from django.conf import settings
from .skills_data import SKILLS_DICTIONARY as CATEGORY_TAXONOMY, ALL_SKILLS_LIST

# Curated high-fidelity YouTube video IDs for official interactive watch verification
COURSE_VIDEO_IDS = {
    "cybersecurity": "inWWhr5tnEA",
    "machine-learning": "i_LwzRVP7bg",
    "devops": "hQcFE0RD0cQ",
    "mobile-development": "VPvVD8t02U8",
    "qa-testing": "sO8eGL6QVUw",
    "blockchain": "gyMwXuJrbJQ",
    "iot": "6mBO2vqLv38",
    "prompt-engineering": "_ZvnD73m40o",
    "server-maintenance": "kGY8e658y28",
    "software-architecture": "77flD_3F3kU",
    "quantitative-research": "xxpc-HPKN28",
    "sql": "HXV3zeRR3h4",
    "data-analysis": "r-uOLxNrNk8",
    "statistical-analysis": "xxpc-HPKN28",
    "data-visualization": "ztnT3_T-p4A",
    "data-engineering": "kZ_QJcW5540",
    "business-intelligence": "ztnT3_T-p4A",
    "data-mining": "r-uOLxNrNk8",
    "big-data": "1vbXmCrkT3Y",
    "predictive-modeling": "i_LwzRVP7bg",
    "content-marketing": "x_0gT4S2_uY",
    "copywriting": "Xn_7U7c4tA0",
    "social-media": "c8wS0s3eG74",
    "market-research": "xxpc-HPKN28",
    "seo": "DvwS7cV9GmQ",
    "sem-ppc": "045k286E95g",
    "email-marketing": "z8iE2y1Y3iI",
    "crm": "c8wS0s3eG74",
    "lead-generation": "045k286E95g",
    "brand-management": "c8wS0s3eG74",
    "video-marketing": "x_0gT4S2_uY",
    "digital-marketing-strategy": "DvwS7cV9GmQ",
    "ecommerce": "c8wS0s3eG74",
    "public-relations": "x_0gT4S2_uY",
    "sales": "c8wS0s3eG74",
    "financial-accounting": "yYX4bS44n3E",
    "inventory-control": "yYX4bS44n3E",
    "budgeting": "yYX4bS44n3E",
    "supply-chain": "yYX4bS44n3E",
    "quality-control": "sO8eGL6QVUw",
    "financial-modeling": "yYX4bS44n3E",
    "risk-management": "yYX4bS44n3E",
    "business-analysis": "r-uOLxNrNk8",
    "contract-negotiation": "yYX4bS44n3E",
    "compliance": "yYX4bS44n3E",
}


def get_base_dir():
    try:
        return settings.BASE_DIR
    except Exception:
        return Path(__file__).resolve().parent.parent


def load_user_roadmap_resources():
    """
    Dynamically loads the user's custom 'course-specification.py' and 'youtube link.py'
    from the project root directory, preserving exact custom dictionaries and functions.
    """
    base_dir = get_base_dir()
    spec_file = os.path.join(base_dir, 'course-specification.py')
    yt_file = os.path.join(base_dir, 'youtube link.py')

    execution_scope = {'SKILLS_DICTIONARY': {}}

    # Load course specifications
    if os.path.exists(spec_file):
        try:
            with open(spec_file, 'r', encoding='utf-8') as f:
                exec(f.read(), execution_scope)
        except Exception as e:
            print(f"Warning: Error loading course-specification.py: {e}")

    courses_dict = execution_scope.get('SKILLS_DICTIONARY', {})

    # Load youtube links generator
    get_yt_func = None
    if os.path.exists(yt_file):
        try:
            with open(yt_file, 'r', encoding='utf-8') as f:
                exec(f.read(), execution_scope)
            get_yt_func = execution_scope.get('get_youtube_links')
        except Exception as e:
            print(f"Warning: Error loading youtube link.py: {e}")

    # Fallback youtube link generator if missing
    if not callable(get_yt_func):
        def default_yt_func(skill_slug, data_dict=courses_dict):
            skill = data_dict.get(skill_slug)
            if not skill:
                return []
            course_name = skill.get("name", skill_slug.replace("-", " ").title())
            languages = {
                "en": "English",
                "hi": "Hindi",
                "kn": "Kannada",
                "ml": "Malayalam",
                "fr": "French",
            }
            res = []
            for code, lang in languages.items():
                query = f"{course_name} tutorial full course beginner to advanced in {lang}"
                encoded_query = urllib.parse.quote_plus(query)
                res.append({
                    "language_code": code,
                    "language_name": lang,
                    "url": f"https://www.youtube.com/results?search_query={encoded_query}",
                    "type": "YOUTUBE_SEARCH"
                })
            return res
        get_yt_func = default_yt_func

    return courses_dict, get_yt_func


def slugify_skill(name):
    """
    Standardize a skill name into a URL/dictionary-friendly slug.
    """
    if not name:
        return ""
    slug = re.sub(r'\(.*?\)', '', name)  # remove parenthetical info
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', slug).strip('-').lower()
    return slug


def get_roadmap_for_skill(skill_input):
    """
    Retrieves or generates a complete course roadmap for a skill.
    Uses course-specification.py and youtube link.py if defined,
    or generates an aligned structured curriculum as fallback.
    """
    courses_dict, get_youtube_links = load_user_roadmap_resources()

    clean_name = skill_input.strip()
    slug_candidate = slugify_skill(clean_name)

    # 1. Exact match on slug
    course_data = courses_dict.get(slug_candidate)
    matched_slug = slug_candidate

    # 2. Match by exact or normalized 'name' attribute
    if not course_data:
        lower_input = clean_name.lower()
        for k, v in courses_dict.items():
            course_name = v.get("name", "").lower()
            if course_name == lower_input or slugify_skill(course_name) == slug_candidate:
                course_data = v
                matched_slug = k
                break

    # 3. Partial substring match against course names
    if not course_data:
        for k, v in courses_dict.items():
            if k in slug_candidate or slug_candidate in k:
                course_data = v
                matched_slug = k
                break

    # 4. Fallback curriculum if skill is outside the 45 batch-2 specifications
    if not course_data:
        track_name = "Professional Specialization"
        for cat, skills in CATEGORY_TAXONOMY.items():
            if any(s.lower() == clean_name.lower() for s in skills):
                track_name = cat
                break

        matched_slug = slug_candidate or "course-roadmap"
        course_data = {
            "name": clean_name,
            "track": track_name,
            "level": "INTERMEDIATE",
            "stage": "CORE",
            "prerequisites": ["foundational-concepts"],
            "subtopics": [
                f"Core Principles & Environment Setup for {clean_name}",
                f"Essential Syntax, Tools & Practical Workflows",
                f"Architecture Patterns & Practical Problem Solving",
                f"Optimization, Security & Industry Best Practices",
                f"Testing, Debugging & Production Deployment",
            ],
            "project": f"Architect and deploy an end-to-end applied portfolio project mastering {clean_name}."
        }

    # Generate full course YouTube links across 5 languages
    try:
        yt_links = get_youtube_links(matched_slug, data_dict={matched_slug: course_data, **courses_dict})
    except Exception:
        c_name = course_data.get("name", clean_name)
        languages = {"en": "English", "hi": "Hindi", "kn": "Kannada", "ml": "Malayalam", "fr": "French"}
        yt_links = []
        for code, lang in languages.items():
            query = f"{c_name} tutorial full course beginner to advanced in {lang}"
            yt_links.append({
                "language_code": code,
                "language_name": lang,
                "url": f"https://www.youtube.com/results?search_query={urllib.parse.quote_plus(query)}",
                "type": "YOUTUBE_SEARCH"
            })

    # Assigned default verification video ID
    course_video_id = COURSE_VIDEO_IDS.get(matched_slug, "rfscVS0vtbw")

    # Prepare structured milestones list with video verification metadata
    milestones = []
    step_counter = 1

    # 1. Prerequisite Milestone
    prereqs = course_data.get("prerequisites", [])
    if prereqs:
        prereq_names = []
        for p in prereqs:
            if p in courses_dict:
                prereq_names.append(courses_dict[p].get("name", p.replace("-", " ").title()))
            else:
                prereq_names.append(p.replace("-", " ").title())

        query = f"{course_data.get('name')} prerequisites tutorial"
        milestones.append({
            "step": step_counter,
            "id": f"step-{step_counter}",
            "type": "PREREQUISITE",
            "type_label": "Prerequisite Check",
            "title": "Foundation & Prerequisites",
            "description": f"Recommended preliminary mastery: {', '.join(prereq_names)}.",
            "items": prereq_names,
            "video_url": f"https://www.youtube.com/results?search_query={urllib.parse.quote_plus(query)}",
            "video_id": course_video_id,
            "required_watch_pct": 80,
        })
        step_counter += 1

    # 2. Subtopic Milestones
    subtopics = course_data.get("subtopics", [])
    for idx, subtopic in enumerate(subtopics, 1):
        query = f"{course_data.get('name')} {subtopic} tutorial"
        milestones.append({
            "step": step_counter,
            "id": f"step-{step_counter}",
            "type": "SUBTOPIC",
            "type_label": f"Module {idx}",
            "title": subtopic,
            "description": f"Detailed exploration and mastery of {subtopic}.",
            "items": [],
            "video_url": f"https://www.youtube.com/results?search_query={urllib.parse.quote_plus(query)}",
            "video_id": course_video_id,
            "required_watch_pct": 80,
        })
        step_counter += 1

    # 3. Capstone Project Milestone
    project_desc = course_data.get("project", "")
    if project_desc:
        query = f"{course_data.get('name')} capstone project tutorial build and deploy"
        milestones.append({
            "step": step_counter,
            "id": f"step-{step_counter}",
            "type": "PROJECT",
            "type_label": "Capstone Project",
            "title": "Hands-On Capstone Project",
            "description": project_desc,
            "items": ["Requirements Analysis", "Implementation", "Testing & Verification", "Portfolio Showcase"],
            "video_url": f"https://www.youtube.com/results?search_query={urllib.parse.quote_plus(query)}",
            "video_id": course_video_id,
            "required_watch_pct": 80,
        })

    return {
        "slug": matched_slug,
        "name": course_data.get("name", clean_name),
        "track": course_data.get("track", "General Track"),
        "level": course_data.get("level", "INTERMEDIATE"),
        "stage": course_data.get("stage", "CORE"),
        "milestones": milestones,
        "total_milestones": len(milestones),
        "project": course_data.get("project", ""),
        "youtube_links": yt_links,
        "course_video_id": course_video_id,
    }


def parse_student_skills(skills_string):
    """
    Parses comma-separated skills without breaking on commas inside parentheses.
    """
    if not skills_string:
        return []
    items = re.split(r',\s*(?![^()]*\))', skills_string.strip())
    return [s.strip() for s in items if s.strip()]
