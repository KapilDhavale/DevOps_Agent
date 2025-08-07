from llm_interface import prompt_llm

def suggest_cicd(project_path):
    prompt = f"Generate a GitHub Actions YAML workflow for Python testing in the project '{project_path}'."
    result = prompt_llm(prompt)
    print("\n[Generated CI/CD Workflow]:\n")
    print(result)
