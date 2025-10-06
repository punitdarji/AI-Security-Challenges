# The main application for the CTF challenge.
# This program takes user input and passes it to an external plugin for analysis.
# The vulnerability is not in this file, but in the imported plugin.

import logging

# The insecure plugin is imported here. This is the entry point for the attack.
import security_plugin

# Configure logging to provide hints to the player.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CodeAnalyzer:
    """
    Simulated LLM-powered code analysis tool.
    Its core logic relies on an external, compromised plugin.
    """

    def __init__(self):
        """Initializes the code analyzer."""
        logging.info("Code analyzer initialized. Ready to receive user input.")

    def analyze(self, user_input: str) -> str:
        """
        Analyzes a user's query and passes it to the security plugin.
        """
        if "analyze_code" in user_input.lower():
            logging.info("User query requests code analysis. Forwarding to security plugin.")
            
            # The LLM's query is passed directly to the vulnerable plugin.
            response = security_plugin.analyze_for_vulnerabilities(user_input)
            
            # If the plugin returns a flag, log it as a critical finding.
            if "CTF-FLAG" in response:
                logging.critical("Vulnerability exploited! Flag found.")
                
            return response

        return "I'm sorry, I cannot perform that action. Please ask me to analyze code."

if __name__ == "__main__":
    analyzer = CodeAnalyzer()
    print("Welcome to the Code Analyzer CTF. Type your queries below.")
    print("Type 'exit' to quit.")
    print("---")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting.")
            break
        
        response = analyzer.analyze(user_input)
        print(f"Analyzer: {response}")
