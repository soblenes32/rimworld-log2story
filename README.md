# rimworld-log2story

## Overview

This repository is a small experiment for turning Rimworld gameplay logs into a
novella. The workflow will rely on Jupyter notebooks and a large language model
to automatically generate a narrative from the collected logs.

## Getting Started

1. Install Python 3.8 or newer.
2. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Launch Jupyter and open the provided notebook:

```bash
jupyter notebook
```

You can then step through the notebook to parse logs, feed them to the LLM, and
produce story text.

## Loading Log Files

The project includes a small helper module for reading log files. Example usage:

```python
from src import log_loader

content = log_loader.load_output_log('/path/to/RimWorld_data')
player = log_loader.load_player_log('/path/to/RimWorld_data')
```

Any log path can be supplied to `load_log()` if you need to load custom files.

## Choosing the OpenAI Model

The helper function ``complete_prompt`` accepts a ``model`` parameter so you can
control which OpenAI model generates the story. It defaults to ``gpt-4.1`` but
can be overridden if you wish to use a different engine:

```python
from src import complete_prompt

text = complete_prompt("your-api-key", "Once upon a time...", model="gpt-3.5")
```

## Project Status

This is an early prototype intended to explore approaches for generating longer
form text from gameplay logs. Contributions and suggestions are welcome!
