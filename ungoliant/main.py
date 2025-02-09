#!/usr/bin/env python3
"""
ungoliant.py

A retro-styled command line tool for querying graph data,
inspired by Ungoliant (/ʊŋˈɡoʊliənt/), the dark and ancient spider
from Tolkien's legendarium.
"""

import sys
import graph as gp
import agent as ag

def print_banner():
    
    spider_art = r"""
                                       / \
                                      / _ \
                                    \_\(_)/_/
                                     _//"\\_  
                                      /   \

    """
    width = 80

    title = "UNGOLIANT (/ʊŋˈɡoʊliənt/)"
    blurb = (
        "Inspired by Ungoliant, the dark and ancient spider of Middle-earth,\n"
        "whose insatiable hunger consumed every glimmer of light and knowledge, \n"
        "this tool scours an immense web of stock market data to devour your queries \n"
        "and reveal hidden insights. Embrace the hunger for truth and let Ungoliant feed \n"
        "your relentless curiosity. Type 'exit' or 'quit' to leave.\n"
    )
    
    border = "=" * 80
    separator = "-" * 80

    print(border)
    print(spider_art.center(80))
    print(title.center(80))
    print(separator)
    for line in blurb.splitlines():
        print(line.center(80))
    print(border)
    print("\n")

def main():
    """Main interactive loop for the command line interface."""
    print_banner()
    print("Type your query below. (Type 'exit' or 'quit' to exit)\n")
    
    while True:
        try:
            user_input = input(">> ").strip()
            if user_input.lower() in {"exit", "quit"}:
                print("\nExiting Ungoliant. Farewell!")
                break
            if not user_input:
                continue
            
            answer = ag.single_answer(user_input)
            print("\nAssistant: " + answer + "\n")
        
        except KeyboardInterrupt:
            print("\n\nInterrupted by user. Exiting Ungoliant. Goodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}\n")


if __name__ == "__main__":
    main()
