'''

Given an table oriented text file with header and a TableDataDesc that describes the
file, make global attributes, variables, variable attributes and the table data
available.

Created on Feb 27, 2017

@author: cyoung
'''

import gov.noaa.gmd.table_2_netcdf.TableDataDesc

class DataSet:
    def  __init__ (self, inputFile, dataSetDesc):
        self.inputFile=inputFile
        self.dataSetDesc=dataSetDesc
    def getAllGlobalAttributes(self):
        pass
    def getAllVariables(self):
        pass
    def getGlobalAttribute(self, attributeName):
        pass
    def getVariable(self, variableName):
        pass
    def getVariableAttributes(self, variableName):
        pass
    def __eq__(self, other):
        if self.inputFile != other.inputFile:
            return False
        if self.dataSetDesc != other.dataSetDesc:
            return False
        return True

class GlobalAttribute:
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

class Variable:
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

class VariableAttribute:
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

class Row:
    pass

class TableDataSet (DataSet):

    def  __init__ (self, inputFile, tableDataDesc):
        self.tableDataDesc=tableDataDesc
        self.inputFile=inputFile

    def parse(self):
        pass
    
    def getRows(self):
        pass

    def __eq__(self, other):
        if self.inputFile != other.inputFile:
            return False
        if self.tableDataDesc != other.tableDataDesc:
            return False
        return True

class Row :
    pass