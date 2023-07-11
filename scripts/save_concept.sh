#!/bin/bash

# Function to display usage of the script
usage() {
  echo "Usage: $0 [-r] filename1 filename2 ..." 1>&2
  echo "Purpose: This script moves the files with specific name patterns to a 'saved_concepts' subdirectory."
  echo "These are reviewed outputs from a chatbot-based concept explainer program."
  echo "The files in this directory can then be used to list pre-saved concept explanations."
  echo "Option: -r Removes the original files after moving."
  exit 1
}

# Initialize our own variables
remove=0

# Parse command-line arguments
while getopts "r" opt; do
  case $opt in
    r)
      # If the -r flag is set, the original files will be removed after being moved
      remove=1
      ;;
    \?)
      usage
      ;;
  esac
done
shift $((OPTIND-1))

# Check if at least one filename has been provided
if [ -z "$1" ]; then
    usage
fi

# Process each input file
for file in "$@"; do
    # Check if the file exists
    if [ ! -f "$file" ]; then
        echo "File $file not found!"
        continue
    fi

    # Extract the filename
    filename=$(basename -- "$file")

    # Get the name after the last underscore
    new_filename="${filename#*_}"

    # Create the subdirectory if it doesn't exist
    mkdir -p saved_concepts

    # Copy the file to the subdirectory with the new name
    cp "$file" "saved_concepts/$new_filename"

    echo "File has been copied and renamed successfully!"
    echo "New file: saved_concepts/$new_filename"

    # Remove the original file if the -r option was specified
    if [ $remove -eq 1 ]; then
        rm "$file"
        echo "Original file $file has been removed!"
    fi
done

