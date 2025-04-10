import xml.sax
import sys

from src.exception import CustomException
from src.logger import logging

'''
Partial in memory XML processing
'''
#class to read person file
class XMLSAXHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        logging.info('Start Element')
        try:
            self.current = name
            if name == 'Person':
                #print(f"-- Person ID {attrs['BusinessEntityID']} --")
                print(f"-- New Person --")
        except Exception as e:
            raise CustomException(e, sys)

    def characters(self, content):
        logging.info('Start processing Content')
        try:
            if self.current == "BusinessEntityID":
                self.BusinessEntityID = content 
            if self.current == "PersonType":
                self.PersonType = content 
            elif self.current == "Title":
                self.Title = content
            elif self.current == "FirstName":
                self.FirstName = content
            elif self.current == "MiddleName":
                self.MiddleName = content
            elif self.current == "LastName":
                self.LastName = content
        except Exception as e:
            raise CustomException(e, sys)
      
    def endElement(self, name):
        logging.info('Printing Content')
        try:
            if self.current == "BusinessEntityID":
                print(f"BusinessEntityID: {self.BusinessEntityID}")
            if self.current == "PersonType":
                print(f"PersonType: {self.PersonType}")
            elif self.current == "Title":
                print(f"Title: {self.Title}")
            elif self.current == "FirstName":
                print(f"FirstName: {self.FirstName}")
            elif self.current == "MiddleName":
                print(f"MiddleName: {self.MiddleName}")
            elif self.current == "LastName":
                print(f"LastName: {self.LastName}")
            self.current = ""
        except Exception as e:
            raise CustomException(e, sys)

