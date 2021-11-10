import os
from time import sleep
header = "const char PROGMEM = R\"=====("
trailer = ")=====\";"
temp = {};
files = os.listdir()
for file in files:
    if os.path.isfile(file):
        if file.endswith(".htm") or file.endswith(".html") or file.endswith(".css") or file.endswith(".js"):
            temp[file[ : file.rindex(".")]] = open(file, 'r').read()
            
while(1):
    sleep(1)
    files = os.listdir()
    for file in files:
        if os.path.isfile(file):
            if file.endswith(".htm") or file.endswith(".html") or file.endswith(".css") or file.endswith(".js"):
                fileName = file[ : file.rindex(".")];
                modifiedHeader = header[: header.index("P")] + "_"+fileName + "[] " + header[header.index("P") : ]
                filePoint = open(file, 'r')
                content = filePoint.read()
                if(content == temp[fileName]):
                    continue
                print(f"{file} changed")
                temp[fileName] = content
                fileContent = modifiedHeader +"\n"+ temp[fileName] +"\n"+ trailer;
                filePoint.close()
                
                filePoint = open(fileName+".h", "w")
                filePoint.write(fileContent)
                filePoint.close()
            

