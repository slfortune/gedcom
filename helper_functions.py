from dateutil import parser

# insert all functions made during sprints here
# import this with project3 code to test functions


def marrBeforeDiv(family, individual):
    arr = []
    for row in individual:
        f_id = row[8]
        name = row[1]
        for row in family:
            if row[0] == f_id:
                if row[2] != "NA":
                    marr = parser.parse(row[1])
                    div = parser.parse(row[2])
                    if (marr < div):
                        continue
                    else:
                        arr.append("Error: " + name + " was divorced before they were married.")
                else:
                    continue
    return arr
    
def marrBeforeDeath(family, individual):
    arr = []
    for row in individual:
        f_id = row[8]
        name = row[1]
        if row[6] != "NA" :
            death = parser.parse(row[6])
            for rowr in family:
                if rowr[0] == f_id:
                    marr = parser.parse(rowr[1])
                    if (marr < death):
                        continue
                    else:
                        arr.append("Error: " + name + " died before they were married.")
                else:
                    continue
    return arr



def birthBeforeMarr(family, individual):
    arr = []
    for row_i in individual:
        f_id = row_i[8]
        name = row_i[1]
        p_id = row_i[0]
        born = parser.parse(row_i[3])
        for row_f in family:
            if row_f[0] == f_id:
                marr = parser.parse(row_f[1])
                if (born < marr):
                    continue
                else:
                    arr.append("ERROR: FAMILY: US02: ID: "+ p_id +" F_ID: "+ f_id+": " + name + " was married before they were born.")
    return arr

'''
def marrBeforeDeath(family, individual):
    arr = []
    for row_i in individual:
        f_id = row_i[8]
        name = row_i[1]
        p_id = row_i[0]
        if row_i[6] != 'NA':
            death = parser.parse(row_i[6])
            for row_f in family:
                if row_f[0] == f_id:
                    marr = parser.parse(row_f[1])
                    if (marr < death):
                        continue
                    else:
                        arr.append("ERROR: FAMILY: US05: ID: "+ p_id +" F_ID: "+ f_id+": " + name + " died before they got married.")
    return arr

    '''

def birthBeforeDeath(family, individual):
    arr = []
    for row_i in individual:
        name = row_i[1]
        p_id = row_i[0]
        born = parser.parse(row_i[3])
        if row_i[6] != 'NA':
            death = parser.parse(row_i[6])
            if(born< death):
                continue
            else:
                arr.append("ERROR: INDIVIDUAL: US03: ID: "+ p_id +": " + name + " died before they were born.")
    return arr



def divBeforeDeath(family, individual):
    arr = []
    for row in individual:
        f_id = row[8]
        name = row[1]
        if row[6] != "NA":
            death = parser.parse(row[6])
            for rowr in family:
                if rowr[0] == f_id:
                    if rowr[2] != "NA":
                        div = parser.parse(rowr[2])
                        if (div < death):
                            continue
                        else:
                            arr.append("Error: " + name + " died before they were divorced.")
                else:
                    continue
    return arr

def lessThan150(family, individual):
    arr = []
    for row in individual:
        f_id = row[8]
        name = row[1]
        age = row[4]
        if (age < 150):
            continue
        else:
            arr.append("Error: " + name + " is over 150 years old.")
    return arr

def birthBeforePMarriage(family, individual):
    arr = []
    for row in individual:
        f_id = row[8]
        name = row[1]
		born = parser.parse(row[3])
            for rowf in family:
                if rowf[0] == f_id:
                    marr = parser.parse(rowr[4])
                    if (born < marr):
                        continue
                    else:
                        arr.append("Error: " + name + " was born after their parents' marriage.")
                else:
                    continue
    return arr
	
def birthBeforePDeath(family, individual):
    arr = []
    for row in individual:
        f_id = row[8]
        name = row[1]
		born = parser.parse(row[3])
        if row[6] != "NA":
            death = parser.parse(row[6])
            for rowf in family:
                if rowf[0] == f_id:
                    if (born < death):
                        continue
                    else:
                        arr.append("Error: " + name + " was born after their parents' death.")
                else:
                    continue
    return arr

'''
i1 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 1982', '@F1@', '@F5@'],
['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

f1 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
['@F3@', '07 Mar 2002', '08 Jun 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
result = birthBeforeDeath(f1, i1)
print(result)

'''
