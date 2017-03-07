'''
Created on Mar 5, 2017

@author: greg
'''

import unittest
from gov.noaa.gmd.table_2_netcdf.TableDataDesc import TableDataDesc
from gov.noaa.gmd.table_2_netcdf.TableDataSet import GlobalAttribute
from gov.noaa.gmd.table_2_netcdf.TableDataSet import VariableAttribute
from gov.noaa.gmd.table_2_netcdf import Properties
from gov.noaa.gmd.table_2_netcdf.TableDataSet import TableDataSet
from gov.noaa.gmd.table_2_netcdf.TableDataSet import Variable

class TableDataSetTest(unittest.TestCase):

    INPUT_FILE=Properties.TEST_DATA_DIR+"/dummy-data-set.txt"
    XML_FILE=Properties.TEST_DATA_DIR+"/dummy-data-set.xml"

    def test_init(self):
        tableDataDesc=TableDataDesc(self.XML_FILE)
        TableDataSet(self.INPUT_FILE, tableDataDesc)

    def test_getAllGlobalAttributes(self):
        tableDataDesc=TableDataDesc(self.XML_FILE)
        tds=TableDataSet(self.INPUT_FILE, tableDataDesc)
        #expected
        ga1=GlobalAttribute("dummy1","dummy1")
        ga2=GlobalAttribute("dummy2","dummy2")
        #actual
        gas=tds.getAllGlobalAttributes()
        self.assertEqual(2, len(gas))
        self.assertEqual(1, gas.count(ga1))
        self.assertEqual(1, gas.count(ga2))
    
    def test_getAllVariables(self):
        tableDataDesc=TableDataDesc(self.XML_FILE)
        tds=TableDataSet(self.INPUT_FILE, tableDataDesc)
        #expected
        var1=Variable("dummy1","dummy1")
        var2=Variable("dummy2","dummy2")
        #actual
        varz=tds.getAllVariables()
        self.assertEqual(2, len(varz))
        self.assertEqual(1, varz.count(var1))
        self.assertEqual(1, varz.count(var2))

    def test_getAllVariableAttributes(self):
        tableDataDesc=TableDataDesc(self.XML_FILE)
        tds=TableDataSet(self.INPUT_FILE, tableDataDesc)
        #expected
        var1=VariableAttribute("dummy1","dummy1")
        #var2=VariableAttribute("dummy2","dummy2")
        #actual
        varz=tds.getAllVariableAttributes("dummy1")
        self.assertEqual(1, len(varz))
        self.assertEqual(1, varz.count(var1))
        #self.assertEqual(1, varz.count(var2))           