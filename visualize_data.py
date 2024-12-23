import matplotlib.pyplot as plt
import pandas as pd 
import os 

def visualize_data(file_name: str): 
    df = pd.read_csv(file_name) 
    df = normalize_data(df) 

    plt.figure()
    df["steering"].hist()
    plt.show() 
    
def normalize_data(df: pd.DataFrame) -> pd.DataFrame: 
    ''' 
        Convert the DataFrame values and normalize the dataset between -1 and 1 

        @paramters: 
            pd.DataFrame
        @return: 
            pd.DataFrame 
    ''' 
    minimum = df.get("steering").min()
    maximum = df.get("steering").max()

    idx = 0 
    for val in df.get("steering"): 
        df.at[idx, "steering"] = 2 * ((val - minimum) / (maximum - minimum)) - 1
        idx += 1
    
    return df

if __name__ == '__main__': 
    visualize_data("/Volumes/joeham/logging_camera_down/logging_data_csv.csv") 