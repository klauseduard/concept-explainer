#!/usr/bin/env python3

import datetime
import os
from rich.markdown import Markdown
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

def check_api_key():
    """
    Check if OpenAI API key is properly configured.
    Returns a tuple of (is_configured: bool, message: str)
    """
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        message = """Error: OpenAI API key not found!

To use this application, you need an OpenAI API key. Here's how to set it up:

1. Sign up for an OpenAI account at https://platform.openai.com/signup
2. Create an API key at https://platform.openai.com/api-keys
3. Copy the .env.example file to .env: cp .env.example .env
4. Add your API key to the .env file: OPENAI_API_KEY=your-key-here

Note: Using OpenAI's API incurs costs. Please review their pricing at:
https://openai.com/pricing

For more information, see our documentation at:
https://github.com/klauseduard/concept-explainer#getting-started"""
        return False, message
    
    if api_key.startswith('sk-') is False:
        message = """Error: Invalid OpenAI API key format!

The API key in your .env file doesn't appear to be valid. OpenAI API keys should:
- Start with 'sk-'
- Be about 51 characters long
- Contain letters, numbers, and hyphens

Please check your API key and try again."""
        return False, message
    
    return True, None

def generate_chat(concept, specialist_role, target_audience, additional_context=None):
    """
    Generate a chat using the provided concept.
    """
    # Check API key before attempting to use it
    is_configured, error_message = check_api_key()
    if not is_configured:
        print(error_message)
        return None

    user_request = f"""
    Explain the concept of {concept} in terms so simple a {target_audience} would understand.
    {additional_context if additional_context else ""}
    Invent follow-up questions the {target_audience} would ask and try to answer them.
    Provide one or more examples if possible.
    After answering the follow-up questions and providing the examples, provide etymology and history of the term, and finally a summary.
    After providing the summary, provide a "See also" section containing related concepts that might help to understand the one discussed better. Format the concepts as hyperlinks in the form "?concept=related+concept&specialist_role={specialist_role}&target_audience={target_audience}"
    Format the text with Markdown syntax and apply line length limit of 80 characters.
    """

    try:
        chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)
        role_template = f"You are a sophisticated {specialist_role}."
        system_message_prompt = SystemMessagePromptTemplate.from_template(role_template)
        user_request_prompt = HumanMessagePromptTemplate.from_template(user_request)
        chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, user_request_prompt])
        result = chat.invoke(chat_prompt.format_messages(concept=concept)).content
        return result
    except Exception as e:
        print(f"Error during chat generation: {str(e)}")
        if "Rate limit" in str(e):
            print("\nNote: You've hit OpenAI's rate limit. Please wait a moment before trying again.")
        elif "Incorrect API key" in str(e):
            print("\nNote: Your API key appears to be incorrect. Please check it and try again.")
        elif "insufficient_quota" in str(e):
            print("\nNote: Your OpenAI account has insufficient quota. Please check your billing status.")
        return None

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


