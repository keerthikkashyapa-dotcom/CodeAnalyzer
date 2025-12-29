import os
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

# Get HuggingFace API token
# For HuggingFace Spaces: Set HF_TOKEN as a secret in Space settings
# For local development: Create a .env file with HF_TOKEN=your_token
hf_token = os.getenv("HF_TOKEN")

# Initialize client variable (will be set when needed)
client = None

def get_client():
    """Initialize and return the OpenAI client with HuggingFace API"""
    global client
    if client is None:
        # This should never be called if hf_token is None, but check anyway
        if not hf_token:
            return None
        client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=hf_token
        )
    return client

def explain_code(code: str):
    """
    Explains code line by line using HuggingFace DeepSeek-R1 model
    """
    if not code.strip():
        return "Please enter some code to explain."
    
    # Check if token is set
    if not hf_token:
        return (
            "❌ Error: HF_TOKEN is not set.\n\n"
            "For HuggingFace Spaces:\n"
            "1. Go to your Space settings (click the gear icon)\n"
            "2. Navigate to 'Variables and secrets' tab\n"
            "3. Click 'New secret'\n"
            "4. Name: HF_TOKEN\n"
            "5. Value: your_huggingface_api_token\n"
            "6. Click 'Add secret'\n\n"
            "For local development:\n"
            "Create a .env file with: HF_TOKEN=your_huggingface_token"
        )
    
    lines = code.split("\n")
    explanations = []

    for i, line in enumerate(lines, start=1):
        if not line.strip():  # Skip empty lines
            explanations.append(f"Line {i}: (empty line)\n")
            continue
            
        prompt = f"Explain this line of code in simple terms:\n{line}"
        try:
            api_client = get_client()
            if api_client is None:
                explanations.append(f"Line {i}: {line}\nExplanation: Error - API client not initialized. Please set HF_TOKEN.\n")
                continue
            completion = api_client.chat.completions.create(
                model="deepseek-ai/DeepSeek-R1",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                timeout=30.0
            )
            explanation = completion.choices[0].message.content
            explanations.append(f"Line {i}: {line}\nExplanation: {explanation}\n")
        except Exception as e:
            error_msg = str(e)
            # Provide more helpful error messages
            if "401" in error_msg or "Unauthorized" in error_msg:
                explanations.append(f"Line {i}: {line}\nExplanation: Error - Invalid API token. Please check your HF_TOKEN in .env file.\n")
            elif "404" in error_msg or "Not Found" in error_msg:
                explanations.append(f"Line {i}: {line}\nExplanation: Error - Model or endpoint not found. Please check the model name and API endpoint.\n")
            else:
                explanations.append(f"Line {i}: {line}\nExplanation: Error - {error_msg}\n")
    
    return "\n".join(explanations)

# Gradio interface
iface = gr.Interface(
    fn=explain_code,
    inputs=gr.Code(
        language="python",
        lines=10,
        label="Code Input"
    ),
    outputs=gr.Textbox(
        lines=20,
        placeholder="Code explanations will appear here...",
        label="Line-by-Line Explanation"
    ),
    title="Code Line-by-Line Explainer",
    description="Enter code and get a line-by-line explanation using HuggingFace DeepSeek-R1 model.",
    examples=[
        ["def hello():\n    print('Hello, World!')"],
        ["x = 5\ny = 10\nresult = x + y"],
    ]
)

if __name__ == "__main__":
    iface.launch()

