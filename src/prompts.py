
from langchain import PromptTemplate

journalism_role = 'You are a journalism professor, critical thinker and expert on logical fallacies'

logical_fallacies_template = """
    {role}
    Name every logical fallacy that can be found in this text: {text}.
    For each of them provide the section of the text, the name of the found fallacy, 
    and explain the context leading up to an explanation on why this is a logical fallacy in the current context.'
"""
    
FALLACIES_PROMPT = PromptTemplate(
    input_variables = ['role', 'text'],
    template = logical_fallacies_template
)