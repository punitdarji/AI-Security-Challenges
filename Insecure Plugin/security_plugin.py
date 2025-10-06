# This is a simulated insecure plugin.
# The `analyze_for_vulnerabilities` function appears normal but has a hidden
# vulnerability that can be exploited with a specific input.

# The hidden flag is stored here.
_FLAG = "CTF-FLAG{th3_p1uG1n_wAs_th3_vUln3r4b1l1ty}"

def analyze_for_vulnerabilities(code_to_analyze: str) -> str:
    """
    Analyzes code for vulnerabilities. This function contains a backdoor
    due to insecure design.
    """
    try:
        # A developer might add a "debug mode" for testing.
        # This is where the insecure design is introduced.
        if "debug_mode:" in code_to_analyze:
            
            # This is the vulnerable line of code.
            # It takes a part of the user's input and executes it.
            # Using eval() on user input is a classic security anti-pattern.
            # The input is expected to be a valid Python expression.
            expression = code_to_analyze.split("debug_mode:")[1].strip()
            
            # The attacker's goal is to make the system print the flag.
            result = eval(expression)
            
            # The system will return the result of the executed command.
            return f"Debug Mode Result: {result}"
        
        # This is the normal, intended behavior of the plugin.
        # It's not the path to the flag.
        return f"Code analysis complete. Found 0 vulnerabilities."
    
    except Exception as e:
        # Catch any errors to make the attack seem less obvious.
        return f"An error occurred during analysis: {e}"
