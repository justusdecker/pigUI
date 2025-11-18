import os, subprocess, sys
def run_git_command(command_list):
    """Runs a git command and returns the output."""
    try:
        result = subprocess.run(
            command_list,
            capture_output=True,
            text=True,
            check=False,
            cwd=os.getcwd()
        )
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except FileNotFoundError:
        err("Error: 'git' command not found. Ensure Git is installed and in your PATH.")
        exit(1)
def err(text: str) -> str:
    return f'\033[33m{text}\033[0m'
def main():
    for root, _, files in os.walk(os.getcwd()):
        if '.git' in root:
            
            continue
                
        for file_name in files:
            file_path = os.path.join(root, file_name)

            relative_path = os.path.relpath(file_path, os.getcwd())

            print(f"Processing File: {relative_path}")
            
            run_git_command(["git", "add", relative_path])

            _, _, returncode = run_git_command(["git", "diff", "--cached", "--quiet", relative_path])

            if returncode == 0: 
                err(f"SKIP: No changes detected for '{relative_path}' since last commit.")
                continue
            
            while True:
                commit_msg = input(f"Enter commit message for '{relative_path}': ").strip()
                if commit_msg:
                    break
                err("Commit message cannot be empty.")
            
            stdout, stderr, returncode = run_git_command([
                "git", "commit", "-m", commit_msg, relative_path
            ])

main()