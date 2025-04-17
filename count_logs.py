import os

nam = "my_syslog"
cwd = os.getcwd()
#cur_path_file = cwd + "/" + name
main_dir = cwd + "/" + nam
files = [f for f in os.listdir(main_dir) if os.path.isfile(os.path.join(main_dir, f))]
d = []
def greatest_num(name):
    number = []
    if files == []:
        return 1
    for i in files:
        if name in i:
            d.append(i)
    for i in d:
        if i[-1].isdigit():
            number.append(i[-1])
    return number
def rename_file(d):
    new = []
    for i in range(len(d)):
        test = d[i]
        try:
            test = test.replace(test[-1], str(int(test[-1])+1))
            new.append(test)
        except:
            test += ".1"
            new.insert(0,test)
    return new

def syslog_rename(name):
    number = greatest_num(name)
    renamed = rename_file(d)
    d.sort(reverse=True)
    renamed.sort(reverse=True)
    for i in range(len(d)):
        cur_path_file = cwd + "/" + nam  + "/" + d[i]
        if os.path.exists(cur_path_file):
            try:
                old_path = os.path.join(main_dir, d[i])
                new_path = os.path.join(main_dir, renamed[i])
                os.rename(old_path, new_path)
            except OSError as e:
                print(f"Can't rename the file {e}")

