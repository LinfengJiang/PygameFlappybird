import pymysql

def sql_exec(sql_command):
    #args address,username,password,databasename
    db = pymysql.connect("45.13.199.46","pygame","srcXaeYBpHtsR22b","pygame")
    cursor = db.cursor()

    # cursor.execute("SELECT VERSION()")
    # data = cursor.fetchone()
    # print(data)

    try:
        cursor.execute(sql_command)
        db.commit()
        data = cursor.fetchall()
        print(data)
    except:
        print("Error 11")
        db.rollback()

    db.close()   #important
