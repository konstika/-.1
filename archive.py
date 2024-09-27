import tarfile
import os

tar = tarfile.open('archive.tar', mode='w')
f = open("file1.txt","w")
f.write("This is file 1")
f.close()
f = open("file2.txt","w")
f.write("This is file 2")
f.close()
f = open("file3.txt","w")
f.write("This is file 3")
f.close()

if not os.path.isdir("mydir"):
    os.mkdir("mydir")
    
f = open("file4.txt","w")
f.write("This is file 4!\nBye bye!")
f.close()
os.replace("file4.txt", "mydir/file4.txt")


tar.add("mydir")
tar.add("file1.txt")
tar.add("file2.txt")
tar.add("file3.txt")

os.remove(os.path.join(os.getcwd(),"mydir/file4.txt"))
os.rmdir(os.path.join(os.getcwd(),"mydir"))
os.remove(os.path.join(os.getcwd(),"file1.txt"))
os.remove(os.path.join(os.getcwd(),"file2.txt"))
os.remove(os.path.join(os.getcwd(),"file3.txt"))

tar.close()

print("Файловая система создана.")
