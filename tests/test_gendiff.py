from gendiff import generate_diff
from gendiff import make_dict
from .fixtures import json_res


file1 = 'tests/fixtures/file1.json'
file2 = 'tests/fixtures/file2.json'
yam_file1 = 'tests/fixtures/file1.yaml'
yam_file2 = 'tests/fixtures/file2.yaml'


def test_diff(json_res):
    f1, f2 = make_dict(file1, file2)
    yf1, yf2 = make_dict(yam_file1, yam_file2)
    assert generate_diff(f1, f2) == json_res
    assert generate_diff(yf1, yf2) == json_res


# def test_dict_maker():
#     print(make_dict(file1, file2))
#     assert make_dict(file1, file2) == dict(json_res)

