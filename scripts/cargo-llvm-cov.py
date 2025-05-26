import os
import subprocess
from security import safe_command

TARGET = "extra_tests/snippets"

def run_llvm_cov(file_path: str):
    """ Run cargo llvm-cov on a file. """
    if file_path.endswith(".py"):
        command = ["cargo", "llvm-cov", "--no-report", "run", "--", file_path]
        safe_command.run(subprocess.call, command)

def iterate_files(folder: str):
    """ Iterate over all files in a folder. """
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            run_llvm_cov(file_path)

if __name__ == "__main__":
    iterate_files(TARGET)
