
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

# look up supervisor architecture: https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/#create-agent-supervisor

class State(TypedDict):
    messages: Annotated[list, add_messages]

pgc = polygon.PolygonClient()

tools = [pgc.get_open_close]
llm = ChatOpenAI(model_name="gpt-4o-mini")
llm = llm.bind_tools(tools)   

def chatbot(state: State):
    message = {"messages": [llm.invoke(state["messages"])]}
    #print(state['messages'])
    return message

# create a graph object with a state object. 
graph_builder = StateGraph(State)

# add the chatbot node
graph_builder.add_node("chatbot", chatbot)

# the tool node is responsible for calling the tool recommended by the llm
tool_node = ToolNode(tools=tools)

#add the tool node
graph_builder.add_node("tools", tool_node)

# A new node that curates a final answer using tool output (if any)
def curate_response(state: State):
    # Append an instruction so the LLM knows to combine the info
    state["messages"].append({
        "role": "assistant",
        "content": "Using the above data, please provide a final, curated answer."
    })
    final_response = llm.invoke(state["messages"])
    return {"messages": [final_response]}

# Add the new curating node
graph_builder.add_node("curate", curate_response)

# define edges
graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "curate")
graph_builder.add_edge("curate", END)
graph_builder.add_edge(START, "chatbot")

graph = graph_builder.compile()

# function that will call the graph with input
def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            #print(value)
            print("Assistant:", value["messages"][-1].content)

if __name__ == "__main__":
    #stream_graph_updates("What is today's date?")
    #stream_graph_updates("What is the largest state by land mass in the United States?")
    stream_graph_updates("What was the closing price of Apple on February 7th 2025?")
    #stream_graph_updates("Can you get me the closing price of Apple on the date closest to today?")
    #stream_graph_updates("Can you get me the most recent closing price of the top five largest companies in the S&P 500?")
