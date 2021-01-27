# We want to return points and part types for each part in the model, along with a bill of material count
from pandas import read_csv
from collections import Counter
import numpy as np


# open and parse to numpy array in the form of
# 1 <colour> x y z a b c d e f g h i <file>
# https://www.ldraw.org/article/218.html

def parse(file_name):
    try:
        file_path = "ldr/" + file_name + ".ldr"
        file = open(file_path, "r")
        combined_data = read_csv(file_path, sep='\s+', header=None).to_numpy()
    except:
        print('Unable to find and open the .ldr file')

    # Convert part .dat identifier to an int 
    for i ,part in enumerate(combined_data[:,-1]):
        combined_data[i,-1] =  int(part.replace(".dat",""))
    
    # TODO: look at making lego object that has color, location, etc. 

        np.slice(combined_data,5,9)


    bom = generate_bom(combined_data)


# generate bill of materials of unique parts
def generate_bom(data):
    identifiers = [data[:, 14], data[:, 1]]
    bom = []
    type(identifiers)
    for i, identifier in enumerate(identifiers):
        print(identifier)


if __name__ == '__main__':
    parse()
