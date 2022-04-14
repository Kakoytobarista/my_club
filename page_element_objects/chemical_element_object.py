from enums.chemical_elements_enum import ChemicalElementsEnum
from page_element_objects.base_element_object import BaseElementObject


class ChemicalElementsObject(BaseElementObject):
    ELEMENT_XPATH = ChemicalElementsEnum.CHEMICAL_ELEMENT_XPATH.value
    CHLORINE_ELEM_BTN = ChemicalElementsEnum.CHLORINE_ELEM_BTN.value  # TODO: Bad case because for every element
    # TODO i will write selector. So if i will use all elements
    # TODO i will using iteration and search with any usefully algorithm for searching

    def click_on_elem(self, xpath):
        """Method for clicking on element when their presence"""
        self.click_(xpath=xpath)
