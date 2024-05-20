import sys
from abc import ABC, abstractmethod
from typing import List
import xml.etree.ElementTree as ET
from enum import Enum, auto
import json
import csv


# Contact data container class
class Contact:
    def __init__(self, full_name, email, phone_number, is_friend):
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.is_friend = is_friend
    
    def __str__(self):
        return f"{self.full_name} ({self.email}) - {self.phone_number} {'(Friend)' if self.is_friend else ''}"


# Our base class for reading file data
class FileReader(ABC) :
    def __init__(self, file_name):
        self.file_name = file_name

    abstractmethod
    def read(self) -> str:
        pass

# Abstract base class for all Contact Data Adapters
class ContactsAdapter(ABC):
    def __init__(self, data_source: FileReader):
        self.data_source = data_source
    
    abstractmethod
    def get_contacts(self) -> List[Contact]:
        pass


# Specific implementation of the adapter to read XML Source data
class XMLContactsAdapter(ContactsAdapter):
    def get_contacts(self):
        # Parse XML data into an ElementTree object
        root = ET.fromstring(self.data_source.read()) # Read XML data from a file
        # Extract contact information from the XML and create Contact objects
        contacts = []
        for elem in root.iter():
            if elem.tag == 'contact':
                full_name = elem.find('full_name').text
                email = elem.find('email').text
                phone_number = elem.find('phone_number').text
                is_friend = elem.find('is_friend').text.lower() == 'true'
                contact = Contact(full_name, email, phone_number, is_friend)
                contacts.append(contact)
        return contacts

# Specific implementation of the adapter to read JSON Source data
class JSONContactsAdapter(ContactsAdapter):
    def get_contacts(self):
        # Parse JSON data into a dictionary
        data_dict = json.loads(self.data_source.read()) # Read JSON data from a file
        # Extract contact information from the dictionary and create Contact objects
        contacts = []
        for contact_data in data_dict['contacts']:
            full_name = contact_data['full_name']
            email = contact_data['email']
            phone_number = contact_data['phone_number']
            is_friend = contact_data['is_friend']
            contact = Contact(full_name, email, phone_number, is_friend)
            contacts.append(contact)
        return contacts
    
################### Exercise 1 ###################
class CSVContactsAdapter(ContactsAdapter):
    def get_contacts(self):
        data_csv = csv.reader(self.data_source.read())
        contacts = []

        for index, contact_data in enumerate(data_csv):
            if index == 0:
                continue
            full_name, email, phone_number, is_friend = contact_data
            is_friend = is_friend.lower() == "true"
            contact = Contact(full_name, email, phone_number, is_friend)
            contacts.append(contact)
        
        return contacts
################### Exercise 1 ###################

# Specific implementation of the file reader to be used with XML Files
class XMLReader(FileReader):
    def read(self):
        # Read the contents of the XML file and return as a string
        with open(self.file_name, 'r') as f:
            return f.read()

# Specific implementation of the file reader to be used with JSON files
class JSONReader(FileReader):
    def read(self):
        # Read the contents of the JSON file and return as a string
        with open(self.file_name, 'r') as f:
            return f.read()

################### Exercise 1 ###################
class CSVReader(FileReader):
    def read(self):
        return open(self.file_name, 'r')
################### Exercise 1 ###################

class AdapterType(Enum):
    XML = auto()
    JSON = auto()
    CSV = auto()

class AdapterExecutor(ABC):
    def __init__(self) -> None:
        self.file_reader: FileReader = None
        self.file_adapter: ContactsAdapter = None

    @abstractmethod
    def reader(self, file_path):
        pass

    @abstractmethod
    def adapter(self):
        pass

    def print_contacts(self):
        for contact in self.file_adapter.get_contacts():
            print(contact)

class XMLAdapterExecutor(AdapterExecutor):
    def __init__(self) -> None:
        super().__init__()

    def reader(self, file_path):
        self.file_reader = XMLReader(file_path)

    def adapter(self):
        self.file_adapter = XMLContactsAdapter(self.file_reader)

class JSONAdapterExecutor(AdapterExecutor):
    def __init__(self) -> None:
        super().__init__()

    def reader(self, file_path):
        self.file_reader = JSONReader(file_path)

    def adapter(self):
        self.file_adapter = JSONContactsAdapter(self.file_reader)

class CSVAdapterExecutor(AdapterExecutor):
    def __init__(self) -> None:
        super().__init__()

    def reader(self, file_path):
        self.file_reader = CSVReader(file_path)

    def adapter(self):
        self.file_adapter = CSVContactsAdapter(self.file_reader)

print("######## CONTACTS APPLICATION ########")
print("Choose from the below choices: ")
print("1. XML")
print("2. JSON")
print("3. CSV")

option = input("Enter a number from the listed options above: ")

def print_contact_data(option: str):
    if option == "1":
        executor = XMLAdapterExecutor()
        executor.reader('contacts.xml')
        executor.adapter()
    elif option == "2":
        executor = JSONAdapterExecutor()
        executor.reader('contacts.json')
        executor.adapter()
    elif option == "3":
        executor = CSVAdapterExecutor()
        executor.reader('contacts.csv')
        executor.adapter()
    else:
        print("Invalid choice")
        sys.exit(1)

    executor.print_contacts()

print_contact_data(option)

# # Simple display routine to display Contact data to the console      
# def print_contact_data(contacts_source : ContactsAdapter):
#     # Print the Contact objects
#     for contact in contacts_source.get_contacts():
#         print(contact)

# # Example usage
# xml_reader = XMLReader('contacts.xml')
# # Create an XML adapter and convert the data to a list of Contact objects
# xml_adapter = XMLContactsAdapter(xml_reader)
# # Print the Contact objects
# print_contact_data(xml_adapter)

# json_reader = JSONReader('contacts.json')
# # Create a JSON adapter and convert the data to a list of Contact objects
# json_adapter = JSONContactsAdapter(json_reader)
# # Print the Contact objects
# print_contact_data(json_adapter)

# ################### Exercise 1 ###################
# csv_reader = CSVReader('contacts.csv')
# csv_adapter = CSVContactsAdapter(csv_reader)
# print_contact_data(csv_adapter)
# ################### Exercise 1 ###################
