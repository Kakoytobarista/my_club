import enum


class PropertiesEnum(enum.Enum):
    PROPERTIES_XPATH = "//ul[@id='Property']"
    DISCOVER_XPATH = "//label[@for='t_discover']/../output"  # TODO: bad realisation, but for more good, i need time.
