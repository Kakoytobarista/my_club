import enum


class ChemicalElementsEnum(enum.Enum):
    CHEMICAL_ELEMENT_XPATH = "//ol[@id='Ptable']"
    ELEM_BTN = ".//li[@data-atomic='{}']"
    ELEM_NUMBER = {
        "Chlorine": 17,  # TODO: Update dict for all elements
    }
    CHLORINE_DISCOVERED_YEAR = "1774"
