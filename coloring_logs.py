from colorama import Fore
import os

cwd = os.getcwd()
file = cwd + "/my_syslog/my_syslog.log"

def main():
    f = [i for i in open(file).readlines()]
    for line in f:
        index = 0
        line = line.split()
        other = ""
        i = 4
        if "Warning:" in line:
            index = line.index("Warning:")
            i = 5
        while line:
            try:
                other += line[i] + " "
                i += 1
            except:
                break
        if "Warning:" in line and line.index("Warning:")!=3:
            print(Fore.GREEN + line[0], Fore.LIGHTYELLOW_EX + line[1], Fore.BLUE + line[2], Fore.RED + line[3],Fore.RED + line[4],Fore.CYAN+other,Fore.WHITE, sep=" ")
        else:
            try:
                print(Fore.GREEN + line[0], Fore.LIGHTYELLOW_EX + line[1], Fore.BLUE + line[2], Fore.RED + line[3], Fore.CYAN+other,Fore.WHITE, sep=" ")
            except:
                print(Fore.GREEN + line[0], Fore.LIGHTYELLOW_EX + line[1], Fore.BLUE + line[2], Fore.WHITE,sep=" ")

if __name__ == "__main__":
    main()
