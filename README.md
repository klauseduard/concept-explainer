# Concept Explainer

> A coding experiment from the early days of the LLM boom (2023), now updated with local LLM support.

This is a simple tool that uses LLMs to explain concepts through simulated conversations. Originally built with OpenAI's API during the initial ChatGPT excitement, it has now been updated to also work with Ollama for local, offline usage.

## What it does

Given a concept, a specialist role, and a target audience, it generates an explanation in a dialogue format. For example:
- Concept: "black holes"
- Specialist: "astrophysicist"
- Audience: "five-year-old"

The output is formatted in Markdown and includes:
- Basic explanation
- Follow-up questions and answers
- Examples where possible
- Brief etymology and history
- Related concepts

## Features

- Works with OpenAI API (original version) or Ollama (new in 2025)
- Command line and basic web interface
- Saves explanations as Markdown files
- Simple search functionality

## Installation

You need Python 3.6+ and either:
- An OpenAI API key, or
- Ollama installed locally (free, works offline)

```bash
git clone https://github.com/klauseduard/concept-explainer.git
cd concept-explainer
pip install -r requirements.txt
```

Configure your `.env` file:
```bash
# For OpenAI:
LLM_PROVIDER=openai
OPENAI_API_KEY=your-api-key-here
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_TEMPERATURE=0.2

# Or for Ollama:
LLM_PROVIDER=ollama
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=mistral-small
OLLAMA_TEMPERATURE=0.2
```

## Usage

### Console Interface

Basic command format:
```bash
python explain.py <concept> <specialist_role> <target_audience> --additional_context <context>
```

Example:
```bash
python explain.py "black holes" "astrophysicist" "five-year-old" --additional_context "Assume they know what stars are."
```

### Web Interface

Start the web interface:
```bash
python web_interface.py
```

Then open `http://localhost:5000` in your browser.

## Configuration

### OpenAI Provider (original)
- Requires API key
- Default model: `gpt-3.5-turbo`
- Also supports: `gpt-3.5-turbo-0125`, `gpt-4`, `gpt-4-0125`
- See pricing at: https://openai.com/pricing

### Ollama Provider (new)
- Free, runs locally
- Default model: `mistral-small`
- Also works with: `llama2`, `codellama`, `neural-chat`
- No API key needed
- Requires some CPU/GPU power

### Temperature Setting
- Range: 0.0 to 2.0 (default: 0.2)
- Lower = more focused
- Higher = more creative

## License

MIT

## Contact

Klaus-Eduard Runnel - klaus.eduard@gmail.com

Project Link: [https://github.com/klauseduard/concept-explainer](https://github.com/klauseduard/concept-explainer)