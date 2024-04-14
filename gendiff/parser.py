from itertools import chain
import json
import yaml


def gener_diff(file1, file2):
    print(f'gener:{file1}')
    print(f'gener{file2}')
    res = []
    keys = sorted(list(set([k for k in chain(file1.keys(), file2.keys())])))
    for key in keys:
        v1 = file1.get(key)
        v2 = file2.get(key)
        if v1 is not None and v2 is not None:
            if file1.get(key) == file2.get(key):
                res.append(f'    {key}: {file1.get(key)}')
            else:
                res.append(f'  - {key}: {v1}')
                res.append(f'  + {key}: {v2}')
        elif v1 is not None and v2 is None:
            res.append(f'  - {key}: {v1}')
        elif v1 is None and v2 is not None:
            res.append(f'  + {key}: {v2}')
    a = '\n'.join(res)
    return '{\n' + a + '\n}'


def make_dict(first_file, second_file):
    file_format = first_file.rsplit('.', 1)
    if file_format[1] == 'yaml' or file_format[1] == 'yml':
        dict1 = yaml.load(open(first_file), Loader=yaml.FullLoader)
        dict2 = yaml.load(open(second_file), Loader=yaml.FullLoader)
    elif file_format[1] == 'json':
        dict1 = json.load(open(first_file, 'r'))
        dict2 = json.load(open(second_file, 'r'))
    return dict1, dict2
