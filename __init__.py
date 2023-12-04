# __init__.py
DOMAIN = "your_integration"

async def async_setup(hass, config):
    return True

config_entry = config_entries.ConfigEntry(
    version=1,
    domain=DOMAIN,
    title="Your Integration",
    data={},
    source="user",
    connection_class=config_entries.CONN_CLASS_UNKNOWN,
)

async def async_setup_entry(hass, entry):
    return True

async def async_remove_entry(hass, entry):
    return True
