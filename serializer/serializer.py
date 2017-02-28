from __future__ import print_function

import base64
import json
import sys


def jsonize(filename):
    contents = ''
    with open(filename) as f:
        contents = f.read()
    encoded = base64.b64encode(contents)
    json_dict = {'contents':    encoded,
                 'language':    'python',
                 'version':     '1'}
    return json.dumps(json_dict)

def extract(json_str):
    json_dict = json.loads(json_str)
    encoded = json_dict['contents']
    return base64.b64decode(encoded)


if __name__ == '__main__':
    json_str = jsonize(sys.argv[1])
    print(json_str)
    print('==============================')
    print(extract(json_str))
