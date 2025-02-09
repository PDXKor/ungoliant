
from typing import Annotated
from typing_extensions import TypedDict

#from ungoliant.tools import polygon_tools as pt
import helpers.polygon as polygon
from ungoliant.helpers import dates
from ungoliant.helpers import plot_graph as pg

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI  
from dotenv import load_dotenv
from langchain_core.tools import BaseTool, StructuredTool
from pydantic import BaseModel, Field
import json
from langchain_core.messages import ToolMessage
from langgraph.prebuilt import ToolNode, tools_condition
import ungoliant.tools.tooled_llm as tooled_llm

# look up supervisor architecture: https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/#create-agent-supervisor

llm = tooled_llm.get_llm_with_tools() 

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    message = {"messages": [llm.invoke(state["messages"])]}
    return message

def curate_response(state: State):
    state["messages"].append({
        "role": "assistant",
        "content": "Using the above data, please provide a final, curated answer."
    })
    final_response = llm.invoke(state["messages"])
    return {"messages": [final_response]}

def get_graph(plot_graph=False):

    # create a graph object with a state object. 
    graph_builder = StateGraph(State)

    # add the chatbot node
    graph_builder.add_node("chatbot", chatbot)

    # the tool node is responsible for calling the tool recommended by the llm
    tool_node = ToolNode(tools=tooled_llm.get_tools())

    #add the tool node
    graph_builder.add_node("tools", tool_node)

    # Add the new curating node
    graph_builder.add_node("curate", curate_response)

    # define edges
    graph_builder.add_conditional_edges("chatbot", tools_condition)
    graph_builder.add_edge("tools", "curate")
    graph_builder.add_edge("curate", END)
    graph_builder.add_edge(START, "chatbot")

    graph = graph_builder.compile()

    if plot_graph:
        pg.plot_graph(graph)

    return graph