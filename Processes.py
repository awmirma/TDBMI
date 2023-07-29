from tciaclient.core import TCIAClient
# print("ttt")
# def load_TCIA_data():
print("start downloading...")
tc = TCIAClient()
collection_name = "NSCLC-Radiomics"
series = tc.get_series(collection=collection_name, modality="CT")
download_path = "./tcia-downloads"
for i, s in enumerate(series):
    print(i)
    tc.get_image(seriesInstanceUid = s["SeriesInstanceUID"],
        downloadPath = download_path, zipFileName = str(i).zfill(3)+"-"+collection_name+".zip")
    
print("\nDownload complited . Saved in ./tcia_downloads")