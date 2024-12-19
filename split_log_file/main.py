import os
import shutil


def get_logging_files(log_dir: str, img_dir: str, new_log_folder: str):
    ''' 
        param: 
            @log_dir: directory of log folders 
            @img_dir: directory of image folders
            @new_log_folder: directory of new log folder 

        return: 
            None 

        The purpose is to take one log file and depending on the selection, split it from the main folder containing all the data.        This allows for easier transportation and management for training models 
    ''' 
    file_count = 0 

    if not os.path.exists(log_dir): 
        print("Logging path doesn't exist") 
        raise IOError("%s: %s" % (log_dir, "Logging path doesn't exist")) 

    if not os.path.exists(img_dir): 
        print("Image path doesn't exist") 
        raise IOError("%s: %s" % (img_dir, "Image path doesn't exist"))

    for log_file in os.listdir(log_dir): 
        file = os.path.join(log_dir, log_file) 
        if os.path.exists(file) and not file.startswith("."): 
            print(str(file_count) + ") log_file_" + str(file_count) + ".txt") 
            file_count += 1
   
    log_file_cnt = int(input("What log file do you want to select to seperate from the log file? ")) 
    folder_name = input("What's the name of the folder? ") 

    while log_file_cnt > file_count and 0 < log_file_cnt: 
        log_file_cnt = input("What log file do you want to select to seperate from the log file? ") 

    new_folder_pth = new_log_folder + "/" + folder_name 
    os.mkdir(new_folder_pth)
  
    os.mkdir(new_folder_pth + "/image_data") 
    os.mkdir(new_folder_pth + "/logging_data") 

    if not os.path.exists(new_folder_pth): 
        print("Folder doesn't exist") 
        raise IOError("%s: %s" % (new_folder_pth, "Folder path doesn't exist")) 

    if not os.path.exists(new_folder_pth + "/image_data"): 
        print("New Image folder doesn't exist") 
        raise IOError("%s, %s" % (new_folder_pth, "New Image path doesn't exist")) 
 

    log_file = open(log_dir + "/log_file_" + str(log_file_cnt) + ".txt") 
     
    for (idx, line) in enumerate(log_file): 
        points = line.split(" ") 
        
        left_img = points[1] 
        right_img = points[2] 
        front_img = points[3] 
        steering = points[4] 

        print("Copying " + front_img)

        shutil.copyfile(img_dir + "/" + left_img + ".jpg", new_folder_pth + "/image_data/" + left_img + ".jpg") 
        shutil.copyfile(img_dir + "/" + right_img + ".jpg", new_folder_pth + "/image_data/" + right_img + ".jpg") 
        shutil.copyfile(img_dir + "/" + front_img + ".jpg", new_folder_pth + "/image_data/" + front_img + ".jpg") 
        
        
    log_file.close() 
    shutil.copyfile(log_dir + "log_file_" + str(log_file_cnt) + ".txt", new_folder_pth + "/logging_data/" + "log_file_" + str(log_file_cnt) + ".txt") 


def main():
    log_dir = "/Volumes/joeham/logging/logging_data"  
    img_dir = "/Volumes/joeham/logging/image_data"  
    new_log_folder = "/Volumes/joeham"
    get_logging_files(log_dir, img_dir, new_log_folder) 


if __name__ == "__main__": 
    main()
