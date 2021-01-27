import sys,  json, argparse
import read, render

def main():
    # Load settings from json
    with open('config.json') as config_file:
        data = json.load(config_file)

    # Parse and update settings using input arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument("-input_path", default=data['input_path'], type=str)
    args = parser.parse_args()
    
    # Parse input ldr file
    read.parse(args.input_path)
    


if __name__ == '__main__':
    main()
