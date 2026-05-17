from src.langgraphagenticaiui.ui.streamlitui.loadui import LoadStreamlitUi
import streamlit as st
from src.langgraphagenticaiui.LLMS.GroqLLMS import GroqLLM
from src.langgraphagenticaiui.graph.graph_builder import GraphBuilder
from src.langgraphagenticaiui.ui.streamlitui.display_result import DisplayResultStreamlit
def load_agentic_app():

    """Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness."""

    ui=LoadStreamlitUi()
    user_input=ui.load_streamlit_ui()

    if user_input is None:
        st.warning("Streamlit ui are not loading")

    user_message=st.text_input("Enter your input text")

    if user_message:
        try:   
            obj_llm_config=GroqLLM(user_input)
            llm=obj_llm_config.load_llm()

            if llm is None:
                st.error("LLM are not loaded") 
            
            use_case=user_input["SELECTED_USE_CASE"]

            if use_case is None:
                st.error("error")

            graph_builder=GraphBuilder(llm)

            try:
                graph=graph_builder.setup_graph(use_case)
                DisplayResultStreamlit(use_case,graph,user_message).display_result_on_ui()

            except Exception as e:
                raise ValueError(f"the error is {e}")
            

        except Exception as e:
            raise ValueError(f"the error is {e}")
    

    