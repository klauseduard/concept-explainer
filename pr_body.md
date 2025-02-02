# Web Interface Search Initialization Issue

Fixes #12

## Problem
The web interface requires pre-built search indices (`embeddings.npy`, `indices.json`, and `hashes.json`) to function properly, but these files are not automatically generated. Currently, users need to manually run `search_semantic.py` before starting the web interface, which is not documented and leads to errors.

## Proposed Solution
1. Modify `web_interface.py` to automatically initialize search indices if they don't exist
2. Add proper error handling and user feedback during initialization
3. Update documentation to explain the search index generation process

## Implementation Plan
1. Move the index building logic to a shared module
2. Add initialization check in web interface startup
3. Show proper progress/status messages during initialization
4. Add graceful fallback if search dependencies are not installed

## Testing
- Test web interface startup with and without existing indices
- Verify search functionality after auto-initialization
- Test error handling for various edge cases

Closes #6\n\n## Changes Made\n- Added Ollama as an alternative LLM provider\n- Created abstraction layer for LLM providers with `LLMProvider` abstract base class\n- Implemented `OllamaProvider` with chat functionality\n- Added environment variables for model configuration:\n  - `LLM_PROVIDER` to select provider (openai/ollama)\n  - `OLLAMA_HOST`, `OLLAMA_MODEL`, `OLLAMA_TEMPERATURE` for Ollama settings\n- Updated documentation with:\n  - Installation and setup instructions for Ollama\n  - Configuration options and examples\n  - Provider comparison table\n  - Best practices for performance\n\n## Testing Done\n- [x] Tested with OpenAI provider (existing functionality)\n- [x] Tested with Ollama provider using mistral-small model\n- [x] Verified configuration validation\n- [x] Checked error handling\n- [x] Validated markdown formatting and output\n\n## Benefits\n- Users now have a free, offline option for running the tool\n- Privacy-focused option as all data stays local\n- No API key required for Ollama\n- Flexible model selection based on user needs
