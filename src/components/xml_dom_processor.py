import xml.dom.minidom
import sys 

from src.exception import CustomException

#Loaad entire file into memory and can modify
#class to read XML file
class XMLDOMHandler():

    def __init__(self, file_path):
        self.domtree = xml.dom.minidom.parse(file_path)
        self.group = self.domtree.documentElement
        
    def getNodeList(self, node):
        try:
            #domtree = self.domtree
            group = self.group
            xml_obj = group.getElementsByTagName(node)
            return xml_obj
        except Exception as e:
            raise CustomException(e, sys)
        
    def writeXML(self, file_path):
        try:
            domtree = self.domtree
            domtree.writexml(open(file_path, 'w'))
        except Exception as e:
            raise CustomException(e, sys)
        
    def AddNode(self, id, personType, firstName, middleName, lastName):
        try:
            domtree = self.domtree
            new_person = domtree.createElement('Person')
            #new_person.setAttribute('Town','Addlestone')

            BusinessEntityID = domtree.createElement('BusinessEntityID')
            BusinessEntityID.appendChild(domtree.createTextNode(id))
            new_person.appendChild(BusinessEntityID)

            PersonType = domtree.createElement('PersonType')
            PersonType.appendChild(domtree.createTextNode(personType))
            new_person.appendChild(PersonType)

            FirstName = domtree.createElement('FirstName')
            FirstName.appendChild(domtree.createTextNode(firstName))
            new_person.appendChild(FirstName)

            MiddleName = domtree.createElement('MiddleName')
            MiddleName.appendChild(domtree.createTextNode(middleName))
            new_person.appendChild(MiddleName)

            LastName = domtree.createElement('LastName')
            LastName.appendChild(domtree.createTextNode(lastName))
            new_person.appendChild(LastName)

            group = self.group
            group.appendChild(new_person)

        except Exception as e:
            raise CustomException(e, sys)
        
    def AddNode2(self, mainElement, nodeList):
        try:
            domtree = self.domtree
            new_node = domtree.createElement(mainElement)
            #new_person.setAttribute('Town','Addlestone')
            for val in nodeList:
                subNode = domtree.createElement(val)
                subNode.appendChild(domtree.createTextNode(val))
                new_node.appendChild(subNode)

            group = self.group
            group.appendChild(new_node)

        except Exception as e:
            raise CustomException(e, sys)