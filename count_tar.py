import os
import re

def tars(files):
    temp = files.copy()
    try:
        for i in range(len(temp)-1, -1, -1):
            match = re.search(r'my_syslog\.tar\.(\d+)\.gz', temp[i])
            if match:
                num = int(match.group(1))
                new_num = num + 1
                temp[i] = f"my_syslog.tar.{new_num}.gz"
            elif temp[i] == "my_syslog.tar.gz":
                temp[i] = "my_syslog.tar.1.gz"
            else:
                continue
        return temp
    except Exception as e:
        print(f"Error in tars(): {e}")
        return []

def rename_tar(files):
    if not files:
        return 0
    
    def sort_key(f):
        match = re.search(r'my_syslog\.tar\.(\d+)\.gz', f)
        if match:
            return int(match.group(1))
        elif f == "my_syslog.tar.gz":
            return 0
        return -1
    
    sorted_files = sorted(files, key=sort_key)
    new_names = tars(sorted_files)
    
    if not new_names:
        return 0
    
    for old, new in zip(reversed(sorted_files), reversed(new_names)):
        try:
            os.rename(old, new)
        except OSError as e:
            print(f"Can't rename file {old} to {new}: {e}")

if __name__ == "__main__":
    cwd = os.getcwd()
    files = [f for f in os.listdir(cwd) if f.startswith("my_syslog.tar") and f.endswith(".gz")]
    rename_tar(files)
