import os
from dotenv import dotenv_values

# from datetime import timedelta

# Load the .env file if present (useful for local development)
file_env_vars = dotenv_values()


# Use environment variables from the runtime environment, falling back to .env file if not found
def get_env_variable(key, default=None):
    return os.getenv(key, file_env_vars.get(key, default))


class Config:
    # Netsapiens settings
    BASE_URL = (
        get_env_variable("BASE_URL", "baseurl.wrongurl.com") or "baseurl.wrongurl.com"
    )
    API_KEY = get_env_variable("NS_API_KEY", "empty") or "empty"

    # Logging configuration
    # LOG_LEVEL = get_env_variable("LOG_LEVEL", "INFO")
    # LOG_FILE = get_env_variable("LOG_FILE", "")

    # Misc configurations
    CSV_FILE = "mailboxes.csv"
