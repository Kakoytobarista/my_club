from enums.properties_enum import PropertiesEnum
from page_element_objects.base_element_object import BaseElementObject


class PropertiesElementObject(BaseElementObject):
    ELEMENT_XPATH = PropertiesEnum.PROPERTIES_XPATH.value
    DISCOVERED_XPATH = PropertiesEnum.DISCOVER_XPATH.value

    @property
    def get_discovered(self):
        return self.element.find_element_by_xpath(self.DISCOVERED_XPATH).text

    def click_to_discovered(self):
        self.element.find_element_by_xpath(self.DISCOVERED_XPATH).click()
