from llm_interface import prompt_llm

def suggest_tests(project_path):
    prompt = f"Generate a basic pytest-style test file for a Python project in '{project_path}'."
    result = prompt_llm(prompt)
    print("\n[Generated Test Code]:\n")
    print(result)
