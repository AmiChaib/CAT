import streamlit as st
from prompts.roles import roles
from langchain.llms import OpenAI
from container import container
from config import OPENAI_API_KEY, CUSTOM_CSS, CATEGORY_OPTIONS
from prompts.prompt_templates import FALLACIES_PROMPT_TEMPLATE, POLITICAL_INTENT_PROMPT_TEMPLATE, PROMPT_TEMPLATE
from exceptions.no_category_selected_exception import NoCategorySelectedException
from exceptions.no_text_provided_exception import NoTextProvidedException
from warning import warning

def get_prompt(is_log_fal, is_pol_int):
    if is_log_fal:
        return [FALLACIES_PROMPT_TEMPLATE, roles['logical fallacies']]
    elif is_pol_int:
        return [POLITICAL_INTENT_PROMPT_TEMPLATE, roles['political intent']]
    else:
        raise NoCategorySelectedException
    
# def process_results(results):
#     keys = ['identified_section', 'fallacy_name', 'identified_fallacy_explanation']

def main():
    # adding the custom CSS into the Streamlit app
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    st.title("Critical Analysis Tool")
    if warning.is_warning:
        st.warning(warning.content)
    st.markdown("Input your text and click submit to analyze it.")
    user_input = st.text_area("Enter your text:", height=300)

    # putting the checkboxes into columns, so that 2 will be below each other
    col1, col2, col3, col4 = st.columns(4)
    log_fal = col1.checkbox("Logical Fallacies")
    col1.checkbox("Category 2...")
    pol_int = col2.checkbox("Political Intent")
    col2.checkbox("Category 3...")
    col3.checkbox("Category 4...")
    col3.checkbox("Category 5...")
    submit_button = col4.button("Submit")

    # Convert the set to a list
    categories = sorted(list(CATEGORY_OPTIONS))

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
            current_col.markdown(f'<p class="highlight" id="highlight{i}">{categories[i]}</p>', unsafe_allow_html=True)
        
        # Detect logical fallacies and display results
        try:
            if user_input:
                warning.set_warning(False, None)
                try:
                    prompt = get_prompt(log_fal, pol_int)
                    template = prompt[0]
                    role = prompt[1]
                    model = OpenAI(model_name="gpt-3.5-turbo-instruct")
                    results = container.client.detect_logical_fallacies(model, role, template, user_input)
                    # processed_results = process_results(results)
                    with st.sidebar:
                        st.title("Explanation")
                        st.markdown(f"Logical Fallacy Detected: {results}", unsafe_allow_html=True)
                except NoCategorySelectedException as e:
                    warning.set_warning(True, e)                
            else:
                raise NoTextProvidedException
        except Exception as e:
            warning.set_warning(True, e)
            

        #st.markdown(highlighted_text, unsafe_allow_html=True)

if __name__ == "__main__":
    main()


#  CSS for adding highlights and some additional styling





# Streamlit app layout
