from src.langgraphagenticaiui.states.state import GraphState

class Graph_builder_with_tool:

    def __init__(self,model):
        self.llm=model

    def assistent(self,tools):


        llm_with_tools=self.llm.bind_tools(tools)

        def create_chat_bot(state:GraphState):
            "Generate the response of the user query"

            return {"messages":[llm_with_tools.invoke(state["messages"])]}
        
        return create_chat_bot
        