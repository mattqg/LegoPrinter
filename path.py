import config


def prepare():
    bricks = config.bricks
    file_path = str(config.output_path) + "/gcode.txt"
    file = open(file_path, "w")
    file.write("(Made by Matt using LegoPrinter.py)\n")
    

    [location]






def togcode():
    print("to gcode")