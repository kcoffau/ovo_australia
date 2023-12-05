from homeassistant import config_entries
class OvoEnergyAuFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL
    async def async_step_user(self, user_input=None):
