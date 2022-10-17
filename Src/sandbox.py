#  ----------------------------------------------:
# * import : 
#  ----------------------------------------------:
# import json
# import requests
#  ----------------------------------------------:
# * Code :
#  ----------------------------------------------:

#  ----------------------------------------------:
# * main block:
#  ----------------------------------------------:
# file = open("sandbox.txt")
# line = file.read()
# print(line)
r = []
filename = "sandbox.org"
mindmap = False
# print(r.join(r))
# print("".join(r))
with open("sandbox.plantuml", "w") as fo:
    if mindmap:
      fo.write("@startmindmap\n")
    else:
      fo.write("@startwbs\n")
    fo.write("* " + filename + "\n")
    # f.write("".join(r))
    lastline = ""
    lastline_is_header = True
    with open(filename, "r", encoding='UTF8' ) as fi:
        # line = fi.readline()
        for line in fi:
            # if not line.find("Name") == -1 :
              # print(line)
              # print("")
            # if line.find("Nickname") != -1 and line.find('""') == -1  :
              # print(line)
              # print("")
            line =  line.replace(";", "!") 
            # if line.find("* ") != -1   :
            if line.startswith("*"):
                line = "*" + line
                if line.find(" \n") != -1   :
                    line =  line.replace(" \n", " _\n") 
                if not lastline_is_header:
                  fo.write(lastline)
                  lastline = ";\n"
                  # lastline = lastline.replace("* ", "*:", 1)
                lastline_is_header = True
            else :
                if lastline_is_header:
                  lastline = lastline.replace("* ", "*:", 1)
                  # fo.write(";\n")
                  # lastline = lastline.replace("* ", "*:", 1)
                lastline_is_header = False
            fo.write(lastline)
            lastline = line
    if not lastline_is_header:
      fo.write(lastline)
      fo.write(";\n")
    # if lastline_is_header:
    #   fo.write(";\n")
    else:
      fo.write(lastline)
    if mindmap:
      fo.write("@endmindmap\n")
    else:
      fo.write("@endwbs")
# line = file.read().replace("\n", " ")
# file.close()


#  ----------------------------------------------:
# * ----------------------------------------------:
