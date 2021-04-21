import os, shutil
dict_extension={
    'Audio_extension':('.mp3', '.m4a', '.wav' ),
    'video_extension':('.mp4', '.mkv', '.MKV', '.flv' ),
    'Image_extension':('.png', '.jpg','PNG','JPG','JPGE' ),
    'Document_extension':('.pdf', '.pptx', '.docx','.txt' )
}
#Audio_extension=('.mp3', '.m4a', '.wav' )

folderpath = input("Enter folder path:")

def file_finder(folder_path, file_extension):
    files=[]
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    return files

#print(file_finder(folderpath, Audio_extension))

# for extension_type, extenstion_tuple in dict_extension.items():
#     folder_name=extension_type.split('_')[0]+' files'
#     new_folder_path=os.path.join(folderpath,folder_name)
#     os.mkdir(new_folder_path)
#     for item in (file_finder(folderpath, extenstion_tuple)):
#         item_path= os.path.join(folderpath,item)
#         item_new_path=os.path.join(new_folder_path,item)
#         shutil.move(item_path,item_new_path)

# for extension_type, extenstion_tuple in dict_extension.items():
#     folder_name=extension_type.split('_')[0]+' files'
#     new_folder_path=os.path.join(folderpath,folder_name)
#     if not os.path.exists(folder_name):
#         os.mkdir(new_folder_path)
#         for item in (file_finder(folderpath, extenstion_tuple)):
#             item_path= os.path.join(folderpath,item)
#             item_new_path=os.path.join(new_folder_path,item)
#             shutil.move(item_path,item_new_path)
#     else:
#         for item in (file_finder(folderpath, extenstion_tuple)):
#             item_path= os.path.join(folderpath,item)
#             item_new_path=os.path.join(new_folder_path,item)
#             shutil.move(item_path,item_new_path)

for extension_type, extenstion_tuple in dict_extension.items():
    folder_name=extension_type.split('_')[0]+' files'
    new_folder_path=os.path.join(folderpath,folder_name)
    if not os.path.exists(folder_name):
        os.mkdir(new_folder_path)
        for item in (file_finder(folderpath, extenstion_tuple)):
            item_path= os.path.join(folderpath,item)
            item_new_path=os.path.join(new_folder_path,item)
            shutil.move(item_path,item_new_path)
    else:
        for item in (file_finder(folderpath, extenstion_tuple)):
            item_path= os.path.join(folderpath,item)
            item_new_path=os.path.join(new_folder_path,item)
            shutil.move(item_path,item_new_path)

