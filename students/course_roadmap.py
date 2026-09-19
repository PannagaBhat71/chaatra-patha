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

# Curated content-specific YouTube video mapping for subtopics, prerequisites & capstone projects
SUBTOPIC_VIDEOS = {
    # Cybersecurity subtopics
    "security principles": "bPVaOlJ6ln0",
    "cia triad": "bPVaOlJ6ln0",
    "threat modeling": "k0v21K6kY0M",
    "authentication & iam": "SLwpqD_F1lA",
    "iam": "SLwpqD_F1lA",
    "network security": "kDEX1HXybrk",
    "firewalls": "kDEX1HXybrk",
    "app security": "2_lswM1S264",
    "owasp": "2_lswM1S264",
    "risk assessment": "P2MydR2UjI8",

    # Machine Learning subtopics
    "supervised learning": "ukzFI9rgwfU",
    "unsupervised learning": "Iqy77mQp56c",
    "clustering": "Iqy77mQp56c",
    "decision trees": "7VeUPuFG444",
    "random forests": "7VeUPuFG444",
    "model evaluation": "wpQi640oxpo",
    "overfitting": "DEMKGeyv5io",
    "scikit-learn": "0Lt9w-BxKFQ",

    # DevOps subtopics
    "devops culture": "scEDHsr3APg",
    "ci/cd": "R8_veQiYWrI",
    "jenkins": "R8_veQiYWrI",
    "github actions": "R8_veQiYWrI",
    "containerization": "fqMOX6JJhGo",
    "docker": "fqMOX6JJhGo",
    "orchestration": "X48VuDVv0do",
    "kubernetes": "X48VuDVv0do",
    "infrastructure as code": "7xngnjfIlK4",
    "terraform": "7xngnjfIlK4",
    "monitoring": "h4Sl21AKkDg",
    "prometheus": "h4Sl21AKkDg",

    # Mobile App Dev subtopics
    "mobile ui/ux": "yPt4y_z1x6E",
    "cross-platform": "VPvVD8t02U8",
    "flutter": "VPvVD8t02U8",
    "react native": "0-S5a0eXPoc",
    "navigation & routing": "Fv0xLq9g1uQ",
    "state management": "3tm-4Av7LVE",
    "consuming apis": "12tcxZ0x_dE",
    "app store deployment": "4jZf94r_Y5g",

    # QA & Testing subtopics
    "testing fundamentals": "sO8eGL6QVUw",
    "unit testing": "1Lfv5tUGsn8",
    "integration testing": "EZ05e7EMOL4",
    "writing test cases": "bJb9WfT4b_M",
    "test automation": "l2zXj5xK_7k",
    "selenium": "l2zXj5xK_7k",
    "bug reporting": "98qf_41GZps",
    "jira": "98qf_41GZps",

    # Blockchain subtopics
    "distributed ledgers": "gyMwXuJrbJQ",
    "hashing & cryptography": "b4b8ktEV4Bg",
    "consensus mechanisms": "k5pM6K4G7iA",
    "smart contracts": "M576WGiDBdQ",
    "solidity": "M576WGiDBdQ",
    "wallets & transactions": "nHhAEkG1y2U",
    "web3": "nHhAEkG1y2U",

    # IoT subtopics
    "iot architecture": "6mBO2vqLv38",
    "sensors & actuators": "8G8y-Q2H61M",
    "microcontrollers": "nL34z54G830",
    "arduino": "nL34z54G830",
    "raspberry pi": "nL34z54G830",
    "iot protocols": "EIxdz-2rhLs",
    "mqtt": "EIxdz-2rhLs",
    "edge computing": "lYm4r40y8eY",
    "iot security": "y3jW2X0q_90",

    # Prompt Engineering subtopics
    "llm architecture": "_ZvnD73m40o",
    "zero-shot": "jC4v5AS4RIM",
    "few-shot": "jC4v5AS4RIM",
    "chain of thought": "dQr4w7r8U4o",
    "system prompts": "BP46xO_h70E",
    "prompt injection": "v9n0o1643Z8",
    "output formatting": "1KSm0a3q2mI",

    # Server Maintenance & Software Architecture subtopics
    "server hardening": "kGY8e658y28",
    "patch management": "o4r5b0G_gZg",
    "log aggregation": "XmE7v-M_Zz8",
    "load balancing": "K0Ta65OqQk8",
    "high availability": "K0Ta65OqQk8",
    "disaster recovery": "7N_yE_eFj3k",
    "monolith vs microservices": "77flD_3F3kU",
    "microservices": "77flD_3F3kU",
    "event-driven architecture": "STKCRSUsyP0",
    "caching strategies": "oaJq1hkMXPU",
    "redis": "oaJq1hkMXPU",
    "database sharding": "5faMjKuB9bc",
    "system scalability": "xpPnAAAm07k",
    "design patterns": "tv-_1er1mWI",

    # Data & Analytics subtopics
    "sql basics": "HXV3zeRR3h4",
    "sql joins": "9yeOJ0ZMUYw",
    "relational database": "HXV3zeRR3h4",
    "data analysis": "r-uOLxNrNk8",
    "pandas": "vmEHCJofslg",
    "data cleaning": "r-uOLxNrNk8",
    "data visualization": "ztnT3_T-p4A",
    "tableau": "aHaOIvR00So",
    "power bi": "TmhQCQrsmv4",
    "statistical analysis": "xxpc-HPKN28",
    "hypothesis testing": "xxpc-HPKN28",
    "big data": "1vbXmCrkT3Y",
    "hadoop": "1vbXmCrkT3Y",
    "spark": "kZ_QJcW5540",
    "data engineering": "kZ_QJcW5540",
    "predictive modeling": "i_LwzRVP7bg",
    "business intelligence": "ztnT3_T-p4A",

    # Marketing, Sales & Finance subtopics
    "seo": "DvwS7cV9GmQ",
    "search engine optimization": "DvwS7cV9GmQ",
    "sem": "045k286E95g",
    "ppc": "045k286E95g",
    "content marketing": "x_0gT4S2_uY",
    "copywriting": "Xn_7U7c4tA0",
    "social media": "c8wS0s3eG74",
    "email marketing": "z8iE2y1Y3iI",
    "financial accounting": "yYX4bS44n3E",
    "budgeting": "yYX4bS44n3E",
    "inventory control": "yYX4bS44n3E",
    "supply chain": "yYX4bS44n3E",
}

