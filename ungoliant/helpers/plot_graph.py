from IPython.display import Image, display

def plot_graph(graph, output_path="output_graph.png"):
    """
    Plots a graph and saves the output to a PNG file.

    Args:
        graph: The graph object to plot.
        output_path (str): The file path to save the PNG image.
    """
    from IPython.display import Image, display

    try:
        # Get the PNG data from the graph
        png_data = graph.get_graph().draw_mermaid_png()
        
        # Save the PNG data to the specified output path
        with open(output_path, "wb") as f:
            f.write(png_data)
        
        # Optionally display the image in an interactive environment
        display(Image(output_path))
        
        print(f"Graph saved to: {output_path}")
    except Exception as e:
        print(f"Error generating or saving the graph: {e}")
