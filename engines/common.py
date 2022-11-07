import os
import json
from deepdiff import DeepDiff
from pprint import pprint

def get_tests_in_folder(folder):
    json_files = []
    for path, subdirs, files in os.walk(folder):
        for name in files:
            file_path = os.path.join(path, name)
            if file_path.endswith(".json"):
                with open(file_path, 'r') as f:
                    json_files.append(json.loads(f.read()))
    return json_files


def run_tests(build_template_fn):
    for json_test in get_tests_in_folder("testing"):
        diff = DeepDiff(
            json_test['expected'],
            build_template_fn(json_test['template'], json_test['data'])
        )
        if diff:
            print (f"❌ {json_test['description']} - Failed!")
            pprint(diff, indent=2)
        else:
            print (f"✅ {json_test['description']} - Passed!")