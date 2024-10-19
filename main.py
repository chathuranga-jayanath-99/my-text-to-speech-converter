from utils import read_txt_file, get_txt_filenames
from constants import TXT_EXT, MP3_EXT, INPUT_DIR, OUTPUT_DIR, EN_LANGUAGE

# Import the required module for text 
# to speech conversion
from gtts import gTTS

# This module is imported so that we can 
# play the converted audio
import os

def display_filenames(filenames):
    print("Available input file names:")
    for i, filename in enumerate(filenames, start=1):
        print(f"{i}. {filename}")

def select_file(filenames):
    while True:
        try:
            choice = int(input("Enter the number of the file you want to select: "))
            if 1 <= choice <= len(filenames):
                filename_with_ext = filenames[choice - 1]
                filename_without_ext = filename_with_ext.split(".")[0]
                return filename_without_ext
            else:
                print("Invalid number. Please select a valid file number.")
        except ValueError:
            print("Please enter a valid number.")

# The text that you want to convert to audio
available_filenames = get_txt_filenames(INPUT_DIR)
display_filenames(available_filenames)

selected_filename = select_file(available_filenames)

input_file_path = f"{INPUT_DIR}/{selected_filename}.{TXT_EXT}"
output_file_path = f"{OUTPUT_DIR}/{selected_filename}.{MP3_EXT}"

mytext = read_txt_file(input_file_path)

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=EN_LANGUAGE, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
myobj.save(output_file_path)
