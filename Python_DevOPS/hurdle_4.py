# Python code for Hurdle_4 challenge: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_wall():
    turn_left()
    move()
    step = 1
    while not right_is_clear():
        step += 1
        move()
    turn_right()
    move()
    turn_right()
    for i in range(step):
        move()
    turn_left()

    
while not at_goal():
    if wall_in_front():
        jump_wall()
    else:
        move()
    
