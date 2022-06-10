#coding=utf=8

import re
import os

def Csection(): # C段切割
    ok=open("c.txt","w+")
    for string_ip in open("ip.txt"):
        result = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){2}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", string_ip)
        ok.write(",".join(result)+"\n")
        ok.flush()
        print(",".join(result))

def duplicateremoval():# C段去重
    list01 = []
    for i in open("c.txt"):
        if i in list01:
            continue
        list01.append(i)
    with open("c-01.txt","w") as s:
        s.writelines(list01)

def C_section():# C段组合
    ok=open("c-ok.txt","w+")
    for Cd in open("c-01.txt","r"):
        ok.write(Cd.strip()+".0/24\n")
        ok.flush()
        print(Cd.strip()+".0/24")
    os.system("del /F /S /Q c-01.txt&del /F /S /Q c.txt")
    

if __name__ == '__main__':
    Csection()
    duplicateremoval()
    C_section()
