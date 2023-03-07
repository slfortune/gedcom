from tabulate import tabulate
from helper_functions import *

filename = "newFamily.ged"

indi = [[0 for j in range(9)] for i in range(34)]
fam = [[0 for j in range(8)] for i in range(8)]

tags = ['INDI', 'FAM', 'HEAD', 'TRLR', 'NOTE']
tag1 = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV']
date = ['DATE']
decide = ['INDI', 'FAM']
match = False

months = {"JAN": 1,"FEB": 2,"MAR": 3,"APR": 4,"MAY": 5,"JUN": 6,"JUL": 7,"AUG": 8,"SEP": 9,"OCT": 10,"NOV": 11,"DEC": 12,}

row = -1
famrow = -1
dead = False
marriage = 1 
#1 false, 2 true, 3 divorced

with open(filename, "r") as file:
# insert data
    for myline in file:
        line = myline.strip('\n')
        lvl = line[0]
        W = line.split()
        L = W[-1]

        if L == 'FAM' or L == 'INDI':
            tag = W[-1]
            hold = W[1:-1]
            hold = " ".join(hold)
        elif lvl == '0' and line[2:6] != 'HEAD' and line[2:6] != 'TRLR' and line[2:6] != 'NOTE':            
            tag = W[-1]
            hold = W[1:]
            hold = " ".join(hold)
        else:
            tag = W[1]
            hold = W[2:]
            hold = " ".join(hold)

        if lvl == "0":
            if tag in tags:
                match = True
        elif lvl == "1":
            if tag in tag1:
                match = True
        elif lvl == "2":
            if tag in date:
                match = True
        if match == True:
            valid = 'Y'
        else:
            valid = 'N'

# check individual data

        if lvl == "0" and tag in decide:
            row += 1       
        if tag == "INDI":
            indi[row][0] = hold
        elif tag == "NAME":
            indi[row][1] = hold
        elif tag == "SEX":
            indi[row][2] = hold
        elif tag == "BIRT":
            dead = False
            marriage = 1
        elif tag == "DEAT":
            dead = True
            marriage = 1
        elif tag == "DATE":
            if marriage == 1:
                if dead == False:
                    indi[row][3] = hold
                    indi[row][6] = "NA"
                else:
                    indi[row][6] = hold
            elif marriage == 2:
                fam[famrow][1] = hold
            else:
                fam[famrow][2] = hold
        elif tag == "FAMS":
            indi[row][8] = hold
        elif tag == "FAMC":
            indi[row][7] = hold

# check family data
        elif tag == "FAM":
            famrow += 1
            fam[famrow][0] = hold
        elif tag == "MARR":
            marriage = 2
        elif tag == "HUSB":
            fam[famrow][3] = hold
            for b in indi:
                if b[0] == hold:
                    fam[famrow][4] = b[1]
        elif tag == "WIFE":
            fam[famrow][5] = hold
            for c in indi:
                if c[0] == hold:
                    fam[famrow][6] = c[1]
        elif tag == "CHIL":
            holdlist = [hold]
            if type(fam[famrow][7]) is list:
                fam[famrow][7].append(hold)
            else:
                fam[famrow][7] = holdlist
        elif tag == "DIV":
            marriage = 3
        if fam[famrow][1] == 0:
            fam[famrow][1] = "NA"
        if fam[famrow][2] == 0:
            fam[famrow][2] = "NA"
        
# calculate and record age
    curr_day = 22
    curr_month = 2
    curr_year = 2023

    rownum = 0
    
    for x in indi:
        if indi[rownum][3] == 0:
            break
        birthday = indi[rownum][3]
        day, month, year = birthday.split()

        day = int(day)
        month = months[month]
        year = int(year)
        year = curr_year - year

        if month >= curr_month and day > curr_day:
            age = year - 1
        else:
            age = year
        
        indi[rownum][4] = age
        rownum += 1

    # individual counter
    ctr1 = 0
    for person in indi:
        if (person[0] != 0):
            ctr1 +=1
    individual = indi[:ctr1]

    # family counter
    ctr2 = 0
    for a in individual:
        if a[8] != "NA":
            fam[ctr2][0] = a[8]

    # print individual data
    indvheaders = ['ID', 'NAME', 'GENDER', 'BIRTHDAY', 'AGE', 'ALIVE', 'DEATH', 'CHILD', 'SPOUSE']
    indtable = [indvheaders] + individual
    # print(tabulate(individual, headers=indvheaders, tablefmt='fancy_grid'))

    # print family data
    famheaders = ['ID', 'MARRIED', 'DIVORCED', 'HUSBAND ID', 'HUSBAND NAME', 'WIFE ID', 'WIFE NAME', 'CHILDREN']
    famtable = [famheaders] + fam
    # print(tabulate(fam, headers=famheaders, tablefmt='fancy_grid'))

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(tabulate(individual, headers=indvheaders, tablefmt='fancy_grid'))
        f.write(tabulate(fam, headers=famheaders, tablefmt='fancy_grid'))
