from xml.dom import minidom

file = minidom.parse('testXML2.xml')
# print(models.namespaceURI)


class SheetHeader:
    def printHeaders(self):
        model = file.firstChild
        strModel = str(file.firstChild)
        wdTag = strModel[14:16]
        namespace = model.namespaceURI
        print("<?xml version='1.0'?>")
        print("<xsl:stylesheet xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\"")
        print("\txmlns:xs=\"http://www.w3.org/2001/XMLSchema\"")
        print("\txmlns:"+wdTag+"=\""+namespace+"\"")
        print("")

variables = str(input("How many variables would you like to add? "))
variables = int(variables)
iterator = str(1)
iterateLists = 0
variableNameList = []
selectClauses = []
while variables>0:
    variableName = input("Enter Name Of Variable: ")
    variableNameList.append("<xsl:variable name=\""+variableName+"\" ")
    if variableName.casefold() == "delimeter":
        delimeter = input("What type of delimeter?")
        selectClauses.append("select=\"'"+delimeter+"'\"/>")
    elif variableName.casefold()=="newline":
        selectClauses.append("select=\"'&#10;'\"/>")
    variables-=1 
header = SheetHeader()
header.printHeaders()
while iterateLists < len(variableNameList):
    print("\t" +variableNameList[iterateLists]+selectClauses[iterateLists])
    iterateLists+=1
        

            


