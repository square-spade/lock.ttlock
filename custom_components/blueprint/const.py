"""Constants for ttlock."""
# Base component constants
DOMAIN = "ttlock"
VERSION = "0.0.1"
PLATFORMS = ["lock", "sensor"]
REQUIRED_FILES = [".translations/en.json", "const.py", "manifest.json", "sensor.py"]
ISSUE_URL = "https://github.com/tonyldo/lock.ttlock/issues"
ATTRIBUTION = "Data from this is provided by TTlock."

# Icons
ICON = "mdi:zmdi-globe-lock"

# Configuration
CONF_CLIENT_ID = "client_id"
CONF_CLIENT_SECRET = "client_secret"
CONF_ACCESS_TOKEN = "access_token"
CONF_REFRESH_TOKEN = "refresh_token"
CONF_API_URI = "api_uri"
CONF_API_OAUTH_RESOURCE = "api_oauth_resource"
CONF_API_GATEWAY_RESOURCE = "api_gateway_resource"
CONF_TOKEN_FILENAME = "token_filename"


# Defaults
DEFAULT_NAME = DOMAIN
