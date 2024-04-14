import argparse
from .parser import gener_diff
from .parser import make_dict


def main():
    argparsing()


def argparsing():
    parser = argparse.ArgumentParser(description='Compares two configuration'
                                     'files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, metavar='FORMAT')
    args = parser.parse_args()
    file1, file2 = make_dict(args.first_file, args.second_file)
    print(gener_diff(file1, file2))


if __name__ == "__main__":
    main()
