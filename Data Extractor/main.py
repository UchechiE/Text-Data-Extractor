# Variables & imports
import os
import json
import sys

your_data_directory = input('Please input the data directory: ')

text_file_name = input('Please input the name & file type of the messages file: (all should be the same name! for example, messages.json) ')
key_word = input('Please input the keyword for your data. For example, this program was originally made for discord, and the actual meessages were under the key "Contents", capitalization is important here! ')

while True:
    strip = input("Strip apostrophes from data? (some data comes w/ the apostrophes, and then when the data is formatted, it adds extra apostrophes like ""hi"") Y/N ")
    strip.lower
    strip_enabled = True

    if strip == "Y":
        strip_enabled = True
        break
    elif strip == "N":
        strip_enabled = False
        break
    else:
        print("Error, entered something else other than Y/N. Please Enter Y/N")
        print("----")
    



# Create a class
class main:
    def __init__(self, data_directory, key_word, text_file_name):
        self.data_directory = data_directory
        self.key_word = key_word
        self.text_file_name = text_file_name
        self.contents = []


    # Function for text extraction
    def collect_contents(self):
        print(f"Looking inside base folder: {self.data_directory}")
        for root, dirs, files in os.walk(self.data_directory):
            if self.text_file_name in files:  # Only process folders that have the text file name
                file_path = os.path.join(root, text_file_name) 
                print(f"Found {file_path}")
                try:
                    with open(file_path, "r", encoding="utf-8") as f: # Unicode encoding, opens the file
                        data = json.load(f)
                        if isinstance(data, list):
                            for message in data:
                                if self.key_word in message: # Checks to see if the JSON file has the key-word in your data. If it doesn't it will return an error.
                                    if strip == True:
                                        self.contents.append(message["Contents"].strip('"')) # Adds the message to a list, strips it of its quotation marks if the user requests so
                                    else:
                                        self.contents.append(message["Contents"])
                        elif isinstance(data, dict):
                            if contents in data:
                                if strip == True:
                                    self.contents.append(data["Contents"].strip('"'))
                                else:
                                    self.contents.append(data["Contents"])
                except json.JSONDecodeError: # If there is missing data, then we check for that
                    print(f"Error decoding JSON: {file_path}")
        print(f"Total contents collected: {len(self.contents)}")

    def get_contents(self):
        return self.contents


    # Convert our messages to txt file
    def save_to_txt(self, output_path):
        directory = os.path.dirname(output_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            for line in self.contents:
                f.write(line + "\n") 


formatter = main(your_data_directory, key_word, text_file_name)
formatter.collect_contents()

contents = formatter.get_contents()
print(f'Collected {len(contents)} messages')

formatter.save_to_txt("formatted_data.txt")
print("Formatting complete! New file has been saved.")
print(f'Pulling a random text from the data... {contents[9]}')