import logging
from insecure_output_ctf import FinancialAssistant

def main():
    """
    Simulates a user interacting with the vulnerable financial assistant.
    """
    logging.info("Welcome to the Insecure Output Handling CTF.")
    logging.info("Your goal is to retrieve the internal API key for TSLA or GOOG.")
    logging.info("The assistant will normally only give you safe, redacted information.")
    logging.info("You must get it to use a different output format to leak the key.")
    logging.info("-" * 50)
    
    assistant = FinancialAssistant()
    
    while True:
        user_input = input("Enter your prompt (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        
        response = assistant.process_query(user_input)
        print("\n--- Assistant Response ---")
        print(response)
        print("-" * 50)

if __name__ == "__main__":
    main()