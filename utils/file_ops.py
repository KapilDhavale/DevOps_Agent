# utils/file_ops.py

import os

def list_repo_files(repo_path: str) -> list[str]:
    """Return a list of all file paths (relative) in the repo."""
    files = []
    for root, _, filenames in os.walk(repo_path):
        for name in filenames:
            rel = os.path.relpath(os.path.join(root, name), repo_path)
            files.append(rel)
    return sorted(files)
