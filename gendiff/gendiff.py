import argparse
import json
from itertools import chain


def main():
    argparsing()


def argparsing():
    parser = argparse.ArgumentParser(description='Compares two configuration'
                                     'files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, metavar='FORMAT')
    args = parser.parse_args()
    print(gener_diff(args.first_file, args.second_file))


def gener_diff(filename1, filename2):
    js1 = json.load(open(filename1))
    js2 = json.load(open(filename2))
    res = []
    keys = sorted(list(set([k for k in chain(js1.keys(), js2.keys())])))
    for key in keys:
        v1 = js1.get(key)
        v2 = js2.get(key)
        if v1 is not None and v2 is not None:
            if js1.get(key) == js2.get(key):
                res.append(f'    {key}: {js1.get(key)}')
            else:
                res.append(f'  - {key}: {v1}')
                res.append(f'  + {key}: {v2}')
        elif v1 is not None and v2 is None:
            res.append(f'  - {key}: {v1}')
        elif v1 is None and v2 is not None:
            res.append(f'  + {key}: {v2}')
    a = '\n'.join(res)
    return '{\n' + a + '\n}'


if __name__ == "__main__":
    main()
