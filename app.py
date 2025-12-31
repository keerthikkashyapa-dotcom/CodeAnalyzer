import gradio as gr
from openai import OpenAI

def explain_code(api_key: str, code: str):
    """
    Explains code line by line using HuggingFace DeepSeek-R1 model
    """
    # Check if API key is provided
    if not api_key or not api_key.strip():
        return (
            "❌ Error: Please enter your HuggingFace API token.\n\n"
            "Get your token from: https://huggingface.co/settings/tokens\n\n"
            "Enter it in the 'HuggingFace API Token' field above."
        )
    
    if not code or not code.strip():
        return "Please enter some code to explain."
    
    # Initialize OpenAI client with user-provided API key
    try:
        client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=api_key.strip()
        )
    except Exception as e:
        return f"❌ Error initializing API client: {str(e)}"
    
    lines = code.split("\n")
    explanations = []

    for i, line in enumerate(lines, start=1):
        if not line.strip():  # Skip empty lines
            explanations.append(f"Line {i}: (empty line)\n")
            continue
            
        prompt = f"Explain this line of code in simple terms:\n{line}"
        try:
            completion = client.chat.completions.create(
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
                explanations.append(f"Line {i}: {line}\nExplanation: Error - Invalid API token. Please check your HuggingFace API token.\n")
            elif "404" in error_msg or "Not Found" in error_msg:
                explanations.append(f"Line {i}: {line}\nExplanation: Error - Model or endpoint not found. Please check the model name and API endpoint.\n")
            else:
                explanations.append(f"Line {i}: {line}\nExplanation: Error - {error_msg}\n")
    
    return "\n".join(explanations)

# Gradio interface
iface = gr.Interface(
    fn=explain_code,
    inputs=[
        gr.Textbox(
            label="HuggingFace API Token",
            type="password",
            placeholder="Enter your HuggingFace API token (get it from https://huggingface.co/settings/tokens)",
            info="Your token will be kept secure and only used for API calls"
        ),
        gr.Code(
            language="python",
            lines=10,
            label="Code Input"
        ),
    ],
    outputs=gr.Textbox(
        lines=20,
        placeholder="Code explanations will appear here...",
        label="Line-by-Line Explanation"
    ),
    title="Code Line-by-Line Explainer",
    description="Enter your HuggingFace API token and code to get a line-by-line explanation using DeepSeek-R1 model.",
    examples=None
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)

