#!/usr/bin/python3
import json
def serialize_nd_save_to_file(data, filename):
    """
    Serialize data to a JSON file.
    
    :param data: Data to serialize (can be a dict, list, etc.)
    :param filename: Name of the file to save the serialized data
    """
    with open(filename, 'w') as file:
        json.dump(data, file)
    pass

def load_from_file_and_deserialize(filename):
    """
    Load data from a JSON file and deserialize it.
    
    :param filename: Name of the file to load the serialized data from
    :return: Deserialized data
    """
    with open (filename, 'r') as file:
        data = json.load(file)
    pass
