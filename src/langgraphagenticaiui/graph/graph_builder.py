from src.langgraphagenticaiui.states.state import GraphState
from langgraph.graph import StateGraph,START,END
from src.langgraphagenticaiui.nodes.basic_graph_node import basic_graph_node
class GraphBuilder:
    def __init__(self,model):
        self.model=model
        self.graph_builder=StateGraph(GraphState)
    
    def build_graph_workflow(self):
        try:
            self.basic_graph_node=basic_graph_node(self.model)
            self.graph_builder.add_node("chatbot",self.basic_graph_node.process)
            self.graph_builder.add_edge(START,"chatbot")
            self.graph_builder.add_edge("chatbot",END)

        
        except Exception as e:
            raise ValueError(f"Graph not able to create due to {e}")
        
    def setup_graph(self,usecase):

        if usecase=="basic chatbot":
            self.build_graph_workflow()

        return self.graph_builder.compile()