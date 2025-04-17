import os
import subprocess
import sys

cwd = os.getcwd()

def run_python(filename) -> bool:
    try:
        result = subprocess.run([sys.executable, filename], check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error while executing {filename} \n {e}")
        return False

def run_bash(filename) -> bool:
    try:
        result = subprocess.run(["bash", filename], check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error while executing {filename} \n {e}")
        return False

def run_scripts():
    scripts = ["create_dir.sh", "get_logs.py", "coloring_logs.py", "taring.sh", "count_tar.py"]
    for script in scripts:
        path_to_script = os.path.join(cwd, script)
        if path_to_script.endswith(".py"):
            success = run_python(path_to_script)
        elif path_to_script.endswith(".sh"):
            success = run_bash(path_to_script)
        else:
            sys.exit(1)

if __name__ == "__main__":
    run_scripts()
