#!/usr/bin/env python3
"""
ungoliant.py

A retro-styled command line tool for querying graph data,
inspired by Ungoliant (/ʊŋˈɡoʊliənt/), the dark and ancient spider
from Tolkien's legendarium.
"""

import sys
import ungoliant.graph as gp
import ungoliant.agent as ag
import argparse

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
        "\n\n An agentic graph based application for investment information.\n\n"+
        "Based on the Tolken's ancient spider who sought to consume all knowledge and light.\n\n"
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
    
    # Argument parsing
    parser = argparse.ArgumentParser(description="Ungoliant: A graph-based CLI tool.")
    parser.add_argument(
        '--verbose', 
        action='store_true', 
        help="Show's tool execution details."
    )
    args = parser.parse_args()
    
    # Set up logging based on verbosity flag
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
            
            answer = ag.single_answer(user_input, verbose=args.verbose)
            print("\nAssistant: " + answer + "\n")
        
        except KeyboardInterrupt:
            print("\n\nInterrupted by user. Exiting Ungoliant. Goodbye!")
            break
        
        except Exception as e:
            print(f"\nAn error occurred: {e}\n")


if __name__ == "__main__":
    main()
