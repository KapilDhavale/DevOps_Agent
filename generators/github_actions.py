# generators/github_actions.py

import os
from jinja2 import Environment, FileSystemLoader

def generate(repo_path: str):
    """Generate a GitHub Actions CI workflow from a Jinja template."""
    template_dir = os.path.join(os.getcwd(), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))
    tpl = env.get_template("github_workflow.yml.j2")

    content = tpl.render()
    workflows_dir = os.path.join(repo_path, ".github", "workflows")
    os.makedirs(workflows_dir, exist_ok=True)
    out_path = os.path.join(workflows_dir, "ci.yml")
    with open(out_path, "w") as f:
        f.write(content)
    print(f"[WRITE] {out_path}")
