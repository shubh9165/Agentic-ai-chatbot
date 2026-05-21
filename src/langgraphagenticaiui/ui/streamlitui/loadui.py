import streamlit as st
from src.langgraphagenticaiui.ui.uiconfigfiles import Config
import os

class LoadStreamlitUi:
    def __init__(self):
        self.config=Config()
        self.user_control={}

    def load_streamlit_ui(self):

        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.header(self.config.get_page_title())

        with st.sidebar:

            llm_options=self.config.get_llm_options()
            use_case_options=self.config.get_usecase()
            model_options=self.config.get_model_options()

            self.user_control["SELECTED_LLM"]=st.selectbox("Select llm",llm_options)

            if self.user_control["SELECTED_LLM"]=="Groq":

                self.user_control["SELECTED_MODEL"]=st.selectbox("Select model",model_options)

                self.user_control["GROQ_API_KEY"]=st.text_input("Groq_Api_key",type="password")
                st.session_state["GROQ_API_KEY"]=self.user_control["GROQ_API_KEY"]
            self.user_control["SELECTED_USE_CASE"]=st.selectbox("Use case",use_case_options)

            if self.user_control["SELECTED_USE_CASE"]=="chatbot with tool":
                self.user_control["TAVILY_API_KEY"]=st.text_input("Tavily_API_key",type="password")
                st.session_state["TAVILY_API_KEY"]=self.user_control["TAVILY_API_KEY"]
                os.environ["TAVILY_API_KEY"]=self.user_control["TAVILY_API_KEY"]

        
        return self.user_control