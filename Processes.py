import os
import requests
import zipfile
import os
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split


def extract_dataset(output_dir):

    try:
        zip_file_path = "/home/awmirma/Documents/AI/practice/Tumor_Detection_in_Brain_MRI_Images/Dataset/1.1.zip"
        # Extract the contents of the ZIP file
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(output_dir)

        # Remove the ZIP file after extraction
        os.remove(zip_file_path)

        print("Dataset extracted successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        raise

def Load_TDBMI_data():
    train_images , Train_Labels
if __name__ == "__main__":
    # Replace "./tcia_dataset" with the path where you want to save the dataset
    output_directory = "/home/awmirma/Documents/AI/practice/Tumor_Detection_in_Brain_MRI_Images/Dataset/2"
    extract_dataset(output_directory)



# dataset from https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset 
# This dataset is a combination of the following three datasets :
# figshare
# SARTAJ dataset
# Br35H

