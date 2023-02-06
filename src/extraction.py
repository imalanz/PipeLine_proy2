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

def delete_food (x):
    # return the cleaining of columns from "food" data base
    x.drop(columns = ["food_category_id", "publication_date", "data_type"], inplace=True, axis=1)
    x.dropna(how="any", inplace=True)
    return x

def delete_nutrient (x):
    # return the cleaining of columns from "nutrient" data base
    x.drop(columns = ["unit_name", "nutrient_nbr", "rank"], inplace= True, axis=1)    
    x.dropna(how="any", inplace=True)
    return x

def merge (nutrition, ids, food):
    # inner merge of the 3 data frames.
    inner_merge = pd.merge(nutrition, ids, on="nutrient_id", how="inner")
    x = pd.merge(inner_merge, food, on="food_id", how="inner")
    usda = x[["food", "nutrient", "Per100g", "food_id", "nutrient_id" ]]
    # cleaning of the ids columns.
    usda.drop(columns = ["food_id", "nutrient_id"], inplace= True, axis=1)
    # cleaning the duplicated.
    return usda

    


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

# concat and creat DF 
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
    

# create individual lists searching for the disease in each text.
def diseases (x):
    enferm = ["beriberi","weight loss","anaemia", "feeling weak and tired", "underdeveloped teeth and bones", "atherosclerosis", "weakness", "angular cheilitis", "chapped", "anemia", "cracked lips", "pellagra", "diarrhoea", "dermatitis", "dementia", "fatigue", "apathy", "irritability", "celiac disease", "crohn", "skin health", "neural tube defects", "methylmalonic acidemia", "scurvy", "skin spots", "nyctalopia", "keratomalacia", "blindness", "rickets", "weakening of bones", "decreased coagulation of blood", "muscle weakness", "nerve weakness", "osteopenia", "nausea", "vomiting", "kidney disease", "loss of taste, smell", "goitre", "hyponatremia", "dehydration", "heart diseases", "muscle contractions", "hypertension"]
    disease = []
    for i in enferm:
        if i in x:
            disease.append(i)
    return (disease)

def diseases_total (n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22):
    # adding all the diseases into one list.
    lst = [n1]+[n2]+[n3]+[n4]+[n5]+[n6]+[n7]+[n8]+[n9]+[n10]+[n11]+[n12]+[n13]+[n14]+[n15]+[n16]+[n17]+[n18]+[n19]+[n20]+[n21]+[n22]
    return lst
    
    
    
def df_diseases (lst):   
    # adding it without a separetion between them.
    nueva = []
    for i in lst:
        nueva.append("/ ".join(i))
    # making it a data frame.
    return pd.DataFrame(nueva)

     
    
def disease_concat (df, enf):
    # para concat las tablas
    x = pd.concat([df, enf], axis=1)
    x[[]]
    return 


