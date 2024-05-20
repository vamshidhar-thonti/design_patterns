import csv
import json
import xml.etree.ElementTree as ET

from abc import ABC, abstractmethod
from typing import List, Dict, Any

# Step 1: Create the FileParser interface
class FileParser(ABC):

    @abstractmethod
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        pass

# Step 2: Implement the file parsers
# TODO: Implement CSVParser, JSONParser, and XMLParser classes
class CSVParser(FileParser):
    def parse_file(self, file_path: str):
        parsed_data = []
        with open(file_path, 'r') as file:
            csv_data = csv.reader(file)
            headers = []
            for index, data in enumerate(csv_data):
                row = {}
                if index == 0:
                    headers = data
                    continue
                for header, value in zip(headers, data):
                    row[header] = value
                parsed_data.append(row)

        return parsed_data
        
class JSONParser(FileParser):
    def parse_file(self, file_path: str):
        with open(file_path, 'r') as file:
            return json.loads(file.read())
            
class XMLParser(FileParser):
    def parse_file(self, file_path: str):
        parsed_data = []
        with open(file_path, 'r') as file:
            root = ET.fromstring(file.read())
            for element in root:
                element_dict = {}
                for field in element:
                    element_dict[field.tag] = field.text
                parsed_data.append(element_dict)
        
        return parsed_data

# Step 3: Implement the FileReader class
class FileReader:

    def __init__(self, file_parser: FileParser):
        # TODO: Initialize the file reader with the given file_parser
        self.file_parser = file_parser

    def read_file(self, file_path: str) -> List[Dict[str, Any]]:
        # TODO: Read the file at the given file_path and return a list of dictionaries using the specified file parser
        data = self.file_parser.parse_file(file_path)
        return data

# Step 4: Test your implementation
if __name__ == "__main__":
    # TODO: Create a file reader with a CSVParser
    reader = FileReader(XMLParser())

    # TODO: Read a sample CSV file and print the list of dictionaries
    data = reader.read_file("sample.xml")
    print(data)
