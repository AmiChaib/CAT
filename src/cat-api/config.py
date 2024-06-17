
# The OpenAI API key must be set in a .env file containing the API key:
# OPENAI_API_KEY="<<key>>"

import dotenv
from os import environ

env_file = './.env'
dotenv.load_dotenv(env_file, override=True)
OPENAI_API_KEY = environ.get('OPENAI_API_KEY')