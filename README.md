# PipeLines _proy2

![portada](https://github.com/imalanz/pipe/blob/main/Imagenes/1.jpg?raw=true) 

# Supreme ultimate food!.
Whats the most powerfull food, by this I mean, wich food in particular is the one that has the most valriable nutrients, that helps you with some diseases.

### Since when to a good eating habbits we started named it diet?

Theres always a feeling of sicknes walking throw our body, and the first thing most of people do is to go to the nearest farmaci and swalow bunch of pills every day, what if I tell you that everything you need is inside the food you eat, just have to know what type of food is good for what disease.

In this proyect I´m going to compare just a few diseases and what lack of nutrients cause them. and from that I would gather the information to check witch food is the one that contains the most common nutrients that this few diseases add, that food would become the supreme ultimate food.

![dolor](https://raw.githubusercontent.com/imalanz/pipe/main/Imagenes/7.avif) 
## Data analsys.
I investigate from 2 sites, the USDA data base that it was already available for us in a .csv format and from a web page that gives us information about some diseases and their lack of nutrients.
### 1. USDA database.
The USDA database of foods its really extense and complete with more than 1,185,081 foods. Its a data base of all the aliments that are in the market to buy in the United states. They have a lot of information like: the lab proceses, where they sell them, wich store, and what we are interested is the nutrients they have.

I had to do a lot od cleaning and searching for what it acctualy it was going to be helpfull for the proyect. Had to:

- Did some searching and selection of the dataframes that I would need, from the almost 15 tables I stay with 3 or 4.
- Had to do some cleanng on the columns that each dataframe had, stayed with just a few of them.
- Needed to change the names of the left columns, to matched the same value in the different dataframes.
- Merged the cleaned and filtered dataframes to a unique one, with only the information that would be helpful for this proyect
- Deleted all the duplicated columns and grouped it by the name of the food, there where acctualy a lot of food with the same name but they where different product, different brand. 

![duda](https://github.com/imalanz/pipe/blob/main/Imagenes/4.jfif?raw=true) 
### 2. Health web scraping.
I got this information from the Encyclopedia Britannica web page, I started looking for diseases and what acctualy couse them, but at the end I got to a page with complete oposite information, "what lack of nutrients causes what disease" but it was still a good information. I had to:

- Do some web scraping, looking for the texts and the title of the text that in this case it was the acctual nutrient.
- From that text I had to look for some key words that meant the diseases it self and separete them from the text.
- Everything put it in an ordered data frame.


![duda](https://github.com/imalanz/pipe/blob/main/Imagenes/8.png?raw=true)  
### 3. Analizing.
After creating both tables with the information that we wanted, its time to merge the information to a single dataframe. 
For that I had to do some filtering in the USDA data frame with the nutrients that apear in the diseases table, because we are only focusing on some specific nutrients that causes some diseases. 

After filtering, I created a formula that filters more the big data frame to some specific parameters, that you can choose puting them in the formula and the output will be the filter table with the parameters you input
From those filtered information I created graphics to analize clearly the information.

1. we can see the foods with the most cuantity of nutrients, more than 14 diferent types of nutrients, and how many grams in total they have. 
it looks that the butter has the most of them. 2. A list of food with no more than 12 different types of nutrients and more than 10,000 amount of grams, this is a more equilibrated graphs and still powerfull foods.

![visual](https://github.com/imalanz/PipeLine_proy2/blob/main/Imagenes/paint1.jpg?raw=true)  



3. Can see that the cooked liver food with bread is powerful. and has more than 20,000 grams, but we can see that also the bananas shake or high protein shake its also has good amount of nutrients. 

![visual](https://github.com/imalanz/PipeLine_proy2/blob/main/Imagenes/paint2.jpg?raw=true) 

### 4. Conclution. 
It depends of what acctualy is what we are loocking for, because I can have the aliment with the most number of diferent nutrients but that doesnt mean that it has the most cuantity per grams.

1. The most powerful food on cuantity of mixed nutrients per 100g is .....

2. The most equilibrated food by the number of nutrients and the cuantity of grams, that still a high number is ...


![feliz](https://raw.githubusercontent.com/imalanz/pipe/main/Imagenes/healthy%208.avif)  

