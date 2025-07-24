# AI Agent

## Setup

(Steps are from boot.dev ai agent course)

Setup the project with `uv`:

```bash
uv init boot-ai-agent
cd boot-ai-agent
```

Create a virtual environment:

```bash
uv venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Then add dependencies with `uv`. Example:

```bash
uv add google-genai==1.12.1
uv add python-dotenv==1.1.0
```

Run the project with `uv`:

```bash
uv run main.py
```
