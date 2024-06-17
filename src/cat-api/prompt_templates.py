# Current working version utilising JSONOutputParser
ANALYSIS_TEMPLATE = """
    Identify all text sections relevant to these categories: {categories}.
    Create a JSON object containing a list of identified 'sections' with the key 'sections'.
    Each 'section' is in the format: {format_instructions}
    If none of the given categories are clearly identifiable in the text, return an empty object.
    Text: {text}
"""

# This previous one was the first try
    # Problems:
        # Not 100% consistent
        # Included newline characters, tabs, etc which were hard to remove
        # Responses broke off in the middle of the JSON string
PROMPT_TEMPLATE = """
    {role}
    Identify sections relevant to these categories: {categories}.
    For each section found, extract the most relevant text for identification.
    Identify a suitable 'sub-category' that specifies a subtype or aspect within the category.
    Briefly explain why this section fits the identified sub-category.
    State the 'category' that best describes the section.
    Format the response in JSON with the keys "section", "sub-category", "explanation", "category" wrapped within the "sections" key.
    If none of the given categories are clearly identifiable in the text, return an empty JSON object.
    
    Text:
    {text}
"""