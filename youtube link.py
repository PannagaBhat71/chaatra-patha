import urllib.parse

def get_youtube_links(skill_slug, data_dict=SKILLS_DICTIONARY):
    """
    Takes a skill slug from the database and returns a list of 5 automatically 
    generated YouTube Search URLs (one for each supported language), providing
    an immediate roadmap video resource for the student.
    """
    
    skill = data_dict.get(skill_slug)
    if not skill:
        return []
        
    course_name = skill.get("name")
    
    # Supported languages for Chaatra Patha
    languages = {
        "en": "English",
        "hi": "Hindi",
        "kn": "Kannada",
        "ml": "Malayalam",
        "fr": "French",
    }
    
    yt_resources = []
    
    for code, lang in languages.items():
        # Build the intelligent search query based on the roadmap structure
        query = f"{course_name} tutorial full course beginner to advanced in {lang}"
        
        # Safely encode the URL
        encoded_query = urllib.parse.quote_plus(query)
        search_url = f"https://www.youtube.com/results?search_query={encoded_query}"
        
        yt_resources.append({
            "language_code": code,
            "language_name": lang,
            "url": search_url,
            "type": "YOUTUBE_SEARCH"
        })
        
    return yt_resources

# Example Output for 'machine-learning':
# {
#   "language_name": "English",
#   "url": "https://www.youtube.com/results?search_query=Machine+Learning+Algorithms+tutorial+full+course+beginner+to+advanced+in+English"
# }