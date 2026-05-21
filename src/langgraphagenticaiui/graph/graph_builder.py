from src.langgraphagenticaiui.states.state import GraphState
from langgraph.graph import StateGraph,START,END
from src.langgraphagenticaiui.nodes.basic_graph_node import basic_graph_node
from src.langgraphagenticaiui.tools.search_tool import get_tool,create_tool_node
from langgraph.prebuilt import tools_condition
from src.langgraphagenticaiui.nodes.build_graph_node_with_tool import Graph_builder_with_tool

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
    
    def build_graph_chatbot_with_tool_workflow(self):
        try:
            tools=get_tool()
            tool_node=create_tool_node(tools)

            llm=self.model

            obj=Graph_builder_with_tool(llm)
            assistent_node=obj.assistent(tools)

            self.graph_builder.add_node("assistent",assistent_node)
            self.graph_builder.add_node("tools",tool_node)

            self.graph_builder.add_edge(START,"assistent")
            self.graph_builder.add_conditional_edges("assistent",
                tools_condition,
                #if the lastest message of assistent is tool call-> so tools_condition Routes to tools
                #if the lastest message of assistent is not tool call-> so tools_condition Routes to END
                )
            self.graph_builder.add_edge("tools","assistent")
            
        except Exception as e:
            raise ValueError(f"error is {e}")
        
    def setup_graph(self,usecase):

        if usecase=="basic chatbot":
            self.build_graph_workflow()
        if usecase=="chatbot with tool":
            self.build_graph_chatbot_with_tool_workflow()

        return self.graph_builder.compile()