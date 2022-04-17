import time

from enums.chemical_elements_enum import ChemicalElementsEnum
from enums.exception_enum import ExceptionEnum
from enums.properties_enum import PropertiesEnum
from page_element_objects.chemical_element_object import ChemicalElementsObject
from page_element_objects.properties_element_object import PropertiesElementObject
from page_objects.properties_page_object import PropertiesPageObject


class TestProperties:

    def test_discovered_chlorine_date(self, browser):
        """Test for checking chlorine discovered"""
        PropertiesPageObject(browser)
        chemical_table = ChemicalElementsObject(browser)
        chemical_table.click_on_chemical_elem(
            ChemicalElementsEnum.ELEM_BTN.value.format(ChemicalElementsEnum.ELEM_NUMBER.value["Chlorine"]))
        properties = PropertiesElementObject(browser)
        chlorine_discovered_year = properties.get_property_value(PropertiesEnum.DISCOVERED_ID.value)
        assert browser.current_url == PropertiesEnum.DISCOVERED_URL.value, \
            ExceptionEnum.URL_WRONG_EXCEPTION.value

    def test_discovered_url_changed(self, browser):
        """Test for change url after click on chlorine element"""
        PropertiesPageObject(browser)
        chemical_table = ChemicalElementsObject(browser)
        chemical_table.click_on_chemical_elem(
            ChemicalElementsEnum.ELEM_BTN.value.format(ChemicalElementsEnum.ELEM_NUMBER.value["Chlorine"]))
        properties = PropertiesElementObject(browser)
        properties.click_property(PropertiesEnum.DISCOVERED_ID.value)
        assert browser.current_url == PropertiesEnum.DISCOVERED_URL.value, \
            ExceptionEnum.URL_WRONG_EXCEPTION.value
