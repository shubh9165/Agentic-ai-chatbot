from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tool():
    "return a list of tools"

    tools=[TavilySearchResults(max_results=2)]

    return tools

def create_tool_node(tools):
    "it create the tool node"

    return ToolNode(tools)