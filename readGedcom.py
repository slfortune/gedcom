validTags = ["INDI","NAME","SEX","BIRT","DEAT","FAMC","FAMS","FAM","MARR","HUSB","WIFE","CHIL","DIV","DATE","HEAD","TRLR","NOTE"]

file1 = open('myFamily.txt')
Lines = file1.readlines()

def num_there(s):
    return any(i.isdigit() for i in s)


for line in Lines:
    line_list = line.split(" ")
    line_list[len(line_list)-1] = line_list[len(line_list)-1].replace("\n","")
    #print(line_list)
    print('--> ' + line)

    level = line_list[0]
    tag = ""
    if(line_list[1].upper() == line_list[1] and not num_there(line_list[1])):
        tag = line_list[1]
    elif(line_list[2].upper() == line_list[2]):
        tag = line_list[2]

    valid = "N"
    if (tag in validTags):
        valid = "Y"
    
    line_list.remove(level)
    line_list.remove(tag)
    line_list_string = ''
    for item in line_list:
        line_list_string = line_list_string + item + " "

    print('<-- '+level+'|'+tag+'|'+valid+'|'+ line_list_string)
    print('')
