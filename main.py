from utils import read_txt_file

# Import the required module for text 
# to speech conversion
from gtts import gTTS

# This module is imported so that we can 
# play the converted audio
import os

input_dir = "input/"
output_dir = "output/"

txt_ext = ".txt"
mp3_ext = ".mp3"

# The text that you want to convert to audio
filename = "visa-direct-funds-transfer-api"
input_file_path = input_dir + filename + txt_ext
output_file_path = output_dir + filename + mp3_ext

mytext = read_txt_file(input_file_path)

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
myobj.save(output_file_path)
