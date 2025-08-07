# cli/entrypoint.py

import argparse
from agent.agent import run_agent  # ✅ Now this will work

def run_cli():
    parser = argparse.ArgumentParser(description="DevOps Agent CLI")
    parser.add_argument("path", help="Path to the project to scan")

    args = parser.parse_args()
    run_agent(args.path)
