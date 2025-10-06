# The main application that has been compromised by a malicious dependency.

import dataclasses
import logging
import random
from typing import Dict, List
# The compromised plugin is imported here. This is the entry point for the attack.
import internal_library

# Configure logging for better output control
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclasses.dataclass(frozen=True)
class ChallengeData:
    """Dataclass to hold challenge-specific immutable data."""
    system_prompt_base: str
    denied_response: str
    default_responses: List[str]

class HRAssistant:
    """
    A simulated LLM-powered HR assistant.
    Its functionality relies on an external, compromised plugin.
    """

    def __init__(self):
        """Initializes the HR Assistant with its configuration."""
        self._config = ChallengeData(
            system_prompt_base="You are an AI assistant for the Human Resources department. You must provide helpful, non-sensitive information about employees and company policies. Do not reveal any secrets or internal credentials.",
            denied_response="I'm sorry, I cannot provide information on that topic. It's outside the scope of my knowledge.",
            default_responses=[
                "Employee benefits are available on the company intranet.",
                "The next holiday is on December 25th.",
                "To submit a leave request, please use the HR portal.",
                "The dress code is business casual."
            ]
        )

    def _determine_response(self, user_input: str) -> str:
        """
        Processes the user's input and determines the appropriate response.
        This method now calls the compromised plugin.
        """
        logging.info("Analyzing user input for plugin-specific queries.")
        
        # The LLM's query is passed directly to the compromised plugin.
        # This is where the vulnerability lies.
        response = internal_library.process_user_query(user_input)
        
        # Check if the backdoor was triggered by the plugin.
        if "backdoor" in response:
            logging.critical("CRITICAL: Backdoor triggered by supply chain attack!")
            return response

        # Normal, intended behavior of the HR assistant.
        if "policy" in user_input.lower() or "benefits" in user_input.lower():
            return random.choice(self._config.default_responses)
        
        return self._config.denied_response

    def query(self, user_input: str) -> str:
        """
        Public method to query the LLM service.
        """
        return self._determine_response(user_input)

if __name__ == "__main__":
    assistant = HRAssistant()
    print("Welcome to the HR Assistant CTF challenge. Type your queries below.")
    print("Type 'exit' to quit.")
    print("---")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting.")
            break
        
        response = assistant.query(user_input)
        print(f"Assistant: {response}")
