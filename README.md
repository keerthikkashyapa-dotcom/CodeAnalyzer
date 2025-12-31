---
title: Code Line-by-Line Explainer
emoji: 💻
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
---

# Code Line-by-Line Explainer

A Gradio web application that explains code line by line using HuggingFace's DeepSeek-R1 model.

## Features

- Line-by-line code explanation
- Syntax highlighting for code input
- Simple and intuitive web interface
- Uses HuggingFace's OpenAI-compatible API

## Setup

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install gradio openai
```

### Step 2: Get Your HuggingFace API Token

1. Go to [HuggingFace tokens](https://huggingface.co/settings/tokens) and generate an API token.
2. You'll enter this token directly in the web interface when using the app.

### Step 3: Run the Application

```bash
python app.py
```

The application will start and display a URL in your terminal (e.g., `http://127.0.0.1:7860`). Gradio will automatically use the next available port if the default port 7860 is already in use. Open the URL shown in your terminal in your browser.

## How It Works

1. User pastes code into the Gradio interface
2. Code is split line by line
3. Each line is sent to the HuggingFace API using DeepSeek-R1 model
4. The model returns a simple explanation for each line
5. Results are displayed in the output textbox

## Usage

1. Enter your HuggingFace API token in the "HuggingFace API Token" field (the token is masked for security)
2. Paste your code into the code input box
3. Click "Submit" or press Enter
4. View the line-by-line explanations in the output box

**Note:** Your API token is only used for the API calls and is not stored anywhere.

## Notes

- Empty lines are skipped in the explanation
- The app handles errors gracefully
- No need to set up environment variables or `.env` files - just enter your API token in the UI
- Your API token is entered securely (password field) and only used for API calls
- If you encounter API endpoint errors, check HuggingFace documentation for the correct endpoint URL

## Deploying to HuggingFace Spaces

1. **The README.md already includes the required configuration** for HuggingFace Spaces (see the YAML frontmatter at the top)
2. **No secrets needed!** Users can enter their own HuggingFace API tokens directly in the web interface
3. Simply push your code to a HuggingFace Space and it will work immediately

