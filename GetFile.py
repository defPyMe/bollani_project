import os
from  datetime import date, datetime
import fnmatch


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
 
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')
    return location

#getting at least the same hour
def get_current_date_time():
    t=datetime.now()
    dt_string = t.strftime("%Y/%m/%d %H:%M:%S")
    # isolating up until the tenth minute
    t_corrected = (str(dt_string).replace("/", "").replace(" ", "").replace(":", ""))[0:11]
    return t_corrected

def find_file_by_name(folder_path, search_string):
    matching_files = []
    
    # List all files in the folder
    for filename in os.listdir(folder_path):
        # Use fnmatch to match the file name with the search string
        if fnmatch.fnmatch(filename, f'*{search_string}*') and ".crdownload" not in filename:
            matching_files.append(filename)
    print("Downloaded file found")
    
    return matching_files

def file_name(): 
    try:
        matching_files = find_file_by_name(get_download_path(),   get_current_date_time())
        chosen_file= (matching_files)[0]
        location = get_download_path()
        print("located file :   " + location + '\\' + chosen_file)
        return location + '\\' + chosen_file
    except:
        print("Downloaded file to be processed not found")

#needs o remove the file so thet the other downloaded files do not interact 
def removeFile(filename):
    os.remove(filename)