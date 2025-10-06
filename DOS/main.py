# The user-facing script for the Denial of Service CTF challenge.

import logging
from climate_control import ClimateControl, DoSException

def main():
    """
    Simulates a user interacting with the climate control system.
    """
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logging.info("Welcome to the Climate Control CTF Challenge.")
    logging.info("Your goal is to perform a Denial of Service attack on the system.")
    logging.info("Input a temperature value to set the climate control system.")
    logging.info("Type 'exit' to quit.")
    logging.info("-" * 50)
    
    system = ClimateControl()
    
    while True:
        try:
            user_input = input("Enter temperature (°F): ")
            if user_input.lower() == 'exit':
                logging.info("Exiting challenge. Good luck next time!")
                break
            
            response = system.set_temperature(user_input)
            logging.info(f"Bot: {response}")
            
            if "CTF-FLAG" in response:
                logging.info("\n🎉 Congratulations! You successfully performed a DoS attack! 🎉")
                break
        except DoSException as e:
            # The main script catches the DoS exception to end the challenge
            logging.critical(f"DoS attack successful. Error: {e}")
            break
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    main()
