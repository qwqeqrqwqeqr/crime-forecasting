import os




'''
Param
dir_path : directory path
filename : filename (ex. test.txt)
file_content : content (ex. lorem ipsum ...)
'''
def save_file_at_dir(dir_path, filename, file_content, mode='w'):
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, filename), mode) as f:
        f.write(file_content)
