# config_flow.py
from homeassistant import config_entries
from .const import DOMAIN

class OvoAustraliaConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    # Your configuration flow implementation
