import logging
import os
import json
import yaml
from minerva import Template
from pydantic import BaseModel

class MinervaTemplate(BaseModel):
    name: str
    repo: str
    version: str
    script: str
    working_dir: str


class MinervaClient:
    @staticmethod
    def get_minerva_templates():
        config_path = os.path.join(os.path.dirname(__file__), './resources/templates.yaml')
        with open(config_path, 'r') as f:
            template_config = yaml.load(f.read(), Loader=yaml.Loader)
            repo = template_config["minerva-templates"]["repo"]
            version = template_config["minerva-templates"]["version"]
            templates = template_config["templates"]
            return [MinervaTemplate(name=template,
                                    repo=repo,
                                    version=version,
                                    script=templates[template]['script'],
                                    working_dir=templates[template]['working_dir']) for template in templates.keys()]

    def register_templates(self, project_name):
        templates = self.get_minerva_templates()
        for templ in templates:
            t = Template(name=templ.name,
                         project_name=f"{project_name}/Templates",
                         version=templ.version)
            t.register(repo=templ.repo,
                       script=templ.script,
                       working_dir=templ.working_dir
                       )
            
            

if __name__ == '__main__':
  project_name = "simple_pipeline_project"
  minervaclient = MinervaClient()
  minervaclient.register_templates(project_name)
  
  