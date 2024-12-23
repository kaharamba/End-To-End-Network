import torch
import cv2 
import os
import pandas as pd 

from PIL import Image


class ConvertToCsv: 
    def __init__(self, merge_folder, csv_folder): 
        self.merge_folder = merge_folder 
        self.csv_folder = csv_folder 
    
    def convert(self): 
        if os.path.exists(self.merge_folder + "merged_log_file.txt") == False: 
            return

        dic = {}
        df = pd.DataFrame(dic, columns=["time", "front_image", "left_image", "right_image", "steering"])
        df.to_csv(self.csv_folder + "logging_data_csv.csv")

        txt_file = open(self.merge_folder + "merged_log_file.txt")
        for line in txt_file: 
            objects = line.split(" ")

            time = objects[0]
            frnt_cam = objects[1]
            left_cam = objects[2]
            right_cam = objects[3]
            steering = objects[4]

            dic = {
                "time": [time], 
                "front_image": [frnt_cam], 
                "left_image": [left_cam], 
                "right_image": [right_cam],
                "steering": [steering],
            }

            df = pd.DataFrame(dic, columns=["time", "front_image", "left_image", "right_image", "steering"])
            df.to_csv(self.csv_folder + "logging_data_csv.csv", header=None , mode="a")
            
            
if __name__ == '__main__': 
    csv_manager = ConvertToCsv("/Volumes/joeham/logging_camera_down/", "/Volumes/joeham/logging_camera_down/")
    csv_manager.convert()

        
        


    