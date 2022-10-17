#  ----------------------------------------------:
# * import : 
#  ----------------------------------------------:
import sys
import os.path
#  ----------------------------------------------:
# * Code :
#  ----------------------------------------------:

#  ----------------------------------------------:
# * main block:
#  ----------------------------------------------:
filename = "sandbox.org"
mindmap = False
helptext = """
for mindmap use -m
-h for this help
"""
# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))
for arg in sys.argv[1:]:
    # print("arg = ", arg) 
    if arg.startswith("-"):
        if arg.find("f") != -1:
          print("mindmap set to True", arg) 
          mindmap = True
        if arg.find("h") != -1:
          print(helptext) 
          sys.exit()
    else:
        if arg.find("\\") != -1:
            print("is windows path")
            arg = arg.replace("\\", "/")
        if not os.path.exists(arg):
            print("File not exists: ", arg)
            sys.exit()
        # print("file found")
        filename = arg

if not os.path.exists(filename):
    print("File not exists: ", filename)
    sys.exit()
with open("sandbox.plantuml", "w") as fo:
    if mindmap:
      fo.write("@startmindmap\n")
    else:
      fo.write("@startwbs\n")
    fo.write("* " + filename + "\n")
    lastline = ""
    lastline_is_header = True
    with open(filename, "r", encoding='UTF8' ) as fi:
        for line in fi:
            line =  line.replace(";", "!") 
            if line.startswith("*"):
                line = "*" + line
                if line.find(" \n") != -1   :
                    line =  line.replace(" \n", " _\n") 
                if not lastline_is_header:
                  fo.write(lastline)
                  lastline = ";\n"
                lastline_is_header = True
            else :
                if lastline_is_header:
                  lastline = lastline.replace("* ", "*:", 1)
                lastline_is_header = False
            fo.write(lastline)
            lastline = line
    if not lastline_is_header:
      fo.write(lastline)
      fo.write(";\n")
    else:
      fo.write(lastline)
    if mindmap:
      fo.write("@endmindmap\n")
    else:
      fo.write("@endwbs")

      
#  ----------------------------------------------:
# * ----------------------------------------------:
