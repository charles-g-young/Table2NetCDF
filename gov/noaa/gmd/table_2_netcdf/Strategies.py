'''
Parsing strategies for use with TableDataDesc.
Created on Mar 1, 2017

@author: cyoung
'''

#A base class for parsing global attributes.
#Currently we just define a method 'parse" that subclasses will implement to do specific parsing.
class GlobalAttributeStrategy:
    def parse(self, attributeName, header):
        return "Method 'parse()' not over-ridden."

#A global attribute strategy for use in unit tests where we don't need a real strategy.
class GlobalAttributeStrategyDummy(GlobalAttributeStrategy):
    def parse(self, attributeName, header):
        return "dummy"

class HeaderStrategyDummy():
    def parse(self,file):
        return "dummy"
