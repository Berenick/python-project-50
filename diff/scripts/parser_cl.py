import argparse


def argparsing():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str) 
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, metavar='FORMAT')
    args = parser.parse_args()