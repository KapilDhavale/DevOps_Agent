# generators/github_actions_generator.py

import os
from llm_interface import ask

def generate(repo_path: str):
    """Generate a GitHub Actions workflow by prompting the LLM."""
    prompt = (
        "You are a DevOps engineer. Write a GitHub Actions YAML workflow named 'ci.yml' "
        "that on push and pull_request:\n"
        "- Checks out the code\n"
        "- Sets up Python 3.9\n"
        "- Installs dependencies from requirements.txt\n"
        "- Runs pytest\n"
        "Make sure the YAML is valid and concise."
    )

    content = ask(prompt)
    workflows_dir = os.path.join(repo_path, ".github", "workflows")
    os.makedirs(workflows_dir, exist_ok=True)
    out_path = os.path.join(workflows_dir, "ci.yml")
    with open(out_path, "w") as f:
        f.write(content)

    print(f"[WRITE] {out_path}")
