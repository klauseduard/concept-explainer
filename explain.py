#!/usr/bin/env python3

import argparse
from rich import print
from rich.markdown import Markdown
from chat_generator import generate_chat, write_to_file

def parse_args():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description='Explain a concept in simple terms.')
    parser.add_argument('concept', type=str, help='The concept to explain.')
    parser.add_argument('specialist_role', type=str, help='Role of the specialist in the conversation.')
    parser.add_argument('target_audience', type=str, help='Intended audience for the conversation.')
    parser.add_argument('--additional_context', type=str, help='Additional context for the conversation.')
    args = parser.parse_args()
    return args


def main():
    """
    Main function to run the script.
    """
    args = parse_args()

    if not args.concept or not args.specialist_role or not args.target_audience:
        print("The 'concept', 'specialist_role', and 'target_audience' arguments must be non-empty strings.")
        return

    chat_content = generate_chat(args.concept, args.specialist_role, args.target_audience, args.additional_context)

    if chat_content:
        print(Markdown(chat_content))
        write_to_file(args.concept, chat_content)

if __name__ == "__main__":
    main()

