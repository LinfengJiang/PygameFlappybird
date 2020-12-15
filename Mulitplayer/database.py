import pymysql

def sql_modify(sql_command):
    #args address,username,password,databasename
    db = pymysql.connect("45.13.199.46","pygame","srcXaeYBpHtsR22b","pygame")
    #seting a cursor for execute the SQL language
    cursor = db.cursor()

    # cursor.execute("SELECT VERSION()")
    # data = cursor.fetchone()
    # print(data)

    try:
        cursor.execute(sql_command)
        db.commit() #send to server
        data = cursor.fetchall() #take the feedback
        #print(data)
    except:
        #print("Error 11")
        db.rollback()

    db.close()   #important

def sql_search(sql_command):
    #args address,username,password,databasename
    db = pymysql.connect("45.13.199.46","pygame","srcXaeYBpHtsR22b","pygame")
    #seting a cursor for execute the SQL language
    cursor = db.cursor()

    try:
        cursor.execute(sql_command)
        data = cursor.fetchone()
        #print(data)
    except BaseException as e:
        print(e)

    db.close()   #important
    return data