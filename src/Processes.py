import os
import requests
import zipfile
import os
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split


def extract_dataset(output_dir):

    try:
        zip_file_path = "./Dataset/1.1.zip"
        # Extract the contents of the ZIP file
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(output_dir)

        # Remove the ZIP file after extraction
        os.remove(zip_file_path)

        print("Dataset extracted successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        raise

def Load_TDBMI_data(data_dir, image_size=(256, 256)):
    x = []
    y = []

    # Load tumor images
    tumor_dir = os.path.join(data_dir,'Training' , 'tumor')
    for filename in os.listdir(tumor_dir):
        if filename.endswith(".jpg"):
            img = Image.open(os.path.join(tumor_dir,filename))
            img = img.convert("RGB")  # Convert to RGB explicitly
            img = img.resize(image_size)
            img = np.array(img) / 255.0 # Normalize pixel values to [0,1]
            x.append(img)
            y.append(1)# Tumor class is labled as 1

    non_tumor_dir = os.path.join(data_dir,'Training','non_tumor')
    for filename in os.listdir(non_tumor_dir):
        if filename.endswith(".jpg"):
            img = Image.open(os.path.join(non_tumor_dir,filename))
            img = img.convert("RGB")  # Convert to RGB explicitly
            img = img.resize(image_size)
            img = np.array(img) / 255.0 #Normalize
            x.append(img)
            y.append(0) # Non_tumor class is labled 0

    x = np.array(x)
    y = np.array(y)


    # Split the data into training and testing sets

    x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = 0.2 , random_state = 42)
    return x_train , x_test ,y_train , y_test


if __name__ == "__main__":
    # Replace "./tcia_dataset" with the path where you want to save the dataset
    output_directory = "./Dataset/2"
    extract_dataset(output_directory)



# dataset from https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset 
# This dataset is a combination of the following three datasets :
# figshare
# SARTAJ dataset
# Br35H

