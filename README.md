_Note: This documentation was generated using OpenAI's ChatGPT, an advanced language model capable of generating human-like text._

# Concept Explainer

Concept Explainer is a project that leverages the OpenAI API via Langchain to explain complex concepts in simple terms, making them more accessible to a wider audience. Langchain is a Python library that simplifies the process of chaining together language models. The system generates a conversation where a specialist explains a concept to a specific target audience. The output is formatted in Markdown and written to a file.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Console Interface](#console-interface)
  - [Web Interface](#web-interface)
- [Implementation Notes](#implementation-notes)
- [Markdown Reader](#markdown-reader)
- [Model Configuration](#model-configuration)
- [LLM Provider Configuration](#llm-provider-configuration)

## Installation

To install Concept Explainer, clone the repository and install the required dependencies with pip. Note that you need Python version 3.6 or later to run this project.

```bash
git clone https://github.com/klauseduard/concept-explainer.git
cd concept-explainer
pip install -r requirements.txt
```

Also, you need to create a .env file in the root of the project with your OpenAI API key. Replace `yourapikey` with your actual OpenAI API key:

```bash
echo "OPENAI_API_KEY=yourapikey" > .env
```

## Usage

### Console Interface

You can run Concept Explainer from the command line using the `explain.py` script. The command line interface takes three required arguments: the concept to explain, the specialist's role, and the target audience. An additional context can be provided as an optional argument.

Here is the basic command format:

```bash
python explain.py <concept> <specialist_role> <target_audience> --additional_context <context>
```

Here is an example usage:

```bash
python explain.py "black holes" "astrophysicist" "five-year-old" --additional_context "Assume that the five-year-old knows what stars are."
```

This will print the generated chat in the console and write it to a markdown file in the `saved_concepts` directory.

### Web Interface

You can run the web interface using the `web_interface.py` script:

```bash
python web_interface.py
```

After running the script, open your web browser and navigate to `http://localhost:5000`.

In the form, you can enter the concept you want to explain, the specialist's role, the target audience, and any additional context. Click the 'Submit' button to generate the explanation. The result will be displayed on the page and also written to a Markdown file.

You can also view all saved concept explanations by navigating to `http://localhost:5000/concepts`. Clicking on a concept will show its explanation.

## Implementation Notes

`explain.py` is the main script that parses command-line arguments and runs the chat generation function `generate_chat` from `chat_generator.py`. The chat is generated based on the provided arguments.

`chat_generator.py` implements `generate_chat` function which uses the Langchain library for language model chaining with the OpenAI API. It formulates a user request based on the provided concept, specialist role, and target audience, and passes it to the language model. The function also handles error scenarios, in case the chat generation fails. The result of the chat generation is formatted as a Markdown text.

`generate_chat` also includes a mechanism to save the generated chat to a markdown file with a filename based on the concept and the current timestamp, using the `write_to_file` function.

The `web_interface.py` script handles different routes and uses the same `generate_chat` function from `chat_generator.py` to generate the chat content.

The main route (`/`) allows users to input the details through a form and displays the generated chat. It supports both GET and POST methods. For GET requests, it uses default values for the concept, specialist role, and target audience, which can be customized. For POST requests, it uses the values submitted in the form.

The `/concepts` route displays a list of all saved concept explanations. The `/concepts/<concept>` route displays the explanation for a specific concept. It reads the content from the respective Markdown file, modifies hyperlinks to work with the web interface, and renders the content with mistune's Markdown parser.

`web_interface.py` also includes error handling if the requested concept is not found.

While the project is designed to be straightforward to use, developers looking to extend the codebase should have a solid understanding of Python, argparse for argument parsing, and have familiarity with the OpenAI API and the Langchain library.

Any

changes to the chat generation logic should be made in the `generate_chat` function in `chat_generator.py`. This function utilizes OpenAI's GPT-3 model for text generation. It's configured to use a temperature of 0.7, which determines the randomness of the model's output (lower values make the output more deterministic, while higher values make it more random).

## Markdown Reader

If you want to read the generated Markdown files, you can use the `md_reader.py` script. The script takes the path of a Markdown file as a command-line argument and prints the content of the file in the console.

Here is the basic command format:

```bash
python md_reader.py <file_path>
```

Here is an example usage:

```bash
python md_reader.py "saved_concepts/black_holes_2023-07-10-15-30-00.md"
```

This command will print the content of the specified Markdown file in the console.

## Model Configuration

The application supports different OpenAI models and settings through environment variables:

### Available Models

Configure the model using `OPENAI_MODEL` in your `.env` file:

- `gpt-3.5-turbo` (default) - Good balance of performance and cost
- `gpt-3.5-turbo-0125` - Latest GPT-3.5 version with improvements
- `gpt-4` - Higher quality but more expensive
- `gpt-4-0125` - Latest GPT-4 version with improvements

Example:
```bash
OPENAI_MODEL=gpt-4
```

### Temperature Setting

Control the randomness of responses using `OPENAI_TEMPERATURE` in your `.env` file:

- Range: 0.0 to 2.0
- Default: 0.2
- Lower values (e.g., 0.2) = More focused, consistent responses
- Higher values (e.g., 0.8) = More creative, varied responses

Example:
```bash
OPENAI_TEMPERATURE=0.5
```

### Cost Considerations

Different models have different pricing:
- GPT-3.5 models are more cost-effective
- GPT-4 models provide higher quality but at higher cost

Please review OpenAI's pricing at: https://openai.com/pricing

## LLM Provider Configuration

The application supports two LLM providers:
1. OpenAI (cloud-based, requires API key)
2. Ollama (local execution, free, works offline)

### OpenAI Provider

To use OpenAI's API (default provider):

1. Set up your OpenAI account and get an API key
2. Configure your .env file:
```bash
LLM_PROVIDER=openai
OPENAI_API_KEY=your-api-key-here
OPENAI_MODEL=gpt-3.5-turbo     # or other supported model
OPENAI_TEMPERATURE=0.2         # 0.0 to 2.0
```

Available OpenAI models:
- `gpt-3.5-turbo` (default) - Good balance of performance and cost
- `gpt-3.5-turbo-0125` - Latest GPT-3.5 version with improvements
- `gpt-4` - Higher quality but more expensive
- `gpt-4-0125` - Latest GPT-4 version with improvements

### Ollama Provider

To use Ollama (local execution):

1. Install Ollama from https://ollama.ai
2. Pull the desired model:
```bash
ollama pull mistral-small    # or other model like llama2, codellama, etc.
```
3. Configure your .env file:
```bash
LLM_PROVIDER=ollama
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=mistral-small    # or other installed model
OLLAMA_TEMPERATURE=0.2       # 0.0 to 2.0
```

Recommended Ollama models:
- `mistral-small` - Fast, efficient, good quality
- `llama2` - Strong general performance
- `codellama` - Excellent for technical concepts
- `neural-chat` - Good conversational abilities

Benefits of using Ollama:
- Free to use
- Complete privacy - all data stays local
- Works offline
- No API key required
- Lower latency
- Customizable models

### Temperature Setting

For both providers, the temperature setting controls response creativity:
- Range: 0.0 to 2.0
- Lower values (e.g., 0.2) = More focused, consistent responses
- Higher values (e.g., 0.8) = More creative, varied responses

Example for more creative responses:
```bash
# OpenAI
OPENAI_TEMPERATURE=0.8

# Ollama
OLLAMA_TEMPERATURE=0.8
```

### Provider Comparison

| Feature | OpenAI | Ollama |
|---------|--------|---------|
| Cost | Pay per use | Free |
| Privacy | Data sent to cloud | All data stays local |
| Internet Required | Yes | No |
| API Key Required | Yes | No |
| Response Speed | Network dependent | Local hardware dependent |
| Model Quality | Very high | Good |
| Resource Usage | Cloud-based | Uses local CPU/GPU |

## License

MIT

## Contact

Klaus-Eduard Runnel - klaus.eduard@gmail.com

Project Link: [https://github.com/klauseduard/concept-explainer](https://github.com/klauseduard/concept-explainer)
