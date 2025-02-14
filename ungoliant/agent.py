
import graph as gp
import json 
from langchain_core.messages import AIMessage


def format_messages(messages):
    formatted = []
    for message in messages:
        formatted.append({
            "content": message.content,
            "tool_calls": message.additional_kwargs.get("tool_calls", None),
            "response_metadata": message.response_metadata,
            "id": message.id
        })
    return formatted


def stream_graph_updates(user_input: str):
    graph = gp.get_graph()
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)


def single_answer(user_input: str, verbose: bool = False):
    graph = gp.get_graph(plot_graph=False)
    response = graph.invoke({"messages": [{"role": "user", "content": user_input}]})
    
    return_message = response['messages'][-1].content
    
    if verbose:
        messages = [message for message in response['messages']]#if isinstance(message, AIMessage)]
        formatted_messages = json.dumps(format_messages(messages), indent=4)
        return_message = f'-----MESSAGES-----:\n\n {formatted_messages}:\n\n-----ANSWER-----:\n\n {return_message}'

    return return_message


if __name__ == "__main__":
    print(single_answer("What was the closing price of Apple on February 7th 2025?",verbose=True))
    #print(single_answer("What was the change in the price of Apple from the begining of 2025 to Feb 7th?"))
    #print(single_answer("What was the average price of Apple for January 2025?"))


