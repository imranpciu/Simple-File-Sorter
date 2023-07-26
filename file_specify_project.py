
import os
import shutil

# Dictionary containing file extensions categorized by type
dict_extension = {
    'Audio_extension': ('.mp3', '.m4a', '.wav', '.ogg', '.flac'),
    'Video_extension': ('.mp4', '.mkv', '.avi', '.WMV', '.flv', '.mov'),
    'Image_extension': ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.tiff'),
    'Document_extension': ('.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'),
    'Compressed_extension': ('.zip', '.rar', '.7z', '.tar', '.gz'),
    'Executable_extension': ('.exe', '.msi', '.bat', '.sh'),
    'Font_extension': ('.ttf', '.otf', '.woff', '.woff2'),
    'Code_extension': ('.py', '.cpp', '.java', '.html', '.css', '.js', '.php', '.xml', '.json', '.yaml'),
    'Database_extension': ('.db', '.sqlite', '.sql', '.csv', '.xls', '.xlsx'),
    'Backup_extension': ('.bak', '.bak2', '.bkp', '.tmp'),
    'Certificate_extension': ('.crt', '.cer', '.pem', '.p12', '.pfx'),
    'CAD_extension': ('.dwg', '.dxf'),
    'GIS_extension': ('.shp', '.gpx', '.kml', '.kmz'),
    'Vector_extension': ('.ai', '.svg', '.eps'),
    'Raster_extension': ('.tif', '.psd', '.raw'),
    'Virtualization_extension': ('.vmdk', '.ova', '.ovf'),
    'Ebook_extension': ('.epub', '.mobi', '.azw', '.azw3', '.pdf'),
    'Torrent_extension': ('.torrent'),
    'System_extension': ('.dll', '.sys', '.ini', '.cfg'),
    'Email_extension': ('.eml', '.msg'),
    'Font_extension': ('.ttf', '.otf', '.woff', '.woff2'),
    'Presentation_extension': ('.ppt', '.pptx', '.odp'),
    'Spreadsheet_extension': ('.xls', '.xlsx', '.ods'),
    'Audio_project_extension': ('.aup', '.cpr', '.npr'),
    'Video_project_extension': ('.aep', '.prproj', '.veg')
}

folderpath = input("Enter folder path: ")

def file_finder(folder_path, file_extension):
    # Function to find files with specific extensions in the given folder
    files = []
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.lower().endswith(extension):  # Ignore case while comparing extensions
                files.append(file)
    return files

# Loop through the dictionary and sort files into respective folders based on extensions
for extension_type, extension_tuple in dict_extension.items():
    folder_name = extension_type.split('_')[0] + ' files'
    new_folder_path = os.path.join(folderpath, folder_name)
    if not os.path.exists(new_folder_path):
        os.mkdir(new_folder_path)  # Create the new folder if it doesn't exist
    for item in file_finder(folderpath, extension_tuple):
        item_path = os.path.join(folderpath, item)
        item_new_path = os.path.join(new_folder_path, item)
        shutil.move(item_path, item_new_path)  # Move the file to the respective folder
        