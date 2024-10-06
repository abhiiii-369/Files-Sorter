import os
import shutil

# Change "os.getcwd()" to a specific path if nessasary
folder_path = os.getcwd()

# Making a directory to store the sub-directories later
try:
    new_dir = f'{folder_path}\\Sorted Files'
    os.mkdir(new_dir)
except FileExistsError:
    try: 
        print(f"\n-- {folder_path}\\Sorted_Files already Exists --\n")
        ch = input(f"Do you want to continue in {folder_path}\\Sorted_Files\n(y/n): ")
        if not ch:
            raise ValueError("\nError : No Value Inputted!\n-- Exited --\n")
        elif ch == 'y':
            new_dir = f'{folder_path}\\Sorted Files'
        else:
            new_folder = input("Enter a new Folder name: ")
            if not new_folder:
                raise ValueError("\nError : No Value Inputted!\n-- Exited --\n")
            new_dir = f"{folder_path}\\{new_folder}"
            os.mkdir(new_dir)
    except ValueError as e:
        print(e)
    except:
        new_dir = f"{folder_path}\\Sorted Files"
        print("-- An Error Occured --\nValues set to Default")

print(f"\nFiles will be sorted in {new_dir}\n")

try:
    # Gets all files and directories in the specified folder
    files_and_dirs = os.listdir(folder_path)

    # Filters out the files only
    files = [f for f in files_and_dirs if os.path.isfile(os.path.join(folder_path, f))]

    # Checking if the folder has any files or not
    if len(files) == 0:
        raise ValueError("\nError : No Files Found!\n-- Exited --\n")
    
    # Dictionary for storing the Filenames having each formats respectively
    folders = { "Python Files"     : {"py"    : []},\
                "C Files"          : {"c"     : []},\
                "Webpages"         : {"html"  : [], "css" : [], "js" : []},\
                "Executable Files" : {"exe"   : []},\
                "Java Files"       : {"java"  : []},\
                "Dart Files"       : {"dart"  : []},\
                "Image Files"      : {"png"   : [], "jpeg"   : [], "gif" : [], "jpg" : [], "tiff" : [], "bmp" : [], "svg" : []},\
                "Video Files"      : {"mov"   : [], "mp4"    : [], "avi" : [], "mkv" : []},\
                "Audio Files"      : {"wav"   : [], "mp3"    : [], "aac" : []},\
                "Compressed Files" : {"zip"   : [], "rar"    : [], "xz"  : [], "z"   : [], "jar"  : []},\
                "Document Files"   : {"pdf"   : [], "xls"    : [], "csv" : [], "txt" : [], "dat"  : []},\
                "Extra"            : {"class" : [], "drawio" : []}
                # Add more if needed here after a comma(,) like :

                # "New Folder_1" : {"file_format_1" : [], "file_format_2" : [], "file_format_3" : [], ...},\
                # "New Folder_2" : {"file_format_4" : [], "file_format_5" : [], "file_format_6" : [], ...},\
                # ...
                
                }
    
    # Splits the Filenames into a list of its names and its file formats
    files_separated = [file.split(".") for file in files]

    count = 0

    # Storing the data and also moving it to the new directory
    for file_separated in files_separated:
        for folder, formats in folders.items():
            for format, files_list in formats.items():
                if file_separated[-1].lower() == format:
                    new_folder_file = f"{new_dir}\\{folder}"
                    os.makedirs(new_folder_file, exist_ok = True)

                    count += 1
                    filename = ".".join(file_separated)

                    source_path = os.path.join(folder_path, filename)
                    destination_path = os.path.join(new_folder_file, filename)

                    shutil.move(source_path, destination_path)
                    print(f"Moved: {source_path} to {destination_path}")
                    
                    files_list.append(filename)
    
    with open("log_sorted.txt", 'a') as fh:
        for each_folder, formats in folders.items():
            fh.write(f"{each_folder} : {formats}\n\n")
            fh.flush()
        fh.write(f"\n-----\nTotal Files Moved : {count}\n-----\n")

except ValueError as e:
    print(e)
