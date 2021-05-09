# We want to return points and part types for each part in the model, along with a bill of material count
from pandas import read_csv
from collections import Counter
import numpy as np
import os
import config


# open and parse to numpy array in the form of
# 1 <colour> x y z a b c d e f g h i <file>
# https://www.ldraw.org/article/218.html


def parse(file_name):
    class Brick:
        def __init__(self, color, x, y, z):
            self.color = color
            self.y = y
            self.z = z
            self.x = x

    try:
        file_path = "ldr/" + file_name + ".ldr"
        file = open(file_path, "r")
        combined_data = read_csv(file_path, sep='\s+', header=None).to_numpy()
    except:
        print('Unable to find and open the .ldr file')
   
    # print(combined_data)
    # ind = np.lexsort((combined_data[:,1],combined_data[:,0]))
    # print(ind)

    
    # Convert part .dat identifier to an int
    bricks = []
    for i, part in enumerate(combined_data[:, -1]):
        combined_data[i, -1] = int(part.replace(".dat", ""))
        bricks.append(Brick(combined_data[i, 1], combined_data[i, 2],
                            combined_data[i, 4], -combined_data[i, 3]/24))
    print(combined_data)
    bom = generate_bom(bricks)
    config.bricks = bricks


# generate bill of materials of unique parts
def generate_bom(data):
    if not os.path.exists(str(config.output_path)):
        os.mkdir(str(config.output_path))
    file_path = str(config.output_path) + "/bom.txt"
    file = open(file_path, "w")
    file.write("Bricks Needed:\n\n")

    colors = []
    written = 0
    for i in range(len(data)):
        colors.append(data[i].color)
    color_array = np.array(colors)
    unique, counts = np.unique(color_array, return_counts=True)

    for pos, i in enumerate(config.color_lookup):
        for j in range(len((unique))):
            if unique[j] == i[1]:
                pos += 1
                if pos > config.channel_num:
                    pos = "error, overflow!"
                else:
                    pos = str(pos)

                file.write(str(counts[j]) + " " + str(i[0]) +
                           " loaded in position " + pos+"\n\n")

                written += 1

    if written != len(unique):
        dif = len(unique)-written
        if dif > 1:
            color_txt = "colors"
            plural_txt = "They"
            dont_txt = "don't"
        else:
            color_txt = "color"
            plural_txt = "It"
            dont_txt = "doesn't"
        file.write(str(dif) + " unique " + color_txt +
                   " found in .ldr which " + dont_txt + " correspond to " + color_txt + " in config.py. " + plural_txt + " will not be built.")


if __name__ == '__main__':
    parse(config.input_path)
