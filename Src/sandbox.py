#  ----------------------------------------------:
# * import : 
#  ----------------------------------------------:
import sys
import os.path

# file_exists = os.path.exists('readme.txt')
#  ----------------------------------------------:
# * Code :
#  ----------------------------------------------:
helptext = "for mindmap use -m"
print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
for arg in sys.argv[1:]:
    print("arg = ", arg) 
    if arg.startswith("-"):
        if arg.find("f") != -1:
          print("mindmap set to True", arg) 
        if arg.find("h") != -1:
          print(helptext) 
    else:
        if arg.find("\\") != -1:
            print("is windows path")
            arg = arg.replace("\\", "/")
        if not os.path.exists(arg):
            print("File not exists: ", arg)
            sys.exit()
        print("file found")


#  ----------------------------------------------:
# * main block:
#  ----------------------------------------------:

#  ----------------------------------------------:
# * ----------------------------------------------:
