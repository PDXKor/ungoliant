from typing import Annotated

from typing_extensions import TypedDict

from ungoliant.tools import polygon_tools as pt
from ungoliant.helpers import plot_graph as pg

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

from langchain_openai import ChatOpenAI  
from dotenv import load_dotenv




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

# create a graph object with a state object. 
graph_builder = StateGraph(State)

# create the LLM object which will be invoked by one or many nodes.
llm = ChatOpenAI(model_name="gpt-4") 

# an example of alling the llm directly, it won't know the answer to this question
ai_msg = llm.invoke("What was the closing price of Apple on January 5th 2024?")

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()

pg.plot_graph(graph)

def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)

while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        stream_graph_updates(user_input)
    except:
        # fallback if input() is not available
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        stream_graph_updates(user_input)
        break