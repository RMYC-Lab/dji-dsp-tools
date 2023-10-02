""" Attribute class """

from datetime import datetime
import xml.etree.ElementTree as ET

from dji_dsp_tools.dsp_codec.internal.code_type import CodeType
from dji_dsp_tools.dsp_codec.internal.fvd import FirmwareVersionDependency, get_fvd_from_string


class Attribute:
    def __init__(self,
                 creation_date: datetime,
                 sign: str,
                 modify_time: datetime,
                 guid: str,
                 creator: str = "Anonymous",
                 firmware_version_dependency: FirmwareVersionDependency = FirmwareVersionDependency(),
                 title: str = "Untitled",
                 code_type: CodeType = CodeType.PYTHON_CODE,
                 app_min_version: str = "",
                 app_max_version: str = ""):
        self.creation_date = creation_date
        self.sign = sign
        self.modify_time = modify_time
        self.guid = guid
        self.creator = creator
        self.firmware_version_dependency = firmware_version_dependency
        self.title = title
        self.code_type = code_type
        self.app_min_version = app_min_version
        self.app_max_version = app_max_version

    def get_xml_element(self) -> ET.Element:
        """ Get XML element """
        attribute = ET.Element("attribute")
        ET.SubElement(attribute, "creation_date").text = self.creation_date.strftime("%m/%d/%Y %I:%M:%S %p")
        ET.SubElement(attribute, "sign").text = self.sign
        ET.SubElement(attribute, "modify_time").text = self.modify_time.strftime("%m/%d/%Y %I:%M:%S %p")
        ET.SubElement(attribute, "guid").text = self.guid
        ET.SubElement(attribute, "creator").text = self.creator
        ET.SubElement(attribute, "firmware_version_dependency").text = self.firmware_version_dependency.value
        ET.SubElement(attribute, "title").text = self.title
        ET.SubElement(attribute, "code_type").text = self.code_type.value
        ET.SubElement(attribute, "app_min_version").text = self.app_min_version
        ET.SubElement(attribute, "app_max_version").text = self.app_max_version
        return attribute


def get_attribute_from_xml_element(attribute_xml_element: ET.Element) -> Attribute:
    """ Get Attribute from XML element """
    return Attribute(
        datetime.strptime(attribute_xml_element.find("creation_date").text, "%m/%d/%Y %I:%M:%S %p"),
        attribute_xml_element.find("sign").text,
        datetime.strptime(attribute_xml_element.find("modify_time").text, "%m/%d/%Y %I:%M:%S %p"),
        attribute_xml_element.find("guid").text,
        attribute_xml_element.find("creator").text,
        get_fvd_from_string(attribute_xml_element.find("firmware_version_dependency").text),
        attribute_xml_element.find("title").text,
        CodeType(attribute_xml_element.find("code_type").text),
        attribute_xml_element.find("app_min_version").text,
        attribute_xml_element.find("app_max_version").text
    )
