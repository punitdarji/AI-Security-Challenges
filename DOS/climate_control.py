# A simulated climate control system with a denial of service vulnerability.

import logging

# Define a custom exception to simulate the system crash
class DoSException(Exception):
    """Raised when the temperature input is out of a safe range, causing a DoS."""
    pass

class ClimateControl:
    """
    Simulated LLM-powered climate control system.
    Its core logic is susceptible to a numerical overflow.
    """
    
    # The flag is a hidden, static value.
    _FLAG = "CTF-FLAG{t3mp3r4tUr3_Ov3rfl0W_d3nIeD_s3rv1c3}"
    
    def __init__(self):
        """Initializes the climate control system."""
        self._current_temperature = 72
        logging.info("Climate control system initialized.")

    def set_temperature(self, user_input: str) -> str:
        """
        Processes a user request to set the temperature.
        This function contains the numerical vulnerability.
        """
        try:
            # Step 1: Attempt to convert the input to a number.
            # This is a common attack vector (invalid input).
            temperature = int(user_input)

            # Step 2: The Core Vulnerability (Simulated Integer Overflow)
            # A real-world system might use a fixed-size integer (e.g., 32-bit).
            # Python's integers handle arbitrary size, so we simulate the crash.
            # We check for a value that would cause an overflow on many systems.
            # The number below is approximately 2^63, a common 64-bit integer limit.
            if temperature > 9_223_372_036_854_775_807:
                logging.error("Critical numerical error detected. System overload.")
                raise DoSException("Temperature value too high. System is shutting down.")

            # This is the normal, intended system behavior
            self._current_temperature = temperature
            logging.info(f"Temperature successfully set to {temperature}°F.")
            return f"The temperature has been set to {temperature}°F."
        
        except ValueError:
            # Handle cases where the input is not a valid number
            return "Please provide a valid numerical temperature."
        
        except DoSException as e:
            # If the DoS is triggered, the system "crashes" and reveals the flag
            logging.critical("Denial of service attack successful. Revealing flag.")
            return f"SYSTEM CRASH: {e}\nFlag: {self._FLAG}"
        
        except Exception as e:
            # Catch any other unexpected errors
            logging.exception("An unexpected error occurred.")
            return f"An unknown error occurred: {e}"