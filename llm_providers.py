#!/usr/bin/env python3

from abc import ABC, abstractmethod
import os
from typing import Optional
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
import ollama

class LLMProvider(ABC):
    """Abstract base class for LLM providers."""
    
    @abstractmethod
    def generate_chat(self, concept: str, specialist_role: str, target_audience: str, additional_context: Optional[str] = None) -> Optional[str]:
        """Generate a chat explaining a concept."""
        pass

    @abstractmethod
    def check_configuration(self) -> tuple[bool, Optional[str]]:
        """Check if the provider is properly configured."""
        pass

class OpenAIProvider(LLMProvider):
    """OpenAI implementation of LLM provider."""
    
    SUPPORTED_MODELS = [
        "gpt-3.5-turbo",
        "gpt-3.5-turbo-0125",
        "gpt-4",
        "gpt-4-0125"
    ]
    
    def check_configuration(self) -> tuple[bool, Optional[str]]:
        """Check if OpenAI configuration is valid."""
        api_key = os.getenv('OPENAI_API_KEY')
        model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
        temp_str = os.getenv('OPENAI_TEMPERATURE', '0.2')
        
        # Check API key
        if not api_key:
            return False, "OpenAI API key not found in environment variables."
        if not api_key.startswith('sk-'):
            return False, "Invalid OpenAI API key format."
            
        # Check model
        if model not in self.SUPPORTED_MODELS:
            return False, f"Unsupported OpenAI model. Must be one of: {', '.join(self.SUPPORTED_MODELS)}"
            
        # Check temperature
        try:
            temp = float(temp_str)
            if not 0.0 <= temp <= 2.0:
                return False, "Temperature must be between 0.0 and 2.0"
        except ValueError:
            return False, "Invalid temperature value"
            
        return True, None

    def generate_chat(self, concept: str, specialist_role: str, target_audience: str, additional_context: Optional[str] = None) -> Optional[str]:
        """Generate a chat using OpenAI."""
        try:
            model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
            temperature = float(os.getenv('OPENAI_TEMPERATURE', '0.2'))
            
            chat = ChatOpenAI(model=model, temperature=temperature)
            role_template = f"You are a sophisticated {specialist_role}."
            system_message_prompt = SystemMessagePromptTemplate.from_template(role_template)
            
            user_request = f"""
            Explain the concept of {concept} in terms so simple a {target_audience} would understand.
            {additional_context if additional_context else ""}
            Invent follow-up questions the {target_audience} would ask and try to answer them.
            Provide one or more examples if possible.
            After answering the follow-up questions and providing the examples, provide etymology and history of the term, and finally a summary.
            After providing the summary, provide a "See also" section containing related concepts that might help to understand the one discussed better.
            Format the text with Markdown syntax and apply line length limit of 80 characters.
            """
            
            user_request_prompt = HumanMessagePromptTemplate.from_template(user_request)
            chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, user_request_prompt])
            result = chat.invoke(chat_prompt.format_messages(concept=concept)).content
            return result
            
        except Exception as e:
            print(f"Error during OpenAI chat generation: {str(e)}")
            return None

class OllamaProvider(LLMProvider):
    """Ollama implementation of LLM provider."""
    
    def check_configuration(self) -> tuple[bool, Optional[str]]:
        """Check if Ollama configuration is valid."""
        host = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
        model = os.getenv('OLLAMA_MODEL', 'mistral-small')
        temp_str = os.getenv('OLLAMA_TEMPERATURE', '0.2')
        
        # Check host
        if not host:
            return False, "Ollama host not configured."
            
        # Check model (we can't validate available models without making an API call)
        if not model:
            return False, "Ollama model not configured."
            
        # Check temperature
        try:
            temp = float(temp_str)
            if not 0.0 <= temp <= 2.0:
                return False, "Temperature must be between 0.0 and 2.0"
        except ValueError:
            return False, "Invalid temperature value"
            
        return True, None

    def generate_chat(self, concept: str, specialist_role: str, target_audience: str, additional_context: Optional[str] = None) -> Optional[str]:
        """Generate a chat using Ollama."""
        try:
            host = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
            model = os.getenv('OLLAMA_MODEL', 'mistral-small')
            temperature = float(os.getenv('OLLAMA_TEMPERATURE', '0.2'))
            
            client = ollama.Client(host=host)
            
            system_prompt = f"You are a sophisticated {specialist_role}."
            user_prompt = f"""
            Explain the concept of {concept} in terms so simple a {target_audience} would understand.
            {additional_context if additional_context else ""}
            Invent follow-up questions the {target_audience} would ask and try to answer them.
            Provide one or more examples if possible.
            After answering the follow-up questions and providing the examples, provide etymology and history of the term, and finally a summary.
            After providing the summary, provide a "See also" section containing related concepts that might help to understand the one discussed better.
            Format the text with Markdown syntax and apply line length limit of 80 characters.
            """
            
            full_prompt = f"{system_prompt}\n\n{user_prompt}"
            
            response = client.chat(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ],
                options={
                    "temperature": temperature
                }
            )
            
            return response['message']['content']
            
        except Exception as e:
            print(f"Error during Ollama chat generation: {str(e)}")
            return None

def get_llm_provider() -> Optional[LLMProvider]:
    """Factory function to get the configured LLM provider."""
    provider_type = os.getenv('LLM_PROVIDER', 'openai').lower()
    
    if provider_type == 'openai':
        return OpenAIProvider()
    elif provider_type == 'ollama':
        return OllamaProvider()
    else:
        print(f"Unsupported LLM provider: {provider_type}")
        return None 