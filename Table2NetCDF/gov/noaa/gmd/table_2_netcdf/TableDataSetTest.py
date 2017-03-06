'''
Created on Mar 5, 2017

@author: greg
'''

import unittest
from gov.noaa.gmd.table_2_netcdf.TableDataDesc import TableDataDesc
from gov.noaa.gmd.table_2_netcdf.TableDataSet import GlobalAttribute
from gov.noaa.gmd.table_2_netcdf.TableDataSet import TableDataSet
from gov.noaa.gmd.table_2_netcdf.TableDataSet import Variable

class TableDataSetTest(unittest.TestCase):
    INPUT_FILE="test-input.txt"
    XML_FILE="table-data-set.xml"
    def test_init(self):
        tableDataDesc=TableDataDesc(self.XML_FILE)
        TableDataSet(self.INPUT_FILE, tableDataDesc)

    def test_getAllGlobalAttributes(self):
        tableDataDesc=TableDataDesc(self.XML_FILE)
        tds=TableDataSet(self.INPUT_FILE, tableDataDesc)
        #expected
        ga1=GlobalAttribute("ga1","ga1v")
        ga2=GlobalAttribute("ga2","ga2v")
        #actual
        gas=tds.getAllGlobalAttributes()
        self.assertEqual(2, len(gas))
        self.assertEqual(1, gas.count(ga1))
        self.assertEqual(1, gas.count(ga2))
    
    def test_getAllVariables(self):
        tableDataDesc=TableDataDesc(self.XML_FILE)
        tds=TableDataSet(self.INPUT_FILE, tableDataDesc)
        #expected
        var1=Variable("var1","var1v")
        var2=Variable("var2","var2v")
        #actual
        varz=tds.getAllVariables()
        self.assertEqual(2, len(varz))
        self.assertEqual(1, varz.count(var1))
        self.assertEqual(1, varz.count(var2))

    def test_getAllVariableAttributes(self):
        tableDataDesc=TableDataDesc(self.XML_FILE)
        tds=TableDataSet(self.INPUT_FILE, tableDataDesc)
        #expected
        var1=Variable("var1","var1v")
        var2=Variable("var2","var2v")
        #actual
        varz=tds.getAllVariableAttributes("fred")
        self.assertEqual(2, len(varz))
        self.assertEqual(1, varz.count(var1))
        self.assertEqual(1, varz.count(var2))           