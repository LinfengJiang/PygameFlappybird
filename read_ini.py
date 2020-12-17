import configparser


def conf_speed():
    c = configparser.ConfigParser()  # initialize
    c.read('settings.ini')  # read ini file
    X_speed = c.get('difficulty', 'X_speed')  # get X-axis speed from config file
    Y_speed = c.get('difficulty', 'Y_speed')  # get Y-axis speed from config file
    K_up = c.get('difficulty', 'K_Up_speed') # get k_up speed
    X_speed = int(X_speed)
    Y_speed = int(Y_speed)
    K_up = int(K_up)   # cover str into int
    return {'X_speed': X_speed, 'Y_speed': Y_speed, 'K_up': K_up}  #return as dict


if __name__ == '__main__':
    conf_speed()
