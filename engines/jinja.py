import os
import jinja2
import json

from .common import TestEngine

environment = jinja2.Environment()

JINJA_FOLDER = "templates-jinja"


class JinjaTestEngine(TestEngine):
    def _build_template(self, template_file, data):
        with open(os.path.join(JINJA_FOLDER, template_file), "r") as f:
            template = environment.from_string(f.read())
            return json.loads(template.render(data))
