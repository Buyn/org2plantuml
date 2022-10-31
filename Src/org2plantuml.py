#  ----------------------------------------------:
# * import : 
#  ----------------------------------------------:
import sys
import os.path


#  ----------------------------------------------:
# * Vars:
#  ----------------------------------------------:
helptext = """
for mindmap use -m
-r to not use rooting
-h for this help
any not key(start from "-")
 is source file
distanatin is going to 
 workig dir as sandbox.plantuml
"""
filename = "sandbox.org"
mindmap = False
root = False



#  ----------------------------------------------:
# * def main(argv):
# ----------------------------------------------
def main(argv):
    cmd_line_arg(argv)
    if not os.path.exists(filename):
        print("File not exists: ", filename)
        sys.exit()
    with open("sandbox.plantuml", "w") as fo:
        if mindmap:
          fo.write("@startmindmap\n")
        else:
          fo.write("@startwbs\n")
        rooting(fo)
        # fo.write("* " + filename + "\n")
        lastline = ""
        lastline_is_header = True
        with open(filename, "r", encoding='UTF8' ) as fi:
            for line in fi:
                line =  line.replace(";", "!") 
                if line.startswith("*"):
                    # line = "*" + line
                    line = rooting(fo, line)
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
                if line.endswith("left side\n"):
                    line = "left side\n"
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



# ----------------------------------------------
# * main functions :
# **  ----------------------------------------------
# ** cmd_line_arg :
def cmd_line_arg(argv):
    global filename, mindmap, root 
    for arg in sys.argv[1:]:
        # print("arg = ", arg) 
        if arg.startswith("-"):
            if arg.find("m") != -1:
              print("mindmap set to True", arg) 
              mindmap = True
            if arg.find("r") != -1:
              print("rooting no using", arg) 
              root = True
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




# ** def rooting : 
def rooting(fo, astline=None): 
    if root: return astline
    if not astline:
        fo.write("* " + filename + "\n")
    else:
        return "*" + astline


# **  ----------------------------------------------
# * if __name__ : 
# ----------------------------------------------
if __name__ == "__main__": 
    import sys
    # sys.argv = ['', 'Test.testName']
    main(sys.argv)


# ----------------------------------------------
# * ----------------------------------------------:
