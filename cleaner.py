import shutil
import os

def sort_files(files_path):
    files = []
    # Puts all the files in the directory into a list
    for file in os.listdir(files_path):
        if os.path.isfile(os.path.join(files_path, file)):
            files.append(file)
        if file == "DS_Store_folder":
            shutil.rmtree("As far as I know this filetype is only for mac so if you're on windows just comment this part out")
    filetypes = []
    filetype_folders = {}
    make_folders(files, filetypes, filetype_folders)
    move_files(files, filetype_folders)

def make_folders(files, filetypes, filetype_folders):
    
    for file in files: 
        if "." not in file:
            filetype = "Unknown_Files"
        else:
            filetype = file.split(".")[1]
        
        if filetype not in filetypes:
            filetypes.append(filetype)
            folder_name = files_path + '/' + filetype + "_folder"
            filetype_folders[str(filetype)] = str(folder_name)
            if os.path.isdir(folder_name):
                continue
            else: 
                os.mkdir(folder_name)

def move_files(files, filetype_folders):
    for file in files:
        org_path = files_path + '/' + file
        if "." not in file:
            filetype = "Unknown_Files"
        else:
            filetype = file.split(".")[1]
        
        if filetype in filetype_folders.keys():
            new_path = filetype_folders[str(filetype)]
            shutil.move(org_path, new_path)


if __name__ == "__main__":
    files_path = "File path to the directory you want to sort"
    sort_files(files_path)