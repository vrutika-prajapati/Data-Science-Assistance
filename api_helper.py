import logging
import re
import subprocess
from mistralai import Mistral
from typing import List, Dict, Optional

def call_mistral_api(api_key: str, agent_id: str, history: List[Dict[str, str]]) -> Optional[str]:
    """
    Calls the Mistral API to generate a response based on the conversation history.
    """
    try:
        client = Mistral(api_key=api_key)
        response = client.chat(
            model="mistral-large-2402",  # or whichever version you're using
            messages=history,
        )
        # If the response is valid, return the bot's reply
        if hasattr(response, 'choices') and response.choices:
            bot_reply = response.choices[0].message.content
            return bot_reply
        else:
            logging.error(f"❌ Empty or invalid response: {response}")
            return "❌ Error: Empty or invalid response."
    except Exception as e:
        logging.error(f"❌ API Error: {e}")
        return f"❌ API Error: {e}"


def isolate_and_save_python_code(input_string: str, file_path: str) -> Optional[str]:
    """
    Extracts Python code from a string and saves it to a .py file.
    """
    pattern = r'```python\s*(.*?)\s*```'
    match = re.search(pattern, input_string, re.DOTALL)

    if match:
        python_code = match.group(1)
        with open(file_path, 'w') as file:
            file.write(python_code)
        return file_path
    return None


def execute_python_script(script_path: str) -> Optional[str]:
    """
    Executes a Python script and returns the output.
    """
    try:
        result = subprocess.run(
            ['python', script_path],
            capture_output=True,
            text=True,
            check=True
        )
        print("✅ Script Output:\n", result.stdout)

        with open(script_path, 'r') as f:
            if 'plt.' in f.read():
                print("📈 Detected matplotlib usage. Check your window for plots.")

        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Error executing script:\n{e.stderr}")
        return None
