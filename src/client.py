from langchain import PromptTemplate
from langchain.chains import LLMChain

class Client():
    def __init__(self):
        pass
    
    def detect_logical_fallacies(self, llm, role, temp, input_text):     
        prompt = PromptTemplate(
            input_variables = ['role', 'text'],
            template = temp
        )
        chain = LLMChain(llm=llm, prompt=prompt)
        return chain.run({'role': role, 'text': input_text})