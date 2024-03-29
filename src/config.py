import dotenv
from os import environ

env_file = './.env'
dotenv.load_dotenv(env_file, override=True)
OPENAI_API_KEY = environ.get('OPENAI_API_KEY')

CATEGORY_OPTIONS = {"option 1", "option 2", "option 3", "option 4", "option 5", "option 6"}

CUSTOM_CSS = """
<style>
    
    img{
       width: 100px;
       height: 100px;
       margin-left: 27.5%;
       border-radius: 50%; 
       object-fit: cover;
    }
    
    .highlight {
        display: flex;
        justify-content: center;
        width: 112px;
        margin: auto;
        border-radius: 8px;
        margin-bottom: 14px;
    }
    #highlight0 {
        background-color: #A9B6FB;
    }
    #highlight1 {
        background-color: #B6F187; 
    }
    #highlight2 {
        background-color: #D9B5F6;  
    }
    #highlight3 {
        background-color: #F6E173; 
    }
    #highlight4 {
        background-color: #ECAA2B;  
    }
    #highlight5 {
        background-color: #F7748C;
    }

</style>
"""