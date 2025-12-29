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
2. Create a `.env` file in the project root directory with your token:

```
HF_TOKEN=your_huggingface_token
```

**Note:** Make sure the `.env` file is in the same directory as `app.py`.

**Alternative - Set as environment variable:**

**For Linux/Mac:**
```bash
export HF_TOKEN="your_huggingface_token"
```

**For Windows (PowerShell):**
```powershell
$env:HF_TOKEN="your_huggingface_token"
```

**For Windows (CMD):**
```cmd
set HF_TOKEN=your_huggingface_token
```

### Step 3: Run the Application

```bash
python app.py
```

The application will start and open in your browser at `http://127.0.0.1:7860` (or another port if 7860 is busy).

## How It Works

1. User pastes code into the Gradio interface
2. Code is split line by line
3. Each line is sent to the HuggingFace API using DeepSeek-R1 model
4. The model returns a simple explanation for each line
5. Results are displayed in the output textbox

## Usage

1. Paste your code into the input box
2. Click "Submit" or press Enter
3. View the line-by-line explanations in the output box

## Notes

- Empty lines are skipped in the explanation
- The app handles errors gracefully
- Make sure your HF_TOKEN is set in the `.env` file before running the app locally
- If you encounter API endpoint errors, you may need to check HuggingFace documentation for the correct OpenAI-compatible endpoint URL
- The `.env` file is automatically ignored by Git (see `.gitignore`)

## Deploying to HuggingFace Spaces

If you're deploying this to HuggingFace Spaces:

1. **Set the HF_TOKEN as a Secret (REQUIRED):**
   - Go to your Space settings (click the gear icon ⚙️ in your Space)
   - Navigate to the **"Variables and secrets"** tab
   - Click **"New secret"**
   - **Name:** `HF_TOKEN` (exactly as shown, case-sensitive)
   - **Value:** Your HuggingFace API token (get it from [HuggingFace tokens](https://huggingface.co/settings/tokens))
   - Click **"Add secret"**
   - The app will automatically use this environment variable

2. **The README.md already includes the required configuration** for HuggingFace Spaces (see the YAML frontmatter at the top)

3. **Important:** The app will load successfully even without the token, but you'll see a helpful error message when you try to use it if the token is not set.

