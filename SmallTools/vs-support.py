import os
import shutil

dest = input("Your destination for .vscode: ")
src = 'D:\\Basic_Python\\vscode-support\\'
os.makedirs(dest + '\\.vscode')
dest = dest + '\\.vscode'

names = os.listdir(src)
for name in names:
    shutil.copy2(src + name, dest)