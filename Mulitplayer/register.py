import Mulitplayer.IDgenerate as idgen
import Mulitplayer.database as db

#input a name as plyer name. and use diskID for ID
def register(name):
    id = idgen.codegen()
    sql_command = 'INSERT INTO flappybird(ID,NAME) VALUES (\'%s\',\'%s\')' % (id,name)
    print(sql_command)
    db.sql_exec(sql_command)

if __name__ == '__main__':
    name = input("Input Your Username")
    register(name)