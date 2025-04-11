This repository contains methods for processing XML documents.
The XML document is generated from the Person table in the Person schema of the AdventureWorks database from SQL Server.
Code use to extract XML document

```
select
    TOP (50)
	BusinessEntityID,
	PersonType,
	FirstName,
	MiddleName,
	LastName
from
	Person.Person as Person
FOR XML AUTO, ELEMENTS, ROOT('Persons');
```

The XML document is saved as a file on a local drive with the name ‘XML_Person_export.xml’.

The document is then loaded into the Person table on the demo schema.
The upload code is

```
insert into demo.Person (
						BusinessEntityID,
						PersonType,
						FirstName,
						MiddleName,
						LastName
						)
select
	P_XML.record.query('BusinessEntityID').value('.','INT'),
	P_XML.record.query('PersonType').value('.','VARCHAR(10)'),
	P_XML.record.query('FirstName').value('.','VARCHAR(50)'),
	P_XML.record.query('MiddleName').value('.','VARCHAR(50)'),
	P_XML.record.query('LastName').value('.','VARCHAR(50)')
FROM
	(select CAST(P_XML as XML)
	FROM OPENROWSET(BULK 'D:\XML\XML_Person_export.xml', SINGLE_BLOB) as T(P_XML)) AS T(P_XML)
	CROSS APPLY P_XML.nodes('Persons/Person') AS P_XML (record);
```

There is Python code to process the downloaded XML file. Two modules are used to process the file:

1. Simple API for XML – Method
2. Document Object Model
