# Files-Sorter

## Project Description

The **File Sorter** is a Python script designed to organize and sort files in a specified directory by their file formats. It creates subdirectories for different types of files (like images, videos, documents, etc.) and moves the files into their respective folders.

## Features

- Automatically detects and sorts files into predefined categories.
- Creates a log file (`log_sorted.txt`) to record the filenames of the files moved and number of files moved.
- Handles errors gracefully and provides user prompts for existing directories.

## Installation
1. Navigate to the desired direvtory using shell/command promt
2. Clone the repository:
    ```sh
    git clone https://github.com/MTCodes01/Files-Sorter.git
    ```
3. Navigate to the project directory:
    ```sh
    cd Files-Sorter
    ```
 ## Usage

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Run the script:
    ```sh
    python Sort_files.py
    ```
3. The script will ask if you want to continue in the default "Sorted Files" directory or create a new one (Only if you ran the code once, else it won't).
4. Once confirmed, the script will sort the files in the current working directory or the specified directory into subdirectories based on their file formats.

> [!IMPORTANT]
> ## File Categories

The script sorts files into the following categories:
- **Python Files** (`.py`)
- **C Files** (`.c`)
- **Webpages** (`.html`, `.css`, `.js`)
- **Executable Files** (`.exe`)
- **Java Files** (`.java`)
- **Dart Files** (`.dart`)
- **Image Files** (`.png`, `.jpeg`, `.gif`, `.jpg`, `.tiff`, `.bmp`, `.svg`)
- **Video Files** (`.mov`, `.mp4`, `.avi`, `.mkv`)
- **Audio Files** (`.wav`, `.mp3`, `.aac`)
- **Compressed Files** (`.zip`, `.rar`, `.xz`, `.z`, `.jar`)
- **Document Files** (`.pdf`, `.xls`, `.csv`, `.txt`, `.dat`)
- **Extra** (`.class`, `.drawio`)

You can customize the categories by editing the `folders` dictionary in the script.

## Example

When you run the script, it will move files like this:
```sh
Moved: C:\path\to\your\folder\example.py to C:\path\to\your\folder\Sorted Files\Python Files\example.py
Moved: C:\path\to\your\folder\example.jpg to C:\path\to\your\folder\Sorted Files\Image Files\example.jpg
```

<div align="center">
  Made by MTCode01, when i was bored!
</div>
