import os
import json
from deepdiff import DeepDiff
from pprint import pprint


class TestEngine:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def _get_tests_in_folder(self, folder):
        json_files = []
        for path, subdirs, files in os.walk(folder):
            for name in files:
                file_path = os.path.join(path, name)
                if file_path.endswith(".json"):
                    with open(file_path, "r") as f:
                        json_files.append(json.loads(f.read()))
        return json_files

    def _build_template(self):
        raise NotImplementedError

    def run(self):
        total_tests = 0
        failed_tests = 0
        passed_tests = 0
        for json_test in self._get_tests_in_folder("testing"):
            diff = DeepDiff(
                json_test["expected"],
                self._build_template(json_test["template"], json_test["data"]),
            )
            if diff:
                print(f"    ❌ {json_test['description']} - Failed!")
                pprint(diff, indent=2)
                failed_tests += 1
            else:
                print(f"    ✅ {json_test['description']} - Passed!")
                passed_tests += 1
            total_tests += 1
        return {"total": total_tests, "failed": failed_tests, "passed": passed_tests}
