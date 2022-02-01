# Import Module
import os

# Folder Path
path = "/Users/enki/Work/read"

# Change the directory
os.chdir(path)

# Read text File


def read_text_file(file_path):
    is_find = False
    file_data = ''
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line_data = line
                if "```" in line:
                    if not is_find and "java" not in line:
                        with open(file_path, 'w') as w:
                            line_data = "```java\n"
                    is_find = not is_find
                file_data += line_data
    except:
        print("error")
        return
    try:
        with open(file_path, 'w', encoding='utf-8')as w:
            w.write(file_data)
    except:
        print("error")
        return


def file_reader():
    # iterate through all file
    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith(".md"):
            file_path = f"{path}/{file}"

            # call read text file function
            read_text_file(file_path)


def file_reader_with_subFile(path):
    if path == '':
        return
    file_list = []
    for home, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith(".md"):
                file_list.append(os.path.join(home, filename))
                read_text_file(os.path.join(home, filename))


if __name__ == "__main__":
    file_reader_with_subFile(path)
