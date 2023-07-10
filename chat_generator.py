#!/usr/bin/env python3

import datetime
from rich.markdown import Markdown
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from dotenv import load_dotenv


def generate_chat(concept, specialist_role, target_audience, additional_context=None):
    """
    Generate a chat using the provided concept.
    """

    user_request = f"""
    Explain the concept of {concept} in terms so simple a {target_audience} would understand.
    {additional_context if additional_context else ""}
    Invent follow-up questions the {target_audience} would ask and try to answer them.
    Provide one or more examples if possible.
    After answering the follow-up questions and providing the examples, provide a summary.
    After providing the summary, provide a "See also" section containing related concepts that might help to understand the one discussed better. Format the concepts as hyperlinks in the form "?concept=related+concept&specialist_role={specialist_role}&target_audience={target_audience}"
    Format the text with Markdown syntax and apply line length limit of 80 characters.
    """

    load_dotenv() # take environment variables (api key) from .env

    chat = ChatOpenAI(temperature=0.2)

    role_template = f"You are a sophisticated {specialist_role}."
    system_message_prompt = SystemMessagePromptTemplate.from_template(role_template)
    user_request_prompt = HumanMessagePromptTemplate.from_template(user_request)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, user_request_prompt])

    chain = LLMChain(llm=chat, prompt=chat_prompt)

    try:
        result = chain.run(concept=concept)
    except Exception as e:
        print(f"Error during chat generation: {e}")
        return None

    return result

def write_to_file(concept, content):
    """
    Write the content to a file named based on the concept and current timestamp.
    """
    current_time = datetime.datetime.now().isoformat().replace(':', '').replace('-', '')
    formatted_concept = concept.replace(' ', '_')
    filename = f"{current_time}_{formatted_concept}.md"
    
    try:
        with open(filename, 'w') as f:
            f.write(content)
    except Exception as e:
        print(f"Error writing to file: {e}")

