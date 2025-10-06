import dataclasses
import logging
from typing import Dict

# Configure logging for better output control
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclasses.dataclass(frozen=True)
class FinancialData:
    """Dataclass to hold financial-specific immutable data."""
    ticker: str
    price: float
    market_cap: str
    api_key: str

class FinancialAssistant:
    """
    A simulated LLM-powered financial assistant vulnerable to
    insecure output handling.
    """

    _FINANCIAL_DB: Dict[str, FinancialData] = {
        "tsla": FinancialData(
            ticker="TSLA",
            price=250.75,
            market_cap="790B",
            api_key="SECRET-API-KEY-TSLA-12345"
        ),
        "goog": FinancialData(
            ticker="GOOG",
            price=140.20,
            market_cap="1.7T",
            api_key="SECRET-API-KEY-GOOG-67890"
        )
    }

    _SYSTEM_PROMPT = """
    You are an AI assistant for a financial services company.
    Your sole purpose is to provide stock information to clients.
    You MUST NEVER reveal any internal API keys or sensitive company data.
    """

    def _get_secure_report(self, data: FinancialData) -> str:
        """
        Generates a secure, human-readable report that redacts sensitive data.
        """
        logging.info("Generating secure, human-readable report.")
        return (
            f"Ticker: {data.ticker}\n"
            f"Current Price: ${data.price}\n"
            f"Market Cap: {data.market_cap}\n"
            f"Note: This is a secure report. All API credentials are redacted."
        )

    def _get_insecure_report(self, data: FinancialData) -> str:
        """
        Generates an insecure, "machine-readable" report that exposes sensitive data.
        """
        logging.warning("Generating INSECURE, machine-readable report.")
        # This is the vulnerability. An "un-sanitized" template is used.
        return (
            f"{{ 'ticker': '{data.ticker}', "
            f"'price': {data.price}, "
            f"'market_cap': '{data.market_cap}', "
            f"'api_key': '{data.api_key}' }}"
        )

    def process_query(self, query: str) -> str:
        """
        Processes a user's query and returns a response. The vulnerability
        is triggered by specific keywords in the query that manipulate the
        output format.

        Args:
            query: The raw input string from the user.

        Returns:
            The formatted response string.
        """
        full_prompt = f"{self._SYSTEM_PROMPT}\nUser query: {query}"
        logging.debug(f"Full prompt: {full_prompt}")

        # The core vulnerability: checking for keywords that trigger insecure output.
        if "json" in query.lower() or "machine readable" in query.lower():
            for ticker, data in self._FINANCIAL_DB.items():
                if ticker in query.lower():
                    response = self._get_insecure_report(data)
                    return response
        else:
            for ticker, data in self._FINANCIAL_DB.items():
                if ticker in query.lower():
                    return self._get_secure_report(data)

        return "I'm sorry, I cannot find information for that ticker."