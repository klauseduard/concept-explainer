#!/usr/bin/env python3

import argparse
from rich.markdown import Markdown
from rich import print

# Command-line argument parser
parser = argparse.ArgumentParser(description='Render a Markdown file.')
parser.add_argument('filename', type=str, help='The name of the Markdown file to render.')
args = parser.parse_args()

# Open the file and read its content
with open(args.filename, 'r') as file:
    content = file.read()

# Print the formatted content of the file
print(Markdown(content))
