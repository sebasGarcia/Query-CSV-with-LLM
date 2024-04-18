from langchain_community.llms import Ollama
from langchain_experimental.agents import create_csv_agent 
from dotenv import load_dotenv
from streamlit_lottie import st_lottie
import streamlit as st
import requests

def load_lottieurl(url:str):
    """
    This function is used to show an animation on the webpage
    """
    r = requests.get(url)
    if r.status_code != 200:
        return None 

    return r.json()



def main():

    #execute the following in order to read the variables
    load_dotenv()
    # Setting the model, which in my case is mistral or llama2
    #MODEL = "llama2"
    MODEL = "mistral"
    model = Ollama(model=MODEL)

    st.set_page_config(page_title="Ask Questions to your CSV file 📈")
    st.header("Ask Questions to your CSV file 📈")
    # create a variable to load lottie animation using url
    lottie_animation = load_lottieurl("https://lottie.host/07d60a1d-f055-4a07-8afe-fd5b0c399fc7/WZ0wLUWuS1.json")
    # Show animation
    st_lottie(lottie_animation,
                                height=192,
                                width=192)
    user_csv = st.file_uploader("Upload your CSV file", type="csv")

    if user_csv is not None:
    
        user_question = st.text_input("QUESTION:","Ask a question about your csv file")
        
        llm = model

        agent = create_csv_agent(llm, 
                                 user_csv, 
                                 verbose=True,
                                 handle_parsing_errors="Check your output and make sure it conforms please. Do not output an action and a final answer at the same time.")

        if user_question is not None and user_question !="":

            response = agent.run(user_question)
            st.write(response)


if __name__ == "__main__":
    main()