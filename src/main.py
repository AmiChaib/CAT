import streamlit as st
from openai import OpenAI
import json

from config import OPENAI_API_KEY, CUSTOM_CSS
from categories import CATEGORY_OPTIONS

# function to detect logical fallacies with the use of the prompts. It then processes the response to extract and return the identified fallacies and the modified text with highlights.
def detect_logical_fallacies(text):
    # initializing the OpenAI API key
    client = OpenAI(
        api_key=OPENAI_API_KEY
    )
    model = "gpt-4-1106-preview"
    response_format = {"type": "json_object"} # format should b a JSON object
    messages = [
        {"role": "system", "content": "Your task is to analyze the provided text and identify any logical fallacies present. Logical fallacies are errors in reasoning that can include 'Strawman', 'False Dilemma', 'Slippery Slope', 'Ad Hominem', 'Appeal to Ignorance', and others."},
        {"role": "system", "content": "First, focus on identifying the fallacies. If you find a logical fallacy, name the type of fallacy you have identified."},
        {"role": "system", "content": "Then, modify the text by highlighting the specific part where the fallacy occurs. Use HTML styling for the highlight, applying a background color with a corner radius of 5px. For example, highlight a 'False Dilemma' fallacy in pink. Provide the modified text as a JSON object containing the HTML-formatted string that visually indicates the parts of the text containing the logical fallacies."},
        {"role": "user", "content": text}
    ]

    # sending the request to the API
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            response_format=response_format,
            temperature=0.3,
        )

        # extracting the logical fallacy and modified text from the response
        if response.choices:
            response_json = json.loads(response.choices[0].message.content)
            modified_html_text = response_json.get("text", "")
            logical_fallacy = response_json.get("logical_fallacy", "No fallacy detected") 
            return logical_fallacy, modified_html_text
        else:
            return "Error", "No choices available in the response"

    # handling exceptions, if there are, it will return an error message
    except Exception as e:
        print(e)
        return "Error", str(e)

def main():
    st.title("Hello World")
    # adding the custom CSS into the Streamlit app
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    st.title("Critical Analysis Tool")
    st.markdown("Input your text and click submit to analyze it.")

    user_input = st.text_area("Enter your text:", height=300)

    # putting the checkboxes into columns, so that 2 will be below each other
    col1, col2, col3, col4 = st.columns(4)
    col1.checkbox("hello")
    col1.checkbox("hello1")
    col2.checkbox("hello2")
    col2.checkbox("hello3")
    col3.checkbox("hello4")
    col3.checkbox("hello5")
    submit_button = col4.button("Submit")

    # Convert the set to a list
    logical_fallacies = sorted(list(CATEGORY_OPTIONS))

    # When the submit button is clicked
    if submit_button:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        # Create three columns for the logical fallacies
        col1, col2, col3 = st.columns(3)

        # Place two logical fallacies in each column with highlight
        for i in range(6):
            current_col = [col1, col2, col3][i % 3]
            current_col.markdown(f'<p class="highlight" id="highlight{i}">{logical_fallacies[i]}</p>', unsafe_allow_html=True)
        
        # Detect logical fallacies and display results
        logical_fallacy, highlighted_text = detect_logical_fallacies(user_input)
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown(f"Logical Fallacy Detected: {logical_fallacy}", unsafe_allow_html=True)
        st.markdown(highlighted_text, unsafe_allow_html=True)

if __name__ == "__main__":
    main()


#  CSS for adding highlights and some additional styling





# Streamlit app layout
