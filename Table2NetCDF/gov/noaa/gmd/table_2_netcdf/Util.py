'''

Utilities

Created on Mar 3, 2017

@author: cyoung
'''
class Util:
    # Get a class by fully qualified name.
    def getClass(self, kls):
        parts = kls.split('.')
        moduleName = ".".join(parts[:-1])
        #print("module "+module)
        #print("attr "+parts[-1])
        mod = __import__(moduleName, fromlist=[parts[-1]])
        clazz = getattr(mod, parts[-1])
        return clazz
    