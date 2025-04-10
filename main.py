from src.components.xml_sax_processor import XMLSAXHandler
from src.components.xml_dom_processor import XMLDOMHandler

import xml.sax


def usingSAX():
    handler = XMLSAXHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler=handler)
    parser.parse('XML_Person_export.xml')


def usingDOM():
    handler = XMLDOMHandler(r'XML_Person_export.xml')
    persons = handler.getNodeList( 'Person')

    for person in persons:
        #print(f" --Person: {person.getAttribute('BusinessEntityID')} --")
        print(f" --Person: {person.getElementsByTagName('BusinessEntityID')[0].childNodes[0].nodeValue} --")
        if person.getElementsByTagName('PersonType'):
            persontype =  person.getElementsByTagName('PersonType')[0].childNodes[0].nodeValue
        if person.getElementsByTagName('FirstName'):
            firstName =  person.getElementsByTagName('FirstName')[0].childNodes[0].nodeValue
        if person.getElementsByTagName('MiddleName'):
            middleName =  person.getElementsByTagName('MiddleName')[0].childNodes[0].nodeValue
        if person.getElementsByTagName('LastName'):
            lastName =  person.getElementsByTagName('LastName')[0].childNodes[0].nodeValue

        print(f"PersonType : {persontype}")
        print(f"FirstName : {firstName}")
        print(f"MiddleName : {middleName}")
        print(f"LastName : {lastName}")

    '''#Update DOM file values
    if persons[2].getElementsByTagName('MiddleName'):
        persons[2].getElementsByTagName('MiddleName')[0].childNodes[0].nodeValue = "Salano"
    else:
        persons[2].setAttribute("MiddleName", "Salano")
    #set ne attributes
    persons[2].setAttribute("Id", "25")
    persons[2].setAttribute("City", "Addlestone")
    '''
    #Add new node
    handler.AddNode("500","EM","Cleveland","Salano","Sullivan")




    #write output
    handler.writeXML('XML_Person_export.xml')


usingSAX()


