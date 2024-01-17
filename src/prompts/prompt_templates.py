FALLACIES_PROMPT_TEMPLATE = """
    {role}
    Name every part of the text that is considered a logical fallacy in this text: {text}.
    For each provide the section of the text, the name of the fallacy, and an explanation on why this is a logical fallacy.
"""

POLITICAL_INTENT_PROMPT_TEMPLATE = """
    {role}
    Name every part of the text that could be politically motivated in this text: {text}.
    For each provide the section of the text and an explanation on what the political intent is.
"""

PROMPT_TEMPLATE = """
    {role}
    Name every part of the text that is considered a logical fallacy in this text: {text}.
    For each provide the section of the text, the name of the fallacy, and an explanation on why this is a logical fallacy. 
    Return a dictionary with the keys 'identified_section', 'fallacy_name', and 'identified_fallacy_explanation' and provide the values accordingly.
"""