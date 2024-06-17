import re
from langchain.chains import LLMChain
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from classes import Section

class Client():
    def __init__(self):
        pass
    
    def stringify_array(self, array):
        if len(array) == 1:
            modified_array = array[0]
        else:
            modified_array = ", ".join(array[:-1]) + ", and " + array[-1]
        return modified_array
    
    def clean_text(self, text):
        cleaned_text = re.sub(r'[\n\t]', ' ', text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
        return cleaned_text
    
    def detect_categories(self, model, template, input_categories, input_text):
        categories = self.stringify_array(input_categories)   
        text = self.clean_text(input_text) 
        
        parser = JsonOutputParser(pydantic_object=Section)

        prompt = PromptTemplate(
            template = template,
            partial_variables={"format_instructions": parser.get_format_instructions()},
            input_variables=['categories', 'text'],
        )
        chain = prompt | model | parser
        try:
            result = chain.invoke({"categories": categories, "text": text})
        except Exception as e:
            print("\n\nException:\n{}".format(e))
            result = e
        return result