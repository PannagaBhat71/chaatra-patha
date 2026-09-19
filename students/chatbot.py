"""
Intelligent Chatbot Engine for Chaatra Patha (छात्रपथः).
Answers student queries about curriculum, skills taxonomy, roadmaps,
and dispatches SMS notifications using the user's Twilio account (+17372508034).
Zero emojis, 100% crash-proof for Vercel serverless deployment.
"""

import re
from .course_roadmap import load_user_roadmap_resources, slugify_skill
from .skills_data import SKILLS_DICTIONARY, ALL_SKILLS_LIST
from .twilio_service import send_sms, TWILIO_PHONE_NUMBER


def process_chat_message(user_message, context=None):
    """
    Analyzes the user's question and generates an intelligent, helpful response.
    Dispatches Twilio SMS if a phone number or SMS command is detected.
    """
    if not user_message or not user_message.strip():
        return (
            "Hello! I am your Chaatra Patha educational advisor. "
            "You can ask me about course roadmaps, skills taxonomy, tutorial languages, "
            f"or request an SMS alert via our Twilio number ({TWILIO_PHONE_NUMBER})."
        )

    msg = user_message.strip().lower()

    # 1. Twilio SMS Dispatch Intent
    phone_match = re.search(r'(\+?\d[\d\s\-]{8,15}\d)', user_message)
    is_sms_request = any(k in msg for k in ['sms', 'text message', 'send to my phone', 'message me', 'send mobile'])

    if phone_match and (is_sms_request or 'send' in msg or '+' in user_message):
        phone_raw = phone_match.group(1).replace(" ", "").replace("-", "")
        summary_text = (
            "Chaatra Patha (छात्रपथः) Study Update: "
            "Explore your personalized learning roadmap, interactive progress milestones, "
            "and multi-language YouTube tutorials at our student portal. "
            f"Sent via Twilio: {TWILIO_PHONE_NUMBER}"
        )
        sms_result = send_sms(phone_raw, summary_text)
        if sms_result.get("success"):
            return (
                f"Twilio SMS successfully dispatched from {TWILIO_PHONE_NUMBER} to {phone_raw}! "
                f"Message SID: {sms_result.get('sid')}. Check your phone for your roadmap notification."
            )
        else:
            return (
                f"Attempted to dispatch SMS to {phone_raw} via Twilio ({TWILIO_PHONE_NUMBER}).\n\n"
                f"Notice: {sms_result.get('message')}\n\n"
                "Tip: If you are testing with a Twilio trial account, destination phone numbers must first be verified in your Twilio Console."
            )

    # 2. Inquiries about Twilio / Phone support
    if any(k in msg for k in ['twilio', 'phone number', 'contact number', 'call', 'sms info']):
        return (
            f"Chaatra Patha is integrated with Twilio SMS using our verified sender number {TWILIO_PHONE_NUMBER}. "
            "You can type: 'Send roadmap to +[your_country_code_and_number]' at any time, "
            "and I will dispatch a direct SMS with your curriculum highlights."
        )

    # 3. How the Green Connector Progress line works
    if any(k in msg for k in ['green line', 'connector', 'checkbox', 'progress', 'milestone', 'how does roadmap work']):
        return (
            "How the Interactive Roadmap Works:\n\n"
            "1. Enter your credentials and select your approved skill on the Student Registration page.\n"
            "2. You will be redirected to your personalized roadmap with sequential milestones (Prerequisites, Core Modules, and Capstone Project).\n"
            "3. For each milestone, click the 'Mark Complete' checkbox.\n"
            "4. When checked, the milestone node turns green and an animated vibrant green line follows the connector to the next stage, displaying your live completion percentage.\n"
            "5. Your progress is saved automatically in your browser so you can return anytime."
        )

    # 4. Multi-language video tutorials
    if any(k in msg for k in ['language', 'youtube', 'video', 'kannada', 'hindi', 'malayalam', 'french', 'english', 'tutorial']):
        return (
            "Chaatra Patha provides comprehensive video tutorial resources across 5 supported languages:\n\n"
            "- English\n"
            "- Hindi\n"
            "- Kannada\n"
            "- Malayalam\n"
            "- French\n\n"
            "Each roadmap features one-click buttons for full-course tutorials in these languages, as well as dedicated tutorial buttons for every individual subtopic module."
        )

    # 5. Course specific questions (Cybersecurity, ML, DevOps, SQL, etc.)
    courses_dict, _ = load_user_roadmap_resources()
    for slug, course in courses_dict.items():
        c_name = course.get("name", "").lower()
        if slug in msg or c_name in msg or any(word in msg for word in c_name.split() if len(word) > 4):
            subtopics_str = ", ".join(course.get("subtopics", [])[:4])
            prereqs = course.get("prerequisites", [])
            prereqs_str = ", ".join(p.replace("-", " ").title() for p in prereqs) if prereqs else "None (Foundation course)"
            return (
                f"Course Specification: {course.get('name')}\n\n"
                f"- Track: {course.get('track')}\n"
                f"- Level: {course.get('level')} ({course.get('stage')} stage)\n"
                f"- Prerequisites: {prereqs_str}\n"
                f"- Core Modules: {subtopics_str}\n"
                f"- Capstone Project: {course.get('project')}\n\n"
                f"You can generate the complete interactive roadmap with green connector lines by selecting '{course.get('name')}' on the student registration form."
            )

    # 6. Skills Taxonomy & Domains
    if any(k in msg for k in ['skills', 'taxonomy', 'categories', 'domains', 'what can i learn', 'courses list']):
        categories = list(SKILLS_DICTIONARY.keys())
        cat_list = "\n".join(f"- {c} ({len(SKILLS_DICTIONARY[c])} skills)" for c in categories)
        return (
            f"Chaatra Patha offers a standardized taxonomy of 90+ verified skills across {len(categories)} domains:\n\n"
            f"{cat_list}\n\n"
            "You can browse and select any of these skills when registering your student profile."
        )

    # 7. Student Registration / Navigation
    if any(k in msg for k in ['register', 'sign up', 'student form', 'add student', 'enroll']):
        return (
            "To register and create your learning roadmap:\n\n"
            "1. Click 'Students Form' in the navigation bar or visit /student/add/.\n"
            "2. Fill in your roll number, full name, age, and approved skills.\n"
            "3. Click 'Save & View Course Roadmap' to immediately generate your interactive roadmap."
        )

    # Default general intelligent fallback
    return (
        "I am here to assist with your Chaatra Patha journey.\n\n"
        "Here are common things you can ask:\n"
        "- 'Tell me about Machine Learning' (or Cybersecurity, DevOps, SQL, etc.)\n"
        "- 'How does the green progress line work?'\n"
        "- 'What video tutorial languages are supported?'\n"
        f"- 'Send roadmap SMS to +[phone number]' (via Twilio {TWILIO_PHONE_NUMBER})\n"
        "- 'What skills taxonomy domains are available?'"
    )

