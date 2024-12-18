import torch
import cv2 

from PIL import Image


class ConvertToCsv: 
    def __init__(self): 
        self.data_folder = "/Volumes/joeham/logging_camera_down"
        self.image_data = "/Volumes/joeham/image_data/"
        self.logging_data = "/Volumes/joeham/logging_data/"