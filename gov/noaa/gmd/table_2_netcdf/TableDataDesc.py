'''
Given an XML file that describes a text file containing a header and a table, parse
the XML into it's descriptive elements.

Created on Feb 27, 2017

@author: cyoung
'''

import  xml.etree.ElementTree as ElementTree
from gov.noaa.gmd.table_2_netcdf.Util import Util

class TableDataDesc:

    #XML element names
    ELEMENT_NAME="name"
    ELEMENT_DATA_TYPE="data-type"
    ELEMENT_GLOBAL_ATTRIBUTE="global-attribute"
    ELEMENT_GLOBAL_ATTRIBUTE_STRATEGY="global-attribute-strategy"
    ELEMENT_CLASS_NAME="class-name"

    def  __init__ (self, xmlFile):
        self.xmlFile=xmlFile
        self.tree = ElementTree.parse(xmlFile)

    def getAllColumnDesc (self):
        pass
    def getAllGlobalAttributeDesc(self):
        pass
    def getAllVariableAttributeDesc(self):
        pass
    def getColumnDesc(self, columnName):
        pass

    def getGlobalAttributeDesc(self, attributeName):
        element=self.__getGlobalAttributeElement(attributeName)
        name=element.find(self.ELEMENT_NAME).text
        dataType=element.find(self.ELEMENT_DATA_TYPE).text
        child=element.find(self.ELEMENT_GLOBAL_ATTRIBUTE_STRATEGY)
        className=child.find(self.ELEMENT_CLASS_NAME).text
        strategyDesc=GlobalAttributeStrategyDesc(className)
        return GlobalAttributeDesc(name, dataType, strategyDesc)

    def getGlobalAttributeStrategyDesc(self, attributeName):
        element=self.__getGlobalAttributeStrategyElement(attributeName)
        className=element.find(self.ELEMENT_CLASS_NAME).text
        return GlobalAttributeStrategyDesc(className)

    def getVariableAttributeDesc(self, variableName):
        pass
    def getVariableAttributeStrategyDesc(self, variableName):
        pass

    def __getGlobalAttributeElement(self, attributeName):
        root = self.tree.getroot()
        elements=root.findall(".//"+self.ELEMENT_GLOBAL_ATTRIBUTE)
        element=None
        for e in elements:
            if e.find(self.ELEMENT_NAME).text == attributeName:
                element=e
                break
        if element is None:
            raise Exception(self.ELEMENT_GLOBAL_ATTRIBUTE+" element with name '"+attributeName+
                            "' not found in file '"+self.xmlFile+"'.")
        return element

    def __getGlobalAttributeStrategyElement(self, attributeName):
        globalAttributeElement=self.__getGlobalAttributeElement(attributeName)
        element=globalAttributeElement.find(self.ELEMENT_GLOBAL_ATTRIBUTE_STRATEGY)
        if element is None:
            raise Exception(self.ELEMENT_GLOBAL_ATTRIBUTE_STRATEGY+" element with name '"+attributeName+
                            "' not found in file '"+self.xmlFile+"'.")
        return element

    def __eq__(self, other):
        if self.xmlFile != other.xmlFile:
            return False
        return True

class ColumnDesc:
    def  __init__ (self, columnName, index, dataType):
        self.columnName=columnName
        self.index=index
        self.dataType=dataType
    def getColumnName(self):
        return self.columnName
    def getDataType(self):
        return self.dataType
    def getIndex(self):
        return self.index
    def __eq__(self, other):
        if self.columnName != other.columnName:
            return False
        if self.index != other.index:
            return False
        if self.dataType != other.dataType:
            return False
        return True

class GlobalAttributeDesc:
    def  __init__ (self, attributeName, attributeType, globalAttributeStrategy):
        self.attributeName=attributeName
        self.attributeType=attributeType
        self.globalAttributeStrategy=globalAttributeStrategy
    def getAttributeName(self):
        return self.attributeName
    def getAttributeType(self):
        return self.attributeType
    def getGlobalAttributeStrategy(self):
        return self.globalAttributeStrategy
    def __eq__(self, other):
        if self.attributeName != other.attributeName:
            return False
        if self.attributeType != other.attributeType:
            return False
        if self.globalAttributeStrategy != other.globalAttributeStrategy:
            return False
        return True

#A base class for strategy descriptions.
class StrategyDesc(object):
    #Hold the name of the strategy class to be loaded.
    def  __init__ (self, strategyClassName):
        self.strategyClassName=strategyClassName

    def __eq__(self, other):
        if self.strategyClassName != other.strategyClassName:
            return False
        return True

class GlobalAttributeStrategyDesc(StrategyDesc):
    def __init__ (self, strategyClassName):
        super().__init__(strategyClassName)
    #Return the value parsed from the header of the given global attribute
    def parse (self, attributeName, header):
        #Instantiate the strategy class by name.
        c=Util().getClass(self.strategyClassName)
        return c.parse(attributeName, header)

class HeaderStrategyDesc(StrategyDesc):
    def __init__ (self, strategyClassName):
        super().__init__(strategyClassName)
    #Return the header parsed from the file.
    def parse (self, file):
        c=Util.getClass(self.strategyClassName)
        return c.parse(file)

class VariableAttributeDesc:
    def  __init__ (self, variableName, variableType, attributes):
        self.variableName=variableName
        self.variableType=variableType
        self.attributes=attributes
    def getVariableName(self):
        return self.variableName
    def getVariableType(self):
        return self.variableType
    def getAttributes(self):
        return self.attributes
    def __eq__(self, other):
        if self.variableName != other.variableName:
            return False
        if self.variableType != other.variableType:
            return False
        if self.attributes != other.attributes:
            return False
        return True

#A strategy for parsing variable attributes
class VariableAttributeStrategyDesc:
    def  __init__ (self, strategyClassName):
        self.strategyClassName=strategyClassName
    #Parse the variable attributes from the header
    def parse (self, variableName, header):
        #Return the Attributes collection
        pass

#A variable attribute. Variables may have multiple attributes.
class Attribute:
    def  __init__ (self, name, value):
        self.name=name
        self.value=value
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.value != other.value:
            return False
        return True

