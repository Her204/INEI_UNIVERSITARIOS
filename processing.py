import geopandas as gpd
import pandas as pd
import os
import matplotlib.pyplot as plt

files = {}

for dirnames,_,files_1 in os.walk(os.getcwd()):
    for file in files_1:
        if file.endswith(".dbf"):
            df = gpd.read_file(os.path.join(dirnames,file))
            df = df[[a for a in df.columns 
                    if len(df[a].unique())>=2]]
            #df = df.dropna(axis=1)
            files[dirnames]= df   

print(files)






















