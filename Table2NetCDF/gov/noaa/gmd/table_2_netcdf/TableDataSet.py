'''

Given an table oriented text file with header and a TableDataDesc that describes the
file, make global attributes, variables, variable attributes and the table data
available.

Created on Feb 27, 2017

@author: cyoung
'''

#import gov.noaa.gmd.table_2_netcdf.TableDataDesc

class DataSet:
    def  __init__ (self, inputFileName, dataSetDesc):
        self.inputFileName=inputFileName
        self.dataSetDesc=dataSetDesc
        self.file = open(inputFileName, "r", encoding="utf-8")
        
    def getAllGlobalAttributes(self):
        result=[GlobalAttribute("ga1","ga1v"),GlobalAttribute("ga2","ga2v")]
        return result

    def getAllVariables(self):
        result=[Variable("var1","var1v"),Variable("var2","var2v")]
        return result

    def getGlobalAttribute(self, attributeName):
        pass
    def getVariable(self, variableName):
        pass
    def getVariableAttribute(self, variableName):
        pass

    def getAllVariableAttributes(self, variableName):
        result=[VariableAttribute("var1","var1v"),VariableAttribute("var2","var2v")]
        return result

    def __eq__(self, other):
        if self.inputFileName != other.inputFileName:
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

    def  __init__ (self, inputFileName, tableDataDesc):
        self.tableDataDesc=tableDataDesc
        self.inputFileName=inputFileName

    def parse(self):
        pass
    
    def getRows(self):
        pass

    def __eq__(self, other):
        if self.inputFileName != other.inputFileName:
            return False
        if self.tableDataDesc != other.tableDataDesc:
            return False
        return True
    pass