import Mulitplayer.IDgenerate as idgen
import Mulitplayer.database as db

def high_score(score):
    id = idgen.codegen() #getID
    try:   #gei personal high score
        sql_command = 'SELECT HIGH_SCORE FROM flappybird WHERE ID = \'%s\'' % (id)
    except BaseException as e:
        print(e)
    personal_high_score_old =db.sql_search(sql_command) #get data
    personal_high_score_old = personal_high_score_old[0] #take the data from list
    personal_high_score_old = int(personal_high_score_old) #cover the data into nummber

    if score > personal_high_score_old:     #compare the new score and old personal high score
        print('Your reach the new record!')
        try:
            # import the score into database
            sql_command = 'UPDATE `pygame`.`flappybird` SET `HIGH_SCORE` = \'%s\' WHERE `flappybird`.`ID` = \'%s\'' % (
            score, id)
        except BaseException as e:
            print(e)
        db.sql_modify(sql_command)