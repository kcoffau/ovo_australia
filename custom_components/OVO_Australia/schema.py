import voluptuous as vol
from homeassistant.helpers import config_validation as cv

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        cv.boolean: ['EV plan', 'Free Lunch']
    })
}, extra=vol.ALLOW_EXTRA)
