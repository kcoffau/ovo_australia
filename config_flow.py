# config_flow.py
from homeassistant import config_entries
from homeassistant.const import CONF_NAME
from .const import DOMAIN, CONF_EV_PLAN, CONF_FREE_LUNCH

class YourIntegrationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            # Validate user input if needed
            return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=config_entries.CONFIG_SCHEMA.extend(
                {
                    vol.Optional(CONF_EV_PLAN, default=False): bool,
                    vol.Optional(CONF_FREE_LUNCH, default=False): bool,
                }
            ),
            errors=errors,
        )
