# Case study of iris dataset
# calculating area of sepal length and petal length
# author: Atacan Buyuktalas

import csv

FILENAME = "iris.csv"
DATADIR = "my_work/lectures/datafiles/"

with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.DictReader(fp, delimiter=",", quoting= csv.QUOTE_NONE)  
    
    for line in reader: 
        sepal_size = line["sepal_length_cm"] * line["sepal_width_cm"]
        petal_size = line["petal_length_cm"] * line["petal_width_cm"]
        line.append(sepal_size)
        line.append(petal_size)
        print (line)