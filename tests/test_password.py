import pytest
import re
import yaml
import glob

yaml_environment = "./environments/**/*.y*ml"

def yaml_find(path):
    for i in glob.glob(path, recursive=True):
        yield i

def yaml_parse(path):
    data = {}
    with open(path) as f:
        data = yaml.load(f, Loader=yaml.BaseLoader)
    return data

@pytest.mark.parametrize("path", yaml_find(yaml_environment))
def test_password(path):
    var_pattern = re.compile('p(ass(word|wd)?|wd)$')
    val_pattern = re.compile('(\\$ANSIBLE_VAULT\\;.*|\\{{2}.*\\}{2})')
    parsed = yaml_parse(path)

    for k, v in parsed.items():
        if var_pattern.search(k):
            print(f'{ k }: { v }')
            assert val_pattern.search(v)
