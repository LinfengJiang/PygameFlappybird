import Mulitplayer.IDgenerate as idgen
import Mulitplayer.database as db
import Mulitplayer.register as reg

#input the score. and use diskID for ID
def insert_last_score(score):
    id = idgen.codegen()
    try:
        sql_command = 'UPDATE `pygame`.`flappybird` SET `LAST_SCORE` = \'%s\' WHERE `flappybird`.`ID` = \'%s\'' % (score,id)
    except:
        reg.register(name='test')
    print(sql_command)
    db.sql_exec(sql_command)

if __name__ == '__main__':
    score = input("Input Your score")
    insert_last_score(score)