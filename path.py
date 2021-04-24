import config


def prepare():
    bricks = config.bricks
    file_path = str(config.output_path) + "/gcode.txt"
    file = open(file_path, "w")
    file.write("(Made by Matt using LegoPrinter.py)\n")

    # Firstly, sort by decreasing z then sort by same color? --- sort while it's still a numpy array in read.py

    # from bricks we have pickup location from bricks[1].color corresponding to a color lookup which is in a certain spot in color_lookup
    #  which corresponds to index in pickup position - lower z
    # then we can triangulate and move to the right position - optimization comes from sorting by same color since trip needs to be taken anyway
    # raise z and actuate solenoid
    # lower z and deactuate solenoid - repeat pickup


def togcode():
    print("to gcode")


# def pick()):

# def goto():

# def place():
