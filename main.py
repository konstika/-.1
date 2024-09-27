import tarfile
import socket
import os
import sys

with tarfile.open(os.path.join(os.getcwd(),'archive.tar'),'r') as tar:
    root = "archive.tar"
    currentDirectory = root
    i=1
    while True:
        inviting = socket.gethostname()+" >> "
        if(len(sys.argv)>1):
            command = sys.argv[i]
            i = i+1
            print(inviting+command)
        else:
            command = input(inviting)
        if command == 'ls':
            if currentDirectory == root:
                for name in tar.getnames():
                    if not ('/') in name:
                        print(name)
            else:
                for name in tar.getnames():
                    if (currentDirectory+'/') in name:
                        print((name.split(currentDirectory+'/')[1]).split("/")[0])
                    
        elif command == "exit":
          break
        
        elif command.startswith('cat '):
            path = command.split()[1]
            if currentDirectory!=root:
                path = currentDirectory+"/"+path
            if(path in tar.getnames()):
                content =tar.extractfile(path).read()
                print(content)
            else:
                print("The file was not found.")
          
        elif command.startswith("cd"):
            if len(command.split())>1:
                path=command.split()[1]
                if currentDirectory!=root:
                    path = currentDirectory+"/"+path
                if(path in tar.getnames()):
                    currentDirectory=path
                else:
                    print("The file was not found.")
            else:
                currentDirectory=root
                
        elif command.startswith("wc"):
            path = command.split()[1]
            if currentDirectory!=root:
                path = currentDirectory+"/"+path
            if(path in tar.getnames()):
                content = tar.extractfile(path).read()
                print(len(content.splitlines()),len(content.split()),len(content),path.split("/")[-1])
            else:
                print("The file was not found.")

        elif command=="--file_system":
            print(os.path.join(os.getcwd(),'archive.tar'))
        elif command=="--start_script":
            print(os.path.join(os.getcwd(),'start_script.py'))
        else:
            print("The command was not found.")
