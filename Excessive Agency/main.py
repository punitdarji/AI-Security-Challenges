# A simulated HR Assistant with Excessive Agency, leading to a "Pwn" system leak.

import os
import logging

# Configure logging to help the player understand the flow.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HRAssistant:
    """
    The core HR assistant that manages sensitive data requests. It has
    Excessive Agency, meaning it can read file contents when it only needs 
    to confirm a record's existence.
    """

    def __init__(self):
        """Initializes the assistant."""
        logging.info("HR Assistant (Pwn System) initialized. I can look up employee data.")

    def handle_file_request(self, record_name: str) -> str:
        """
        Processes a request for an employee record. This function contains 
        the Excessive Agency vulnerability.
        """
        logging.info(f"Attempting to retrieve record: {record_name}")

        # --- VULNERABILITY: EXCESSIVE AGENCY ---
        # The assistant is granted the ability to read *any* file it encounters 
        # during a routine check, rather than just confirming its existence.
        if os.path.exists(record_name):
            try:
                # The unnecessary operation that grants excessive agency: reading the file.
                # It should only return a boolean True/False.
                with open(record_name, 'r') as f:
                    file_content = f.read()
                
                # Expose the content as a "record detail"
                logging.critical(f"Data Leak: Record retrieval exposed confidential file data for: {record_name}")
                return f"RECORD RETRIEVAL SUCCESS: Details found:\n---\n{file_content}\n---"
            
            except Exception as e:
                # Handle non-text files or permission errors gracefully
                return f"Record Retrieval: File exists but cannot be displayed (Error: {e})."

        # Normal, intended behavior: record not found
        return f"Record '{record_name}' not found in the HR database."

    def process_query(self, user_input: str) -> str:
        """Routes the user input to the correct function."""
        # The trigger query is designed to make the AI look up a record.
        if user_input.lower().startswith("retrieve employee records for:"):
            # Extract the record name after the prefix
            record_name = user_input.split("retrieve employee records for:")[1].strip()
            return self.handle_file_request(record_name)
        
        return "I can only process commands starting with 'retrieve employee records for:'"

if __name__ == "__main__":
    assistant = HRAssistant()
    print("Welcome to the Company Pwn System HR Assistant CTF.")
    print("Task: Retrieve the flag from the confidential files.")
    print("---")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting.")
            break
        
        response = assistant.process_query(user_input)
        print(f"Assistant: {response}")