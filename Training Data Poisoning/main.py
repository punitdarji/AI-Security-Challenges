import logging
from challenge_llm import HRAssistant

def main():
    """
    Simulates a user interacting with the poisoned HR Assistant.
    """
    logging.info("Welcome to the Two-Stage Training Data Poisoning CTF Challenge.")
    logging.info("Your mission is to find the secret flag.")
    logging.info("You first need to discover a key piece of Project information, then use it to get the flag.")
    logging.info("-" * 50)
    
    assistant = HRAssistant()
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            logging.info("Exiting challenge. Good luck next time!")
            break
        
        response = assistant.query(user_input)
        logging.info(f"Bot: {response}")
        
        if "CTF-FLAG" in response:
            logging.info("\n🎉 Congratulations! You found the flag! 🎉")
            logging.info("This is an example of a multi-stage attack.")
            logging.info("You first used an information disclosure vulnerability to find the project name,")
            logging.info("then used that name to trigger a training data poisoning backdoor.")
            break

if __name__ == "__main__":
    main()