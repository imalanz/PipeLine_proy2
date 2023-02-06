import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import json_normalize
import requests
import re
import lxml
import json
import os
from dotenv import load_dotenv
import time

# USDA data csv.

def import_csv (url):
    # import data from csv to pandas.
    return pd.read_csv(url)






# web scraping
     
def get_text(url):
    #encontrar los datos 
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"html.parser")
    
    return soup.find_all("span")


def text_filtered(tags_index):
    # lista de el nutriente y su texto limpio.
    x = []
    y = []
    for i in tags_index:
        x.append(i.getText())
    for i in x:   
        y.append(i.replace(".\xa0", "").strip().lower())

    return y


def db_concat (lst1, lst2, lst3):
    # crear cada lista a dataframe, se crea en una sola columna
    df1 = pd.DataFrame(lst1)
    df2 = pd.DataFrame(lst2)
    df3 = pd.DataFrame(lst3)
    # separar cada df a 2 columnas, nutriente e info.
    df1 = pd.DataFrame(df1[0].values.reshape(-1, 2), columns=['nutrients', 'info'])
    df2 = pd.DataFrame(df2[0].values.reshape(-1, 2), columns=['nutrients', 'info'])
    df3 = pd.DataFrame(df3[0].values.reshape(-1, 2), columns=['nutrients', 'info'])
    #concatinate the 3 database in 1
    return pd.concat([df1, df2, df3], axis=0)

def get_name (url):
    #to get the names of the vitamin from each of the pages.
    
        
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"html.parser")
    tags = soup.find_all("h2")
    x = [i.getText() for i in tags]
    
    disease = ["dry skin", "hair loss", "impaired wound healing"]
    tags = soup.find_all("p")
    
    for i in tags:
        tag_text = i.getText()

    tag_text = tag_text.replace(",", "").strip()

 
    y = [i for i in disease if i in tag_text]

    return x, y


#def get_sickness (nutrient):
    #to filter the sickness from the text from each title.
