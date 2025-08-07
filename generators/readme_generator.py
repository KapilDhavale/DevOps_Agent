# generators/readme_generator.py

import os
from llm_interface import ask
from utils.file_ops import list_repo_files

def generate(repo_path: str):
    """Generate a README.md by prompting the LLM."""
    files = list_repo_files(repo_path)
    project_name = os.path.basename(repo_path)

    prompt = (
        f"You are a helpful documentation generator. The project is named '{project_name}', "
        f"and contains these files:\n{files}\n\n"
        "Write a comprehensive README.md including:\n"
        "- Project description\n"
        "- Installation steps\n"
        "- Usage examples\n"
        "- How to run tests\n"
    )

    content = ask(prompt)
    out_path = os.path.join(repo_path, "README.md")
    with open(out_path, "w") as f:
        f.write(content)

    print(f"[WRITE] {out_path}")
