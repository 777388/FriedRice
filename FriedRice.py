import sys
import os
import re
from blessed import Terminal
print(Terminal().center("You got it"))
target = sys.argv[1] 
i = 0
with open('rootservers.txt', 'r+') as file:
    for line in file:
        i += 1
        c = os.popen("dig +trace +noidnin +noidnout "+line.rstrip()).read()
        ips = [match.group(1) for match in re.finditer(r'\b((?:\d{1,3}\.){3}\d{1,3})(?:\d+)?\b', c)]
        ipp = '\n'.join(ips)
        file.write(ipp)
        z = os.system("hellfire --txt --file=rootservers.txt")
        x = os.system("gau "+str(target)+" --o "+str(target)+str(i)+".txt")
            
print("diff -u "+str(target)+"1.txt "+str(target)+"2.txt > a.txt")
