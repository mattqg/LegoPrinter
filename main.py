import sys
import json
import argparse
import config
import read
import path


def main():
    # Parse and update settings using input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-input_path", default=config.input_path, type=str)
    parser.add_argument("-output_path", default=config.output_path, type=str)
    args = parser.parse_args()

    # Parse input ldr file, output to config.bricks and bom.txt
    read.parse(args.input_path)
    path.prepare()
    path.togcode()
    # render.drawpath()


if __name__ == '__main__':
    main()
