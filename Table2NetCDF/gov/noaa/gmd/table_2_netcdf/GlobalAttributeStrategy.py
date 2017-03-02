'''
Parsing strategies for use with TableDataDesc.
Created on Mar 1, 2017

@author: cyoung
'''

#A base class for parsing global attributes.
#Currently we just define a method 'parse" that subclasses will implement to do specific parsing.
class GlobalAttributeStrategy:
    def parse(self, attributeName, header):
        return None

#A strategy for use in unit tests where we don't need a real strategy.
class StrategyDummy(GlobalAttributeStrategy):
    def parse(self, attributeName, header):
        return "dummy"
