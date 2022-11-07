import os
import jinja2
import json

from .common import get_tests_in_folder, run_tests

environment = jinja2.Environment()

JINJA_FOLDER = 'templates-jinja'


def _build_template(template_file, data):
    with open(os.path.join(JINJA_FOLDER, template_file), 'r') as f:
        template = environment.from_string(f.read())
        print(template.render(data))
        return json.loads(template.render(data))

def test_jinja():
    run_tests(_build_template)