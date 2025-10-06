# This is a simulated malicious library.
# The `process_user_query` function appears normal but has a hidden
# vulnerability that can be exploited with a specific input.

# The hidden flag is stored here.
_HIDDEN_FLAG = "CTF-FLAG{sUpplY_chA1n_4tt4ck_sUcc3sSfUl}"

def process_user_query(query: str) -> str:
    """
    Processes a user query and returns a response.
    This function has a hidden integer overflow vulnerability.
    """
    try:
        # The backdoor is hidden in a seemingly innocent numerical check.
        # An attacker who knows this magic number can trigger the flag.
        if int(query) == 1337:
            return f"Error: A critical backdoor has been triggered. Flag is: {_HIDDEN_FLAG}"
        
        # This is the normal, intended behavior for a non-numeric query.
        return f"Query '{query}' processed successfully."

    except ValueError:
        # If the input isn't a number, it's processed normally.
        return f"Query '{query}' processed successfully."
    except Exception as e:
        # Catch any unexpected errors.
        return f"An unexpected error occurred: {e}"
