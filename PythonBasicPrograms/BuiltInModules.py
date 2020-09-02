import sys
class BuiltInModules:
    def getModules(self):
        moduleName = '\n '.join(sorted(sys.builtin_module_names))
        print(moduleName)

moduleObj = BuiltInModules()
moduleObj.getModules()