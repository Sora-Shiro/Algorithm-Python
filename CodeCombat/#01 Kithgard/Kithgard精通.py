lt = ["1up", "3right", "1up", "1down", "1right", "1Friend", "2right", "1up", "11", "2up", "1attack", "4left", "3up", "3right", "1up", "1down", "1right", "1Friend", "2right", "1up", "12", "2up", "1attack", "5left"]
for string in lt:
    time = string[0]
    command = string[1:]
    for i in range(0, time):
        if command == "up" : 
            hero.moveUp()
        elif command == "down" :
            hero.moveDown()
        elif command == "left" :
            hero.moveLeft()
        elif command == "right":
            hero.moveRight()
        elif command == "attack":
            enemy = hero.findNearestEnemy()
            while enemy:
                hero.attack(enemy)
                enemy = hero.findNearestEnemy()
        else:
            hero.say(command)