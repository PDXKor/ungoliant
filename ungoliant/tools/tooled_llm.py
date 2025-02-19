from langgraph.prebuilt import ToolNode, tools_condition
import ungoliant.helpers.polygon as polygon
import ungoliant.helpers.dates as dates
from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv 


pgc = polygon.PolygonClient()


def get_tools():
    tools = [pgc.get_open_close, pgc.get_financials, dates.get_current_date]
    return tools


def get_llm_with_tools():
    tools = get_tools()
    llm = ChatOpenAI(model_name="gpt-4o-mini")
    llm = llm.bind_tools(tools)
    return llm   

