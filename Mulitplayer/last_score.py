import Mulitplayer.IDgenerate as idgen
import Mulitplayer.database as db
import Mulitplayer.high_score

#input the score. and use diskID for ID
def insert_last_score(score):
    id = idgen.codegen() #getID
    try:
        #import the score into database
        sql_command = 'UPDATE `pygame`.`flappybird` SET `LAST_SCORE` = \'%s\' WHERE `flappybird`.`ID` = \'%s\'' % (score,id)
    except BaseException as e:
        print(e)
    #print(sql_command)
    db.sql_modify(sql_command)
    Mulitplayer.high_score.high_score(score)  #compare if new record


if __name__ == '__main__':
    score = input("Input Your score")
    insert_last_score(score)