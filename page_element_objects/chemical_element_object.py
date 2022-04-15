from enums.chemical_elements_enum import ChemicalElementsEnum
from page_element_objects.base_element_object import BaseElementObject


class ChemicalElementsObject(BaseElementObject):
    ELEMENT_XPATH = ChemicalElementsEnum.CHEMICAL_ELEMENT_XPATH.value
    CHLORINE_ELEM_BTN = ChemicalElementsEnum.ELEM_BTN.value

    def click_on_chemical_elem(self, xpath):
        """Method for clicking on element when their presence"""
        self._click(xpath=xpath)
