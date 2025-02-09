
import graph as gp

def stream_graph_updates(user_input: str):
    graph = gp.get_graph()
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            #print(value)
            print("Assistant:", value["messages"][-1].content)

def single_answer(user_input: str):
    graph = gp.get_graph(plot_graph=False)
    response = graph.invoke({"messages": [{"role": "user", "content": user_input}]})
    return response["messages"][-1].content

if __name__ == "__main__":
    print(single_answer("What was the closing price of Apple on February 7th 2025?"))
    #print(single_answer("What was the change in the price of Apple from the begining of 2025 to Feb 7th?"))
    #print(single_answer("What was the average price of Apple for January 2025?"))


