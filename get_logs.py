from count_logs import *
import os

cwd = os.getcwd()
path = cwd + "/my_syslog/my_syslog.log"

def main():
    with open("/var/log/syslog", "r") as get:
        try:
            logs = get.read()
            print("success reading syslog")
        except:
            print("error reading syslog")

    shift = syslog_rename("my_syslog.log")
    
    with open(path, "w") as put:
        try:
            put.write(logs)
            ("success writing syslog to my_syslog.log")
        except:
            print(f"fail writing syslog to my_syslog.log")



if __name__ == "__main__":
    main()
