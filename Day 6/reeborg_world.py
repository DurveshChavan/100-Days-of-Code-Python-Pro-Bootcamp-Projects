import random


random_number1 = random.randint(0, 1)
random_number2 = random.randint(0, 1)
random_number3 = random.randint(0, 1)
def turn_left():
  print("turned left\n")

def right_is_clear():
  if random_number1 == 0:
    return True
  else:
    return False

def front_is_clear():
  if random_number2 == 0:
    return True
  else:
    return False

def move():
  print("moved Forward\n")

def at_goal():
  if random_number3 == 0:
    print("Reached Goal")
    return True
  else:
    return False