# Domain educational pool ensuring every milestone receives a unique verified video ID
FALLBACK_UNIQUE_VIDEOS = [
    "rfscVS0vtbw", "7vhms8lq4aA", "Z1Yd7up3560", "G9SZa_rGZcI",
    "ukzFI9rgwfU", "Iqy77mQp56c", "7VeUPuFG444", "wpQi640oxpo",
    "fqMOX6JJhGo", "X48VuDVv0do", "7xngnjfIlK4", "h4Sl21AKkDg",
    "sO8eGL6QVUw", "1Lfv5tUGsn8", "EZ05e7EMOL4", "l2zXj5xK_7k",
    "bPVaOlJ6ln0", "k0v21K6kY0M", "SLwpqD_F1lA", "kDEX1HXybrk",
    "2_lswM1S264", "P2MydR2UjI8", "HXV3zeRR3h4", "9yeOJ0ZMUYw",
    "r-uOLxNrNk8", "ztnT3_T-p4A", "xxpc-HPKN28", "1vbXmCrkT3Y",
    "a_fA3Q_Z61Y", "8S0FDjFBj8o", "kJEs2ZfL7bQ", "p33CVuG8q2A",
]


def resolve_milestone_video(course_slug, milestone_type, title, step_index, used_video_ids):
    """
    Returns a distinct, topic-specific verified YouTube video ID for each milestone,
    guaranteeing that no two milestones in the same course roadmap display the same video.
    """
    low_title = title.lower()
    candidate_id = None

    # 1. Check direct topic keywords
    for keyword, vid_id in SUBTOPIC_VIDEOS.items():
        if keyword in low_title:
            if vid_id not in used_video_ids:
                candidate_id = vid_id
                break

    # 2. Prerequisite video selection
    if not candidate_id and milestone_type == "PREREQUISITE":
        prereq_pool = ["7vhms8lq4aA", "Z1Yd7up3560", "G9SZa_rGZcI", "rfscVS0vtbw"]
        for pid in prereq_pool:
            if pid not in used_video_ids:
                candidate_id = pid
                break

    # 3. Capstone Project video selection
    if not candidate_id and milestone_type == "PROJECT":
        project_pool = ["a_fA3Q_Z61Y", "8S0FDjFBj8o", "kJEs2ZfL7bQ", "p33CVuG8q2A"]
        for pjid in project_pool:
            if pjid not in used_video_ids:
                candidate_id = pjid
                break

    # 4. Check course primary video if not yet used
    if not candidate_id:
        c_video = COURSE_VIDEO_IDS.get(course_slug)
        if c_video and c_video not in used_video_ids:
            candidate_id = c_video

    # 5. Deterministic unique fallback from educational pool
    if not candidate_id:
        offset = (abs(hash(f"{course_slug}-{title}")) + step_index) % len(FALLBACK_UNIQUE_VIDEOS)
        for i in range(len(FALLBACK_UNIQUE_VIDEOS)):
            cand = FALLBACK_UNIQUE_VIDEOS[(offset + i) % len(FALLBACK_UNIQUE_VIDEOS)]
            if cand not in used_video_ids:
                candidate_id = cand
                break

    if not candidate_id:
        candidate_id = FALLBACK_UNIQUE_VIDEOS[step_index % len(FALLBACK_UNIQUE_VIDEOS)]

    used_video_ids.add(candidate_id)
    return candidate_id


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
    used_video_ids = set()

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
        prereq_video_id = resolve_milestone_video(
            matched_slug, "PREREQUISITE", "Foundation & Prerequisites", step_counter, used_video_ids
        )
        milestones.append({
            "step": step_counter,
            "id": f"step-{step_counter}",
            "type": "PREREQUISITE",
            "type_label": "Prerequisite Check",
            "title": "Foundation & Prerequisites",
            "description": f"Recommended preliminary mastery: {', '.join(prereq_names)}.",
            "items": prereq_names,
            "video_url": f"https://www.youtube.com/results?search_query={urllib.parse.quote_plus(query)}",
            "video_id": prereq_video_id,
            "required_study_seconds": 3600,
            "required_study_hours": 1,
        })
        step_counter += 1

    # 2. Subtopic Milestones
    subtopics = course_data.get("subtopics", [])
    for idx, subtopic in enumerate(subtopics, 1):
        query = f"{course_data.get('name')} {subtopic} tutorial"
        subtopic_video_id = resolve_milestone_video(
            matched_slug, "SUBTOPIC", subtopic, step_counter, used_video_ids
        )
        milestones.append({
            "step": step_counter,
            "id": f"step-{step_counter}",
            "type": "SUBTOPIC",
            "type_label": f"Module {idx}",
            "title": subtopic,
            "description": f"Detailed exploration and mastery of {subtopic}.",
            "items": [],
            "video_url": f"https://www.youtube.com/results?search_query={urllib.parse.quote_plus(query)}",
            "video_id": subtopic_video_id,
            "required_study_seconds": 3600,
            "required_study_hours": 1,
        })
        step_counter += 1

    # 3. Capstone Project Milestone
    project_desc = course_data.get("project", "")
    if project_desc:
        query = f"{course_data.get('name')} capstone project tutorial build and deploy"
        project_video_id = resolve_milestone_video(
            matched_slug, "PROJECT", "Hands-On Capstone Project", step_counter, used_video_ids
        )
        milestones.append({
            "step": step_counter,
            "id": f"step-{step_counter}",
            "type": "PROJECT",
            "type_label": "Capstone Project",
            "title": "Hands-On Capstone Project",
            "description": project_desc,
            "items": ["Requirements Analysis", "Implementation", "Testing & Verification", "Portfolio Showcase"],
            "video_url": f"https://www.youtube.com/results?search_query={urllib.parse.quote_plus(query)}",
            "video_id": project_video_id,
            "required_study_seconds": 3600,
            "required_study_hours": 1,
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
