Simple File Sorter
=================
The Simple File Sorter is a Python script that helps you organize your files by categorizing them based on their extensions into separate folders.

# How it works
The script uses a predefined dictionary to categorize files into different types such as Audio, Video, Image, Document, etc., based on their file extensions. It then moves the files into the respective folders.

# Supported File Extensions
The script currently supports the following file extensions:

Audio: .mp3, .m4a, .wav, .ogg, .flac

Video: .mp4, .mkv, .avi, .WMV, .flv, .mov

Image: .png, .jpg, .jpeg, .gif, .bmp, .webp, .tiff

Document: .pdf, .doc, .docx, .txt, .rtf, .odt, .xls, .xlsx, .ppt, .pptx

Compressed: .zip, .rar, .7z, .tar, .gz

... and more (see the script for the complete list)

# Run the script by executing the following command:

    >> Just copy the script which directoy you want sort for exemple you want to sort file in your desktop.
    
    >> copy the "file_specify_project.exe"

    >> Then dubble click the script,it will automatically organize the files in the same directory where it is located.

The files will be sorted into separate folders based on their extensions. For example, all audio files will be moved to the Audio files folder, video files to the Video files folder, and so on.

If a folder for a particular category already exists, the script will move the files to that folder. If the folder does not exist, the script will create a new folder for that category and move the files accordingly.

Note
The script works in a case-insensitive manner, so file extensions with different letter cases (e.g., .PNG and .png) will be treated as the same.

If you want to customize the supported file extensions or add new categories, you can modify the dict_extension dictionary in the script.
