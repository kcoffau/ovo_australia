DOMAIN = 'ovoenergyau'
def async_setup(hass, config):
    """Set up the OVO Energy Australia component."""
    hass.data[DOMAIN] = {}
    return True
