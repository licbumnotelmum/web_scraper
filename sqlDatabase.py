def invokeSql():
    import mysql.connector

    conn = mysql.connector.connect(host="localhost",user="root",password="667987",database="erpx")
    cursor = conn.cursor() 
    return conn,cursor

def insertUserName(userId , userName):
    _ , cursor =invokeSql()
    query = f"insert users values('{userId}','{userName}');"
    cursor.execute(query)

    _.commit()
    _.close()

def insertStudent(userID, enrollNo, dob, aadhar, pan, studPhNo, email):
    _ , cursor =invokeSql()
    query = f"insert student values('{userID}','{dob}','{aadhar}','{pan}','{studPhNo}','{email}','{enrollNo}');"
    cursor.execute(query)

    _.commit()
    _.close()

def insertFather(userID,name,PhNo,alterNo,dob,occ):
    _ , cursor =invokeSql()
    query = f"insert father values('{userID}','{name}','{PhNo}','{alterNo}','{dob}','{occ}');"
    cursor.execute(query)

    _.commit()
    _.close()

def insertMother(userID,mother,PhNo,alterNo,dob,occ):
    _ , cursor =invokeSql()
    query = f"insert mother values('{userID}','{mother}','{PhNo}','{alterNo}','{dob}','{occ}');"
    cursor.execute(query)

    _.commit()
    _.close()

def insertSiblings(userID,relation,name,dob,phNo,email,edu,occ):
    _ , cursor =invokeSql()
    query = f"insert siblings values('{userID}','{relation}','{name}','{dob}','{phNo}','{email}','{edu}','{occ}');"
    cursor.execute(query)

    _.commit()
    _.close()

def insertAddress(userID,buildName,plotNo,street,landmark,area,village,pincode):
    _ , cursor =invokeSql()
    query = f"insert paddress values('{userID}','{buildName}','{plotNo}','{street}','{landmark}','{area}','{village}','{pincode}');"
    cursor.execute(query)

    _.commit()
    _.close()

