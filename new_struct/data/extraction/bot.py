import os
import json
import csv
import pandas as pd

dico_list = []
count = 0
for filename in os.listdir("./data"):
    if count % 10000 == 0: print(count)
    with open('./data/'+filename) as json_data:
        data_dict = json.load(json_data)
        dico_list.append(data_dict)
    count += 1


df = pd.DataFrame.from_dict(dico_list)
df.to_csv(r'ulule_data.csv', index=False, header=True)


