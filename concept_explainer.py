#!/usr/bin/env python3

import datetime
import os
from rich.markdown import Markdown
from dotenv import load_dotenv
from llm_providers import get_llm_provider

# List of supported models
SUPPORTED_MODELS = [
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-0125",
    "gpt-4",
    "gpt-4-0125"
]

def check_configuration():
    """
    Check if the LLM provider is properly configured.
    Returns a tuple of (is_configured: bool, message: str)
    """
    load_dotenv()
    
    provider = get_llm_provider()
    if not provider:
        message = """Error: Invalid LLM provider specified!

Please check your .env file and specify a valid provider:
LLM_PROVIDER=openai  # or ollama"""
        return False, message
    
    return provider.check_configuration()

def generate_chat(concept, specialist_role, target_audience, additional_context=None):
    """
    Generate a chat using the provided concept.
    """
    # Check configuration before attempting to use it
    is_configured, error_message = check_configuration()
    if not is_configured:
        print(error_message)
        return None

    provider = get_llm_provider()
    if not provider:
        print("Error: Could not initialize LLM provider")
        return None

    return provider.generate_chat(concept, specialist_role, target_audience, additional_context)

def write_to_file(concept, content):
    """
    Write the content to a file named based on the concept and current timestamp.
    """
    if not content:
        return None
        
    current_time = datetime.datetime.now().isoformat().replace(':', '').replace('-', '')
    formatted_concept = concept.replace(' ', '_')
    
    # Ensure the saved_concepts directory exists
    os.makedirs('saved_concepts', exist_ok=True)
    
    filename = f"saved_concepts/{current_time}_{formatted_concept}.md"
    
    try:
        with open(filename, 'w') as f:
            f.write(content)
        return filename
    except Exception as e:
        print(f"Error writing to file: {e}")
        return None


