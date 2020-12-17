import Mulitplayer.IDgenerate as idgen
import Mulitplayer.database as db


def high_score(score):
    id = idgen.codegen()  # getID
    try:  # get personal high score
        sql_command = 'SELECT HIGH_SCORE FROM flappybird WHERE ID = \'%s\'' % (id)
    except BaseException as e:
        print(e)
    personal_high_score_old = db.sql_search(sql_command)  # get data
    personal_high_score_old = personal_high_score_old[0]  # take the data from list
    personal_high_score_old = int(personal_high_score_old)  # cover the data into nummber

    try:  #get most high score
        sql_command = 'SELECT MAX(HIGH_SCORE) FROM flappybird'
    except BaseException as e:
        print(e)
    most_high_score_old = db.sql_search(sql_command)
    most_high_score_old = most_high_score_old[0]
    most_high_score_old = int(most_high_score_old)

    if score > personal_high_score_old:  # compare the new score and old personal high score
        print('You reach the new record!')
        try:
            # import the score into database
            sql_command = 'UPDATE `pygame`.`flappybird` SET `HIGH_SCORE` = \'%s\' WHERE `flappybird`.`ID` = \'%s\'' % (
                score, id)
        except BaseException as e:
            print(e)
        db.sql_modify(sql_command)
    if score > most_high_score_old:
        print('You make the most high score')


if __name__ == '__main__':
    high_score(1)
