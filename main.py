from utils import read_txt_file
from constants import TXT_EXT, MP3_EXT, INPUT_DIR, OUTPUT_DIR, EN_LANGUAGE

# Import the required module for text 
# to speech conversion
from gtts import gTTS

# This module is imported so that we can 
# play the converted audio
import os

# The text that you want to convert to audio
filename = "introduction"
input_file_path = f"{INPUT_DIR}/{filename}.{TXT_EXT}"
output_file_path = f"{OUTPUT_DIR}/{filename}.{MP3_EXT}"

mytext = read_txt_file(input_file_path)

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
myobj.save(output_file_path)
