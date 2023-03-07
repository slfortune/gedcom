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