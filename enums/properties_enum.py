import enum


class PropertiesEnum(enum.Enum):
    PROPERTIES_XPATH = "//ul[@id='Property']"
    PROPERTY_ENUM_XPATH = ".//label[@for='{}']/.."  # TODO: bad realisation, but for more good, i need time.
    PROPERTY_VALUE_ENUM_XPATH = "./output"

    DISCOVERED_ID = "t_discover"
    DISCOVERED_URL = "https://ptable.com/#Properties/Discovered"
