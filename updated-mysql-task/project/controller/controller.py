import db.query as query


def adduser(id, name, age, department, subject):
    res = query.query_adduser(id, name, age, department, subject)
    if res == 200:
        return { "status" : 200, "massage" : "User add successfully"}
    else:
        return {"status": 500, "massage": "Internal Eerror"}

def deleteuser(id):
    res = query.query_deleteuser(id)
    if res == 200:
        return { "status" : 200, "massage" : "User delete successfully"}
    else:
        return {"status": 500, "massage": "Internal Eerror"}

def showuser():
    res = query.query_showuser()
    if res != 200:
        return res
    else:
        return {"status": 500, "massage": "Internal Eerror"}
