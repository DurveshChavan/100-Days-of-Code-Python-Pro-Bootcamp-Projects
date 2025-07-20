import reeborg_world

def turn_right():
    reeborg_world.turn_left()
    reeborg_world.turn_left()
    reeborg_world.turn_left()

def turn_around():
    reeborg_world.turn_left()
    reeborg_world.turn_left()

while reeborg_world.right_is_clear() and reeborg_world.front_is_clear():
    reeborg_world.move()
turn_around()
 
while not reeborg_world.at_goal():
    if reeborg_world.right_is_clear():
        turn_right()
        reeborg_world.move()
    elif reeborg_world.front_is_clear():
        reeborg_world.move()
    else:
        reeborg_world.turn_left()

