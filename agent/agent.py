# agent/agent.py

import os
from generators.test_generator import suggest_tests
from generators.cicd_generator import suggest_cicd

class DevOpsAgent:
    def __init__(self, path):
        self.project_path = path

    def run(self):
        print(f"[+] Scanning {self.project_path}...\n")

        # Step 1: Check for tests
        has_tests = any('test' in f.lower() for f in os.listdir(self.project_path))
        if not has_tests:
            print("[!] No tests found.")
            suggest_tests(self.project_path)

        # Step 2: Check for CI/CD
        workflows_path = os.path.join(self.project_path, ".github", "workflows")
        if not os.path.exists(workflows_path):
            print("[!] No CI/CD workflows found.")
            suggest_cicd(self.project_path)

        print("\n[✓] Scan Complete.")

# ✅ Add this function so it can be called from CLI
def run_agent(path):
    agent = DevOpsAgent(path)
    agent.run()
