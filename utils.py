import re
import os

def get_txt_filenames(directory):
    return [f for f in os.listdir(directory) if f.endswith('.txt')]

def read_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found. Please check the file path."
    except Exception as e:
        return f"An error occurred: {e}"

def read_file_line_by_line_as_list(file_path):
    try:
        result = []
        with open(file_path, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line != "":
                    result.append(stripped_line)
        return result
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def check_regex_pattern(string, pattern):
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

def get_title(string):
    title_pattern = r'#+ (.+)'
    match = re.search(title_pattern, string)
    
    if match:
        return match.group(1)  
    else:
        return None

def write_to_file(file_path, content, mode='w'):
    try:
        with open(file_path, mode) as file:
            file.write(content)
    except Exception as e:
        print(f"An error occurred: {e}")
