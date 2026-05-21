from src.langgraphagenticaiui.states.state import GraphState

class basic_graph_node:
    def __init__(self,model):
        self.llm=model

    def process(self,state:GraphState):
        "generate the response of following question"

        return {"messages":self.llm.invoke(state["messages"])}

