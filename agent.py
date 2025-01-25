from helpers import polygon as pg

# apple = pg.get_close_on_date("2021-01-04",ticker="AAPL")
# print(apple)

from typing import Annotated
from dotenv import load_dotenv
from typing_extensions import TypedDict
from langchain_openai import ChatOpenAI  
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.tools import BaseTool, StructuredTool
from pydantic import BaseModel, Field



class ClosePriceInput(BaseModel):
    ticker: str = Field(description="The stock symbol of the company to get close price for")
    date: str = Field(description="The date to get the close price for - the format must be YYYY-MM-DD")

def get_close_price(ticker, date):
    print('executing close price')
    data = pg.get_close_on_date(date, ticker=ticker)
    print(data)
    return data

print(get_close_price(ticker="AAPL", date="2024-01-05"))

close_price_tool = StructuredTool(name="get_close_price",
                                  args_schema=ClosePriceInput,
                                  description='Get the close price of a stock on a given date',
                                  func=get_close_price)

tools = [close_price_tool]

llm = ChatOpenAI(model_name="gpt-4")
llm = llm.bind_tools(tools)

ai_msg = llm.invoke("What was the closing price of Apple on January 5th 2024?")

for tool in ai_msg.tool_calls:
    tool_name = tool['name']
    args = tool['args']
    print(tool_name, args)
    func = [t for t in tools if t.name == tool_name][0].func(**args)
    print(func)
    #print(tool['args'])

# class State(TypedDict):
#     # Messages have the type "list". The `add_messages` function
#     # in the annotation defines how this state key should be updated
#     # (in this case, it appends messages to the list, rather than overwriting them)
#     messages: Annotated[list, add_messages]

# def chatbot(state: State):
#     return {"messages": [llm.invoke(state["messages"])]}

# graph_builder = StateGraph(State)
# graph_builder.add_node("chatbot", chatbot)
# graph_builder.add_edge(START, "chatbot")
# graph_builder.add_edge("chatbot", END)
# graph = graph_builder.compile()

# def stream_graph_updates(user_input: str):
#     for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
#         for value in event.values():
#             print("Assistant:", value["messages"][-1].content)

# #stream_graph_updates("What was the closing price of Apple on 1/05/2024?")