from enums.properties_enum import PropertiesEnum
from page_element_objects.base_element_object import BaseElementObject


class PropertiesElementObject(BaseElementObject):
    ELEMENT_XPATH = PropertiesEnum.PROPERTIES_XPATH.value
    PROPERTY_XPATH = PropertiesEnum.PROPERTY_ENUM_XPATH.value
    PROPERTY_VALUE_XPATH = PropertiesEnum.PROPERTY_VALUE_ENUM_XPATH.value

    def get_property_value(self, property_name):
        return self._get_text(f"{self.PROPERTY_XPATH.format(property_name)}/{self.PROPERTY_VALUE_XPATH}")

    def click_property(self, property_name):
        self._click(self.PROPERTY_XPATH.format(property_name))
