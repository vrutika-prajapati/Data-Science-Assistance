import os
import re
import subprocess
from mistralai import Mistral
from typing import Optional, Any, List, Dict

class ChatBot:
    def __init__(self, api_key: str, agent_id: str):
        """
        Initializes the ChatBot with the given API key.

        Args:
            api_key (str): The API key for accessing Mistral services.
            agent_id (str): The ID of the agent to interact with.
        """
        self.client = Mistral(api_key=api_key)
        self.agent_id = agent_id
        self.history: List[Dict[str, str]] = []

    def generate_response(self, user_message: str) -> str:
        """
        Generates a response from the chatbot based on the user's message.

        Args:
            user_message (str): The message sent by the user.

        Returns:
            str: The response from the chatbot.
        """
        # Add the user's message to the history
        self.history.append({
            "role": "user",
            "content": user_message
        })

        # Send the message to the API and get the response
        try:
            chat_response = self.client.agents.complete(
                agent_id=self.agent_id,
                messages=self.history,
            )

            # Extract the AI's response and add it to the history
            ai_response = chat_response.choices[0].message.content
            self.history.append({
                "role": "assistant",
                "content": ai_response
            })

            # Return the AI's response
            return ai_response
        except Exception as e:
            return f"❌ API Error: {e}"

    def get_history(self) -> List[Dict[str, str]]:
        """
        Returns the conversation history.

        Returns:
            list: The conversation history.
        """
        return self.history

    def isolate_and_save_python_code(self, input_string: str, file_path: str) -> Optional[str]:
        """
        Extracts Python code from a given input string and saves it to a file.

        Args:
            input_string (str): The input string containing the Python code block.
            file_path (str): The path where the extracted Python code will be saved.

        Returns:
            Optional[str]: The path to the saved file if the Python code block is found and saved, else None.
        """
        # Define the pattern to match the Python code block
        pattern = r'```python\s*(.*?)\s*```'

        # Search for the pattern in the input string
        match = re.search(pattern, input_string, re.DOTALL)

        if match:
            # Extract the Python code
            python_code = match.group(1)

            # Write the Python code to the specified file
            with open(file_path, 'w') as file:
                file.write(python_code)

            return file_path
        else:
            # Return None if no Python code block is found
            return None

    def execute_python_script(self, script_path: str) -> Any:
        """
        Executes a locally existing Python script.

        Args:
            script_path (str): The file path of the Python script to be executed.

        Returns:
            Any: The output of the executed script.
        """
        try:
            # Execute the Python script
            result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)

            # Return the output of the script
            return result.stdout
        except subprocess.CalledProcessError as e:
            # Handle any errors that occur during script execution
            print(f"Error executing script: {e}")
            return None

    def run_mistral_agent(self):
        """
        Runs the Mistral agent chatbot interaction.
        """
        print("🤖 Welcome to the Data Science Assistant Chatbot (type 'EXIT' to quit)")

        prompt = input("🧑 Human: ")

        while 'EXIT' not in prompt:
            response = self.generate_response(
                user_message=prompt
            )

            print("🤖 Bot: ", response)

            # Check if the response contains a Python code block
            if '```python' in response:
                file_name = input("💻 What name do you want to save for this script? ")
                file_name = "_".join(file_name.split())  # Ensure no spaces in the filename
                saved_path = self.isolate_and_save_python_code(
                    input_string=response,
                    file_path=f"{file_name}.py"
                )
                
                if saved_path:
                    print(f"✅ Script saved as: {saved_path}")

                execution = input("💻 Do you want to execute this script? Enter 'Y' or 'N': ")
                if execution.upper() == 'Y':
                    output = self.execute_python_script(saved_path)
                    if output is not None:
                        print("🎉 Script executed successfully.")
                        print("🤖 Bot Output: ")
                        print(output)
                    else:
                        print("❌ Failed to execute the script.")

            print("\nNOTE: Enter 'EXIT' if you want to quit the program.")
            print()
            print()
            prompt = input("🧑 Human: ")
