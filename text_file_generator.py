from utils import read_file_line_by_line_as_list, check_regex_pattern, get_title, write_to_file
from constants import TXT_EXT, INPUT_DIR

script_file_path = "input/script.md"

def convert_title_to_filename(title):
    title = title.lower()
    words = title.split(' ')
    return '-'.join(words)

def organize_script_lines(script_line_list):
    result = {}
    last_filename = ""
    for line in script_content_list:
        extracted_title = get_title(line)
        if extracted_title is not None:
            filename = convert_title_to_filename(extracted_title)
            result[filename] = ""
            last_filename = filename
        else:
            result[last_filename] += line
    return result

def write_organized_script(organized_script):
    for filename in organized_script.keys():
        file_path = f"{INPUT_DIR}/{filename}.{TXT_EXT}"
        write_to_file(file_path, organized_script[filename])

script_content_list = read_file_line_by_line_as_list(script_file_path)
organized_script_lines = organize_script_lines(script_content_list)
write_organized_script(organized_script_lines)
print(script_content_list)
