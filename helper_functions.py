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
                if (marr < born):
                    continue
                else:
                    arr.append("ERROR: FAMILY: US04: ID: "+ p_id +"F_ID: "+ f_id+": " + name + " was married before they were born.")
    return arr