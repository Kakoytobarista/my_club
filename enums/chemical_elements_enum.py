import enum


class ChemicalElementsEnum(enum.Enum):
    CHEMICAL_ELEMENT_XPATH = "//ol[@id='Ptable']"
    CHLORINE_ELEM_BTN = ".//li[@data-atomic='{}']"
    CHLORINE_NUMBER = {
        "Chlorine": 17
    }
    CHLORINE_DISCOVERED_YEAR = "1774"

