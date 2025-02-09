'''
Basic idea: 
- xyz

Potential Questions:
- What is a stocks % change over x period. 
- What are the metrics like pe ratio of a stock. 
- Which stocks last week had the greatest change. 
   - Start with S&P 500

'''


from typing import Annotated

from typing_extensions import TypedDict

from ungoliant.tools.tooled_llm import polygon_tools as pt
from ungoliant.helpers import dates
from ungoliant.helpers import plot_graph as pg

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

from langchain_openai import ChatOpenAI  
from dotenv import load_dotenv

import json
from langchain_core.messages import ToolMessage

from langgraph.prebuilt import ToolNode, tools_condition

# look up supervisor architecture: https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/#create-agent-supervisor

'''
State is the way that we manage what has been in the chat bot, and what
is currently in process. We can customize this object, but it should essentially
manage an update to keys based on actions within the program. Those 
updates can then be used when figuring out what should be done next. 
'''
class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]

tools = [pt.close_price_tool, dates.get_current_date]
llm = ChatOpenAI(model_name="gpt-4o-mini")
llm = llm.bind_tools(tools)   

def chatbot(state: State):
    message = {"messages": [llm.invoke(state["messages"])]}
    #print(message)
    print(state['messages'])
    return message

# create a graph object with a state object. 
graph_builder = StateGraph(State)

# add the chatbot node
graph_builder.add_node("chatbot", chatbot)

# create a tool node
#tool_node = BasicToolNode(tools=[pt.close_price_tool])
# the tool node is responsible for calling the tooPl recommended by the llm
tool_node = ToolNode(tools=tools)

#add the tool node
graph_builder.add_node("tools", tool_node)

# The `tools_condition` function returns "tools" if the chatbot asks to use a tool, and "END" if
# it is fine directly responding. This conditional routing defines the main agent loop.
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition
)

# Any time a tool is called, we return to the chatbot to decide the next step
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")
graph = graph_builder.compile()

# function that will call the graph with input
def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)

if __name__ == "__main__":
    #stream_graph_updates("What was the closing price of Apple on January 5th 2024?")
    #stream_graph_updates("Can you get me the closing price of Apple on the date closest to today?")
    stream_graph_updates("Can you get me the most recent closing price of the top five largest companies in the S&P 500?")


# while True:
#     try:
#         user_input = input("User: ")
#         if user_input.lower() in ["quit", "exit", "q"]:
#             print("Goodbye!")
#             break

#         stream_graph_updates(user_input)
#     except:
#         # fallback if input() is not available
#         user_input = "What do you know about LangGraph?"
#         print("User: " + user_input)
#         stream_graph_updates(user_input)
#         break
