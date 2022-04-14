import time

from enums.chemical_elements_enum import ChemicalElementsEnum
from enums.exception_enum import ExceptionEnum
from page_element_objects.chemical_element_object import ChemicalElementsObject
from page_element_objects.properties_element_object import PropertiesElementObject
from page_objects.properties_page_object import PropertiesPageObject


class TestProperties:

    def test_discovered_chlorine_date(self, browser):
        """Test for checking chlorine discovered"""
        PropertiesPageObject(browser)
        chemical_table = ChemicalElementsObject(browser)
        chemical_table.click_on_elem(
            xpath=ChemicalElementsEnum.CHLORINE_ELEM_BTN.value.format(ChemicalElementsEnum.CHLORINE_NUMBER.value["Chlorine"]))
        properties = PropertiesElementObject(browser)
        chlorine_discovered = properties.get_discovered
        assert chlorine_discovered == ChemicalElementsEnum.CHLORINE_DISCOVERED_YEAR.value, \
            ExceptionEnum.DISCOVERED_WRONG_EXCEPTION.value  # TODO '\' this symbol does not match PEP8

    def test_discovered_url_changed(self, browser):
        """Test for change url after click on chlorine element"""
        PropertiesPageObject(browser)
        chemical_table = ChemicalElementsObject(browser)
        chemical_table.click_on_elem(
            xpath=ChemicalElementsEnum.CHLORINE_ELEM_BTN.value.format(ChemicalElementsEnum.CHLORINE_NUMBER.value["Chlorine"]))
        properties = PropertiesElementObject(browser)
        properties.click_to_discovered()
        assert browser.current_url == "https://ptable.com/#Properties/Discovered", \
            ExceptionEnum.URL_WRONG_EXCEPTION.value
