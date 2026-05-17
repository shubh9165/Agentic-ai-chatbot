import streamlit as st
import os
from langchain_groq import ChatGroq

class GroqLLM:

    def __init__(self,user_state_input):
        self.user_control=user_state_input
    
    def load_llm(self):
        try:
            api_key=self.user_control["GROQ_API_KEY"]
            selcted_model=self.user_control["SELECTED_MODEL"]

            llm=ChatGroq(model=selcted_model,groq_api_key=api_key)

            return llm
        except Exception as e:
            raise ValueError(f"The llm are not going to load due to {e}")