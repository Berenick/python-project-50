from gendiff import generate_diff
from fixtures.file_fixture import json_res


file1 = '/home/nickolay/test_data/file1.json'
file2 = '/home/nickolay/test_data/file2.json'

def test_diff(json_res):
    print(generate_diff(file1, file2))
    print(json_res)
    assert generate_diff(file1, file2) == json_res